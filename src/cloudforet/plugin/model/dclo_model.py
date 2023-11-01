from typing import List
from cloudforet.plugin.lib.model.cloud_service_type_model import BaseCloudServiceType

_METADATA = {
    'view': {
        'search': [
            {
                'key': 'data.name',
                'name': 'Name'
            },
            {
                'key': 'data.code',
                'name': 'Code'
            },
            {
                'key': 'data.category',
                'name': 'Service',
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
            # compliace_category ?
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
                        {
                            'type': 'text',
                            'key': 'data.category',
                            'name': 'Resource',
                        },
                        {
                            'type': 'text',
                            'key': 'data.name',
                            'name': 'Name',
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
                            'key': 'data.status',
                            'name': 'Status',
                            'options': {
                                'True': {
                                    'type': 'badge',
                                    'options': {
                                        'background_color': 'crimson.500'
                                    }
                                },
                                'False': {
                                    'type': 'badge',
                                    'options': {
                                        'background_color': 'royalblue.500'
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
            }
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
                        {'key': 'data.weakState', 'value': '취약', 'operator': 'eq'},
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
                        {'key': 'data.weakState', 'value': '취약', 'operator': 'eq'},
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
                        {'key': 'data.weakState', 'value': '취약', 'operator': 'eq'},
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
                        {'key': 'data.weakState', 'value': '양호', 'operator': 'eq'},
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
                        {'key': 'data.weakState', 'value': 'N/A', 'operator': 'eq'},
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
                    'filter': []
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
                                'type': 'text',
                                'key': 'report_lv',
                                'name': 'Severity',
                            },
                            {
                                'type': 'text',
                                'key': 'desc',
                                'name': 'Description',
                            },
                            {
                                'type': 'text',
                                'key': 'standard',
                                'name': 'Standard',
                            },
                            {
                                'type': 'text',
                                'key': 'how_act',
                                'name': 'How to Act',
                            },
                        ],
                        'root_path': 'data.findings.defaultInfo'
                    }
                },
                {
                    'type': 'table',
                    'name': 'Compliance',
                    'options': {
                        'fields': [
                            {
                                'type': 'text',
                                'key': 'name',
                                'name': 'Name'
                            },
                            {
                                'type': 'text',
                                'key': 'type',
                                'name': 'Compliance Type'
                            },
                            {
                                'type': 'list',
                                'key': 'comNum',
                                'name': 'Compliance Number',
                                "options": {
                                            "delimiter": " ",
                                            "item": {
                                                "options": {
                                                    "outline_color": "violet.500"
                                                },
                                                "type": "badge"
                                            }
                                },
                            },
                        ],
                        'root_path': 'data.findings.compliance'
                    }
                },
                {
                    'type': 'table',
                    'name': 'Flag Details',
                    'options': {
                        'fields': [
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
                                'type': 'text',
                                'key': 'region',
                                'name': 'Region'
                            },
                            {
                                'type': 'more',
                                'key': 'id',
                                'name': 'findings',
                                "options": {
                                    "sub_key": "findings", 
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
                            }
                        ],
                        'root_path': 'data.findings.flag'
                    }
                },
                {
                    'type': 'table',
                    'name': 'Secure Details',
                    'options': {
                        'fields': [
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
                                'type': 'text',
                                'key': 'region',
                                'name': 'Region'
                            },
                            {
                                'type': 'more',
                                'key': '',
                                'name': 'findings',
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
                        'root_path': 'data.findings.secure'
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
