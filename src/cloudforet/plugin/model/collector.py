from cloudforet.plugin.lib.model.plugin_info_model import PluginInfo, PluginMetadata, ResourceType, ScheduleType, \
    Feature

COMPLIANCE_FRAMEWORKS = {
    'aws': {
        'D-CLO Best Practice': 'SET-00011014',
        'CSP 안전성 평가': 'SET-00026104',
        'ISMS': 'SET-00026100',
        'ISO-27001': 'SET-00026108',
        'KISA-CSAP(간편)': 'SET-00026103',
    },
    'google_cloud': {
        'D-CLO Best Practice': 'SET-00011014',
    },
    'azure': {
        'D-CLO Best Practice': 'SET-00011014',
    }
}


class CollectorPluginInfo(PluginInfo):
    metadata: PluginMetadata = {
        'supported_resource_type': [
            ResourceType.cloud_service,
            ResourceType.cloud_service_type
        ],
        'supported_schedules': [
            ScheduleType.hours
        ],
        'supported_features': [
            Feature.garbage_collection
        ],
        'options_schema': {
            'required': ['provider', 'compliance_framework'],
            'order': ['provider', 'compliance_framework'],
            'type': 'object',
            'properties': {
                'provider': {
                    'title': 'Provider',
                    'type': 'string',
                    'default': 'aws',
                    'disabled': True
                },
                'compliance_framework': {
                    'title': 'Compliance Framework',
                    'type': 'string',
                    'enum': list(COMPLIANCE_FRAMEWORKS['aws'].keys()),
                    'default': 'D-CLO Best Practice'
                },
            }
        }
    }
