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
                'key': 'data.resource',
                'name': 'Resource',
            },
            {
                'key': 'data.name',
                'name': 'Name'
            },
            {
                'key': 'data.report_lv',
                'name': 'Report Lv',
                'enums': [
                    'High',
                    'Medium',
                    'Low',
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
                        {
                            'type': 'text',
                            'key': 'data.code',
                            'name': 'Code'
                        },
                        {
                            'type': 'text',
                            'key': 'data.resource',
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
                            'name': 'Report Lv',
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
                            'key': 'data.status',
                            'name': 'Weak State'
                        },
                        {
                            'type': 'text',
                            'key': 'data.weakState',
                            'name': 'Weak State'
                        }
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
                'name': 'Good Count',
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
            # {
            #     'name': 'Total Score',
            #     'type': 'summary',
            #     'options': {
            #         'value_options': {
            #             'key': 'value',
            #             'options': {
            #                 'default': 0
            #             }
            #         }
            #     },
            #     'query': {
            #         'aggregate': [
            #             {
            #                 'count': {
            #                     'name': 'value'
            #                 }
            #             }
            #         ],
            #         'filter': []
            #     }
            # },
        ],
        'sub_data': {
            'layouts': [
                {
                    'type': 'item',
                    'name': 'Details',
                    'options': {
                        'fields': [
                            # {
                            #     'type': 'text',
                            #     'key': 'code',
                            #     'name': 'Code'
                            # },
                            # {
                            #     'type': 'text',
                            #     'key': 'name',
                            #     'name': 'name',
                            # },
                            # {
                            #     'type': 'text',
                            #     'key': 'report_lv',
                            #     'name': 'Report Lv',
                            # },
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
                                'name': 'Compliance Number'
                            },
                        ],
                        'root_path': 'data.findings.compliance'
                    }
                }
                # reason 탭?
                # JSON 탭
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
