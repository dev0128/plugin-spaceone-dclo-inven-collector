import logging
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
                    {'1': ['reference.resource_id', 'provider', 'cloud_service_type', 'cloud_service_group', 'account']}
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
        # type 설정 secret 인지, role 인지
        selected_provider = options['provider']
        
        if "role_arn" in secret_data:
            key_type = f'{selected_provider.upper()}-002'
            diag_data = {"arg_1": secret_data['external_id'], "arg_2": secret_data['role_arn']}
        else:
            key_type = f'{selected_provider.upper()}-001'
            diag_data = {"arg_1": secret_data['aws_access_key_id'], "arg_2": secret_data['aws_secret_access_key']}

        selected_compliance = options['compliance_framework']
        compliance = COMPLIANCE_FRAMEWORKS[selected_provider][selected_compliance]

        return key_type, compliance, diag_data 

    def _make_compliance_results(self, check_result):
        diag_id = check_result.get('diag_id')
        result = check_result.get('payload', {})

        compliance_result = {
            'name': diag_id,
            'test': "",
            'reference': {
                'resource_id': self.cloud_service_type,
            },
            'data': result,
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
            'account': diag_id,
            'provider': self.provider,
            'cloud_service_group': self.cloud_service_group,
            'cloud_service_type': self.cloud_service_type,
            'region_code': 'global'
        }

        return [compliance_result]


