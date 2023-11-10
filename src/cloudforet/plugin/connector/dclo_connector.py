import logging
import requests
import json

from time import sleep
from uuid import uuid4

from spaceone.core.error import ERROR_REQUIRED_PARAMETER, ERROR_REQUEST_TIMEOUT
from spaceone.core.connector import BaseConnector

_LOGGER = logging.getLogger(__name__)

_DCLO_PLUGIN_URL = 'http://43.202.191.177/diag'
class DcloConnector(BaseConnector):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def verify_client(self, options: dict, secret_data: dict, schema: str):
        self._check_options_data(options)
        self._check_secret_data(secret_data)

    def fetch_compliance_results(self, key_type, compliance, secret_data) -> dict:
        diag_id = uuid4().hex

        param = {
            "diag_id": diag_id,
            "type": key_type,
            "arg_1": secret_data['aws_access_key'],
            "arg_2": secret_data['aws_secret_key'],
            "ruleset_id": compliance
        }

        res = requests.post(f"{_DCLO_PLUGIN_URL}/request", headers={'Content-Type': 'application/json'}, data=json.dumps(param))
        result = {}

        PENDING_TIME = 60
        TIME_LIMIT_MINUTE = 30
        
        waiting_timer = 0
        while True:
            sleep(PENDING_TIME)
            waiting_timer += PENDING_TIME

            res = requests.get(f"{_DCLO_PLUGIN_URL}/result/{diag_id}")
            content = json.loads(res.content)
            status = content.get('status')

            if status == 'end':
                result = content.get('result', {})
                break 
            
            if waiting_timer > PENDING_TIME * TIME_LIMIT_MINUTE:
                raise ERROR_REQUEST_TIMEOUT(key='options.provider') 

        response = {
            'diag_id': diag_id,
            'provider_name': 'aws',
            'payload': result
        }
        
        return response

    @staticmethod
    def _check_options_data(options: dict):
        if 'provider' not in options:
            raise ERROR_REQUIRED_PARAMETER(key='options.provider')

        if 'compliance_framework' not in options:
            raise ERROR_REQUIRED_PARAMETER(key='options.compliance_framework')

    @staticmethod
    def _check_secret_data(secret_data: dict):
        if 'aws_access_key_id' not in secret_data:
            raise ERROR_REQUIRED_PARAMETER(key='secret_data.aws_access_key_id')

        if 'aws_secret_access_key' not in secret_data:
            raise ERROR_REQUIRED_PARAMETER(key='secret_data.aws_secret_access_key')