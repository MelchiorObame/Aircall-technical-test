from enum import Enum

class ServiceState(Enum):
    Unhealthy = 'Unhealthy'
    Healthy = 'Healthy'
    
    
class NotificationType(Enum):
    SMS = 'SMS'
    EMAIL = 'EMAIL'


