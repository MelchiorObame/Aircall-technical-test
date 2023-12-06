from abc import ABC, abstractmethod
from models.alert import Alert

from models.service import Service


class PersistenceAdapter(ABC):
    
    @abstractmethod
    def findServiceById(self, service_id:str)-> Service:
        pass
    
    
    @abstractmethod
    def saveAlert(self, alert: Alert):
        pass
    
    
    @abstractmethod
    def updateMonitoredService(self, service:Service):
        pass