from typing import List
from cloudforet.plugin.lib.model.cloud_service_type_model import BaseCloudServiceType

_METADATA = {
    'view': {
        'search': [
            {
                'key': 'data.code',
                'name': 'Code'
            },
            {
                'key': 'data.name',
                'name': 'Name'
            },
            {
                'key': 'data.category',
                'name': 'Category',
            },
            {
                'key': 'data.report_lv',
                'name': 'Severity',
                'enums': [
                    'High',
                    'Medium',
                    'Low',
                ]
            },
            {
                'key': 'data.flag',
                'name': 'Result',
                'enums': [
                    'Secure',
                    'Vulnerability',
                    'N/A',
                ]
            },
        ],
        'table': {
            'layout': {
                'name': '',
                'type': 'query-search-table',
                'options': {
                    'default_sort': {
                        'key': 'data.code',
                        'desc': False
                    },
                    'fields': [
                        # {
                        #     'type': 'text',
                        #     'key': 'data.code',
                        #     'name': 'Code',
                        # },
                        {
                            'type': 'enum',
                            'key': 'data.category',
                            'name': 'Category',
                        },
                        {
                            'type': 'text',
                            'key': 'data.name',
                            'name': 'Rule Name',
                        },
                        {
                            'type': 'enum',
                            'key': 'data.report_lv',
                            'name': 'Severity',
                            'options': {
                                'High': {
                                    'type': 'badge',
                                    'options': {
                                        'background_color': 'coral.500'
                                    }
                                },
                                'Medium': {
                                    'type': 'badge',
                                    'options': {
                                        'background_color': 'peacock.500'
                                    }
                                },
                                'Low': {
                                    'type': 'badge',
                                    'options': {
                                        'background_color': 'indigo.500'
                                    }
                                }
                            }
                        },
                        {
                            'type': 'enum',
                            'key': 'data.flag',
                            'name': 'Result',
                            'options': {
                                'Vulnerability': {
                                    'type': 'badge',
                                    'options': {
                                        'background_color': 'coral.500'
                                    }
                                },
                                'Secure': {
                                    'type': 'badge',
                                    'options': {
                                        'background_color': 'indigo.500'
                                    }
                                },
                                'N/A': {
                                    'type': 'badge',
                                    'options': {
                                        'background_color': 'dimgray.500'
                                    }
                                }
                            }
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
                        {'key': 'data.report_lv', 'value': 'High', 'operator': 'eq'},
                        {'key': 'data.flag', 'value': 'Vulnerability', 'operator': 'eq'},
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
                        {'key': 'data.report_lv', 'value': 'Medium', 'operator': 'eq'},
                        {'key': 'data.flag', 'value': 'Vulnerability', 'operator': 'eq'},
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
                        {'key': 'data.report_lv', 'value': 'Low', 'operator': 'eq'},
                        {'key': 'data.flag', 'value': 'Vulnerability', 'operator': 'eq'},
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
                        {'key': 'data.flag', 'value': 'Secure', 'operator': 'eq'},
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
                        {'key': 'data.flag', 'value': 'N/A', 'operator': 'eq'},
                    ]
                }
            },
        ],
        'sub_data': {
            'layouts': [
                {
                    'type': 'item',
                    'name': '교정 세부정보',
                    'options': {
                        'fields': [
                            {
                                'type': 'text',
                                'key': 'code',
                                'name': 'Code'
                            },
                            {
                                'type': 'text',
                                'key': 'name',
                                'name': 'Name',
                            },
                            {
                                'type': 'text',
                                'key': 'category',
                                'name': 'Category',
                            },
                            {
                                'type': 'enum',
                                'key': 'report_lv',
                                'name': 'Severity',
                                'options': {
                                    'High': {
                                        'type': 'badge',
                                        'options': {
                                            'background_color': 'coral.500'
                                        }
                                    },
                                    'Medium': {
                                        'type': 'badge',
                                        'options': {
                                            'background_color': 'peacock.500'
                                        }
                                    },
                                    'Low': {
                                        'type': 'badge',
                                        'options': {
                                            'background_color': 'indigo.500'
                                        }
                                    }
                                }
                            },
                            {
                                'type': 'text',
                                'key': 'compliance_decs',
                                'name': 'Description',
                            },
                            {
                                'type': 'text',
                                'key': 'rule_standard',
                                'name': 'Standard',
                            },
                            {
                                'type': 'text',
                                'key': 'action_plan',
                                'name': 'How to Act',
                            },
                        ],
                        'root_path': 'data'
                    }
                },
                {
                    'type': 'table',
                    'name': 'Compliance',
                    'options': {
                        'fields': [
                            {
                                'type': 'text',
                                'key': 'com_1',
                                'name': 'Major',
                                # "options": {
                                #     "outline_color": "violet.500"
                                # },
                            },
                            {
                                'type': 'text',
                                'key': 'com_2',
                                'name': 'Sub',
                                # "options": {
                                #     "outline_color": "violet.500"
                                # },
                            },
                            {
                                'type': 'text',
                                'key': 'com_3',
                                'name': 'Subclass',
                                # "options": {
                                #     "outline_color": "violet.500"
                                # },
                            },
                        ],
                        'root_path': 'data.compliance_dtl'
                    }
                },
                {
                    'type': 'table',
                    'name': 'Flag Details',
                    'options': {
                        'fields': [
                            {
                                'type': 'text',
                                'key': 'region',
                                'name': 'Region'
                            },
                            {
                                'type': 'text',
                                'key': 'id',
                                'name': 'Resource ID'
                            },
                            {
                                'type': 'text',
                                'key': 'name',
                                'name': 'Resource Name'
                            },
                            {
                                'type': 'text',
                                'key': 'resource_type',
                                'name': 'Resource Type'
                            },
                            {
                                'type': 'more',
                                'key': 'show',
                                'name': 'Vulnerability findings',
                                "options": {
                                    "sub_key": "findings", 
                                    "layout": {
                                        "name": "Vulnerability meta",
                                        "type": "popup", 
                                        "options": { 
                                            "layout": { 
                                                "type": "raw", 
                                            }
                                        }
                                    }
                                }
                            }
                        ],
                        'root_path': 'data.flag_key'
                    }
                },
                {
                    'type': 'table',
                    'name': 'Secure Details',
                    'options': {
                        'fields': [
                            {
                                'type': 'text',
                                'key': 'region',
                                'name': 'Region'
                            },
                            {
                                'type': 'text',
                                'key': 'id',
                                'name': 'Resource ID'
                            },
                            {
                                'type': 'text',
                                'key': 'name',
                                'name': 'Resource Name'
                            },
                            {
                                'type': 'text',
                                'key': 'resource_type',
                                'name': 'Resource Type'
                            },
                            {
                                'type': 'more',
                                'key': 'show',
                                'name': 'Secure findings',
                                "options": {
                                    "sub_key": "findings", 
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
                            }
                        ],
                        'root_path': 'data.good_key'
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
