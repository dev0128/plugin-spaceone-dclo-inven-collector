import logging
import hashlib
import re
import json

from spaceone.core.error import ERROR_INVALID_PARAMETER

from cloudforet.plugin.lib.manager.collector_manager import CollectorManager
from cloudforet.plugin.model.collector import COMPLIANCE_FRAMEWORKS
from cloudforet.plugin.model.dclo_model import CloudServiceType
from cloudforet.plugin.connector.dclo_connector import DcloConnector

_LOGGER = logging.getLogger(__name__)


class DcloManager(CollectorManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dclo_connector: DcloConnector = self.locator.get_connector(DcloConnector)
        self.provider = 'aws'
        self.cloud_service_group = 'D-CLO'
        self.cloud_service_type = None

    def verify_client(self, options: dict, secret_data: dict, schema: str = None) -> None:
        self.dclo_connector.verify_client(options, secret_data, schema)


    def collect(self, options: dict, secret_data: dict, schema):
        self.cloud_service_type = options['compliance_framework']
        self._check_compliance_framework()

        try:
            # Collect Cloud Service Type
            cloud_service_type = CloudServiceType(group=self.cloud_service_group, 
                                                  name=self.cloud_service_type,
                                                  provider=self.provider)
            yield self.make_response(   
                cloud_service_type.dict(),
                {'1': ['name', 'group', 'provider']},
                resource_type='inventory.CloudServiceType'
            )

            # Collect Cloud Services
            key_type, compliance, diag_data = self._covert_options(options, secret_data)
            compliance_results = self.dclo_connector.fetch_compliance_results(key_type, compliance, diag_data)

            for compliance_result in self._make_compliance_results(compliance_results):
                yield self.make_response( compliance_result,
                    {'1': ['reference.resource_id', 'provider', 'cloud_service_type', 'cloud_service_group', 'account', 'name']}
                )

        except Exception as e:
            yield self.error_response(e)


    def _check_compliance_framework(self):
        all_compliance_frameworks = list(COMPLIANCE_FRAMEWORKS['aws'].keys())
        if self.cloud_service_type not in all_compliance_frameworks:
            raise ERROR_INVALID_PARAMETER(key='options.compliance_framework',
                                          reason=f'Not supported compliance framework. '
                                                 f'(compliance_frameworks = {all_compliance_frameworks})')


    def _covert_options(self, options, secret_data):
        selected_provider = options['provider']

        if "role_arn" in secret_data:
            key_type = f'{selected_provider.upper()}-002'
            diag_data = {"arg_1": secret_data['role_arn'], "arg_2": secret_data['external_id']}
            diag_data['id'] = hashlib.md5(secret_data['role_arn'].encode()).hexdigest()
        else:
            key_type = f'{selected_provider.upper()}-001'
            diag_data = {"arg_1": secret_data['aws_access_key_id'], "arg_2": secret_data['aws_secret_access_key']}
            diag_data['id'] = hashlib.md5(secret_data['aws_access_key_id'].encode()).hexdigest()

        selected_compliance = options['compliance_framework']
        compliance = COMPLIANCE_FRAMEWORKS[selected_provider][selected_compliance]

        return key_type, compliance, diag_data 

    def _make_compliance_results(self, check_result):
        results = []

        account_id = check_result.get('diag_id')
        payload = check_result.get('payload', {})
        
        findings = payload.get('findings')
        for finding in findings:
            code = {
                'account': account_id,
                'name': finding['code'],
                'reference': {
                    'resource_id': self.cloud_service_type,
                },
                'data': self._covert_description_to_markdown(finding),
                'metadata': {
                    'view': {
                        'sub_data': {
                            'reference': {
                                'resource_type': 'inventory.CloudServiceType',
                                'options': {
                                    'provider': self.provider,
                                    'cloud_service_group': self.cloud_service_group,
                                    'cloud_service_type': self.cloud_service_type,
                                }
                            }
                        }
                    }
                },
                'provider': self.provider,
                'cloud_service_group': self.cloud_service_group,
                'cloud_service_type': self.cloud_service_type,
                'region_code': 'global'
            }

            results.append(code)

        return results

    def _covert_description_to_markdown(self, finding):
        finding['findings_cnt'] = f"{finding['flag_items']} / {finding['checked_items']}" if finding['checked_items'] else '-'
        
        for key in finding:
            if key in ['compliance_decs','rule_standard','action_plan',]:
                finding[key] = self._format_text_and_json(finding[key])      
            if key in ['flag_key', 'good_key']:
                finding[key] = [
                    {
                        "region": row['region'], 
                        "id": row['id'], 
                        "name": row['name'],
                        "resource_type": row['resource_type'],
                        'popup_data': json.dumps(row['findings'], indent=4, separators=(',', ': ')) 
                    } for row in finding[key]]

        return finding

    

    def _format_text_and_json(self, text):
        text = text.replace("\r\n", " ")
        text = text.replace("b:", "")
        text = text.replace("b-h2:", "")
        text = text.replace("h2:", "")
        text = text.replace("h1:", "")

        return text

        