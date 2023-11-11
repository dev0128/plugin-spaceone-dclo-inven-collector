from typing import List
from cloudforet.plugin.lib.model.cloud_service_type_model import BaseCloudServiceType

_METADATA = {
    'view': {
        'search': [
            {
                'key': 'data.ruleset_name',
                'name': 'Ruleset Name'
            },
        ],
        'table': {
            'layout': {
                'name': '',
                'type': 'query-search-table',
                'options': {
                    'default_sort': {
                        'key': 'data.rulest_name',
                        'desc': False
                    },
                    'fields': [
                        {
                            'type': 'text',
                            'key': 'data.rulest_name',
                            'name': 'Ruleset Name',
                        },
                        {
                            'type': 'text',
                            'key': 'data.rulest_desc',
                            'name': 'Description',
                        },
                        # 상중하 secure 갯수 있으면 좋겠다?
                        # 점수?
                    ]
                }
            },
        },
        'widget': [
            # 갯수 합치는 작업하면 좋을듯?
        ],
        'sub_data': {
            'layouts': [
                {
                    'type': 'table',
                    'name': 'Detail',
                    'options': {
                        'fields': [
                            {
                                'type': 'text',
                                'key': 'code',
                                'name': 'Code'
                            },
                            {
                                'type': 'text',
                                'key': 'category',
                                'name': 'Category',
                            },
                            {
                                'type': 'text',
                                'key': 'name',
                                'name': 'Name',
                            },
                            {
                                'type': 'text',
                                'key': 'report_lv',
                                'name': 'Severity',
                            },
                            {
                                'type': 'text',
                                'key': 'status',
                                'name': 'Status',
                            },
                            {
                                'name': 'Secure Details',
                                'type': 'more',
                                'key': 'id',
                                "options": {
                                    "sub_key": "good_key", 
                                    "layout": {
                                        "name": "Secure meta",
                                        "type": "popup",
                                        "options": {
                                            "layout": { 
                                                "type": "raw",
                                            }
                                        }
                                    }
                                }
                            },
                            {
                                'name': 'Flag Details',
                                'type': 'more',
                                'key': 'id',
                                "options": {
                                    "sub_key": "flag_key", 
                                    "layout": {
                                        "name": "Flag meta",
                                        "type": "popup",
                                        "options": {
                                            "layout": { 
                                                "type": "raw",
                                            }
                                        }
                                    }
                                }
                            },
                        ],
                        'root_path': 'data.findings'
                    }
                },
            ]
        }
    }
}


class CloudServiceType(BaseCloudServiceType):
    group: str = 'D-CLO'
    is_primary: bool = True
    is_major: bool = True
    metadata: dict = _METADATA
    labels: List[str] = ['Security', 'Compliance']
    tags: dict = {
        'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/spaceone.svg'
    }
