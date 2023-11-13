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
                        'key': 'data.ruleset_name',
                        'desc': False
                    },
                    'fields': [
                        {
                            'type': 'text',
                            'key': 'data.ruleset_name',
                            'name': 'Ruleset Name',
                        },
                        {
                            'type': 'text',
                            'key': 'data.ruleset_desc',
                            'name': 'Description',
                        },
                        {
                            'type': 'text',
                            'key': 'data.total_count.H',
                            'name': 'High',
                        },
                        {
                            'type': 'text',
                            'key': 'data.total_count.M',
                            'name': 'Medium',
                        },
                        {
                            'type': 'text',
                            'key': 'data.total_count.L',
                            'name': 'Low',
                        },
                        {
                            'type': 'text',
                            'key': 'data.total_count.Secure',
                            'name': 'Secure',
                        },
                        {
                            'type': 'text',
                            'key': 'data.total_count.N/A',
                            'name': 'N/A',
                        },
                         {
                            'type': 'text',
                            'key': 'data.total_count.Score',
                            'name': 'Score',
                        },
                    ]
                }
            },
        },
        'widget': [
            {
                'name': 'High Count',
                'type': 'summary',
                'options': {
                    'value_options': {
                        'key': 'value',
                        'options': {
                            'default': 0
                        }
                    }
                },
                'query': {
                    'aggregate': [
                        {
                            'count': {
                                'name': 'value'
                            }
                        }
                    ],
                    'filter': [
                        {'key': 'data.total_count.H', 'value': 'High', 'operator': 'eq'},
                    ]
                }
            },
            {
                'name': 'Medium Count',
                'type': 'summary',
                'options': {
                    'value_options': {
                        'key': 'value',
                        'options': {
                            'default': 0
                        }
                    }
                },
                'query': {
                    'aggregate': [
                        {
                            'count': {
                                'name': 'value'
                            }
                        }
                    ],
                    'filter': [
                        {'key': 'data.total_count.M', 'value': 'Medium', 'operator': 'eq'},
                    ]
                }
            },
            {
                'name': 'Low Count',
                'type': 'summary',
                'options': {
                    'value_options': {
                        'key': 'value',
                        'options': {
                            'default': 0
                        }
                    }
                },
                'query': {
                    'aggregate': [
                        {
                            'count': {
                                'name': 'value'
                            }
                        }
                    ],
                    'filter': [
                        {'key': 'data.total_count.L', 'value': 'Low', 'operator': 'eq'},
                    ]
                }
            },
            {
                'name': 'Secure Count',
                'type': 'summary',
                'options': {
                    'value_options': {
                        'key': 'value',
                        'options': {
                            'default': 0
                        }
                    }
                },
                'query': {
                    'aggregate': [
                        {
                            'count': {
                                'name': 'value'
                            }
                        }
                    ],
                    'filter': [
                        {'key': 'data.total_count.Secure', 'value': 'Medium', 'operator': 'eq'},
                    ]
                }
            },
            {
                'name': 'N/A Count',
                'type': 'summary',
                'options': {
                    'value_options': {
                        'key': 'value',
                        'options': {
                            'default': 0
                        }
                    }
                },
                'query': {
                    'aggregate': [
                        {
                            'count': {
                                'name': 'value'
                            }
                        }
                    ],
                    'filter': [
                        {'key': 'data.total_count.N/A', 'value': 'N/A', 'operator': 'eq'},
                    ]
                }
            },
            {
                'name': 'Total Score',
                'type': 'summary',
                'options': {
                    'value_options': {
                        'key': 'value',
                        'options': {
                            'default': 0
                        }
                    }
                },
                'query': {
                    'aggregate': [
                        {
                            'count': {
                                'name': 'value'
                            }
                        }
                    ],
                    'filter': [
                        {'key': 'data.total_count.N/A', 'value': 'N/A', 'operator': 'eq'},
                    ]
                }
            },
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
                                'key': 'flag',
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
