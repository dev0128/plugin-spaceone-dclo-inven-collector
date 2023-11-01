import logging
from spaceone.core.error import ERROR_REQUIRED_PARAMETER
from spaceone.core.connector import BaseConnector

_LOGGER = logging.getLogger(__name__)


class DcloConnector(BaseConnector):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def verify_client(self, options: dict, secret_data: dict, schema: str):
        self._check_secret_data(secret_data)

    def list_code(self, provider_name) -> dict:
        """
        """

        response = {
            'provider_name': provider_name,
            'payload': [
                {
                    "id": "REME-0100900001",
                    "code": "AWS-CDN-001",
                    "name": "CloudFront 기본 루트 객체 구성 여부",
                    "category": "CloudFront",
                    "report_lv": "Medium",
                    "status": "N/A",
                    "findings": {
                        "defaultInfo":{
                                        "code": "AWS-CDN-001",
                                        "name": "CloudFront 기본 루트 객체 구성 여부",
                                        "category": "CloudFront",
                                        "report_lv": "Medium",
                                        "desc": "- 기본 루트 객체를 구성하여 운영하는 경우 사용자가 도메인 이름만 입력했을 때 미리 구성된 기본 루트 객체를 반환하여 의도치 않은 리소스 노출(디렉토리 리스팅)을 방지하고 서버의 기본 오류 페이지를 통한 서버 정보 노출을 막을수 있습니다.", 
                                        "standard": "AWS CloudFront에서 기본 루트 객체를 구성하였을 경우 양호", 
                                        "how_act": " [CloudFront] > [배포] > 생성된 배포 선택 > [일반] > [편집] > 기본값 루트 객체 작성(환경에 맞게 루트 요청시 반환할 파일 이름 작성) > [변경 사항 저장]"
                                      },
                        "compliance":[
                                        {
                                            "name": "ISMS-P",
                                            "type": "ISMS-P",
                                            "comNum": [
                                                "2.6.2",
                                                "2.10.2-C"
                                            ]
                                        },
                                        {
                                            "name": "KISA-CSAP(표준)",
                                            "type": "KISA-CSAP",
                                            "comNum": [
                                                "10.1.1"
                                            ]
                                        },
                                        {
                                            "name": "CSP 안전성 평가",
                                            "type": "CSP",
                                            "comNum": [
                                                "10.1.1"
                                            ]
                                        },
                                        {
                                            "name": "ISO-27001",
                                            "type": "ISO27001",
                                            "comNum": [
                                                "A.9.4.1"
                                            ]
                                        }
                                     ],
                        "flag": [],
                        "secure": []
                    }
                },
                {
                    "id": "REME-0100500005",
                    "code": "AWS-RDS-005",
                    "category": "RDS",
                    "name": "RDS 로깅 설정",
                    "report_lv": "Low",
                    "status": 'True',
                    "findings": {
                        "defaultInfo":{
                                        "code": "AWS-RDS-005",
                                        "name": "RDS 로깅 설정",
                                        "category": "RDS",
                                        "report_lv": "Low",
                                        "desc": "- 기본 루트 객체를 구성하여 운영하는 경우 사용자가 도메인 이름만 입력했을 때 미리 구성된 기본 루트 객체를 반환하여 의도치 않은 리소스 노출(디렉토리 리스팅)을 방지하고 서버의 기본 오류 페이지를 통한 서버 정보 노출을 막을수 있습니다.", 
                                        "standard": "AWS CloudFront에서 기본 루트 객체를 구성하였을 경우 양호", 
                                        "how_act": " [CloudFront] > [배포] > 생성된 배포 선택 > [일반] > [편집] > 기본값 루트 객체 작성(환경에 맞게 루트 요청시 반환할 파일 이름 작성) > [변경 사항 저장]"
                                      },
                        "compliance":[
                                        {
                                            "name": "ISMS-P",
                                            "type": "ISMS-P",
                                            "comNum": [
                                                "2.6.2",
                                                "2.10.2-C"
                                            ]
                                        },
                                        {
                                            "name": "KISA-CSAP(표준)",
                                            "type": "KISA-CSAP",
                                            "comNum": [
                                                "10.1.1"
                                            ]
                                        },
                                     ],
                        "flag": [{'id':'q1v2eqweq', 'name': 'test', 'resource_type': "test", 'region' : 'test', 'findings': {}},{'id':'q1v2eqweq', 'name': 'test', 'resource_type': "test", 'region' : 'test', 'findings': {'a':1 , 'b':2, 'c': {'1': 1, '2': [1,2,3]}}}],
                        "secure": [{'id':'q1v2eqweq', 'name': 'test', 'resource_type': "test", 'region' : 'test', 'findings': {}},{'id':'q1v2eqweq', 'name': 'test', 'resource_type': "test", 'region' : 'test', 'findings': {}}]
                    }
                }
            ]
        }
        return response

    @staticmethod
    def _check_secret_data(secret_data: dict):
        if 'user_email' not in secret_data:
            raise ERROR_REQUIRED_PARAMETER(key='secret_data.user_email')

        if 'api_key' not in secret_data:
            raise ERROR_REQUIRED_PARAMETER(key='secret_data.api_key')
