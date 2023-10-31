import logging
import datetime

from cloudforet.plugin.lib.manager.collector_manager import CollectorManager
from cloudforet.plugin.model.dclo_model import CloudServiceType
from cloudforet.plugin.connector.dclo_connector import DcloConnector

_LOGGER = logging.getLogger(__name__)


class DcloManager(CollectorManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.design_connector: DcloConnector = self.locator.get_connector(DcloConnector)
        self.provider = 'aws'
        self.cloud_service_group = 'D-CLO'
        self.cloud_service_type = 'D-CLO'

    def verify_client(self, options: dict, secret_data: dict, schema: str = None) -> None:
        self.design_connector.verify_client(options, secret_data, schema)

    def collect(self, options, secret_data, schema):

        try:
            # Collect Cloud Service Type
            cloud_service_type = CloudServiceType(group=self.cloud_service_group, name=self.cloud_service_type,
                                                  provider=self.provider)
            yield self.make_response(
                cloud_service_type.dict(),
                {'1': ['name', 'group', 'provider']},
                resource_type='inventory.CloudServiceType'
            )

            # Collect Cloud Services (Design members)
            provider_name = "aws"
            codes = self.design_connector.list_code(provider_name)

            for code_result in self._make_code_result(codes):
                yield self.make_response(
                    code_result,
                    {'1': ['reference.resource_id', 'provider', 'cloud_service_type', 'cloud_service_group', 'account']}
                )

        except Exception as e:
            yield self.error_response(e)

    def _make_code_result(self, codes):
        results = []
        payload_codes = codes.get('payload', [])

        for code in payload_codes:
            code_result = {
                'name': code['code'],
                'reference': {
                    'resource_id': code['code']
                },
                'data': code,
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
                # 'account': design_member['department'],
                'provider': self.provider,
                'cloud_service_group': self.cloud_service_group,
                'cloud_service_type': self.cloud_service_type,
                'region_code': 'global'
            }

            results.append(code_result)

        return results
