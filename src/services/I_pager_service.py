from abc import ABC, abstractmethod
from src.models.alert import Alert


class IPagerService (ABC):
    
    @abstractmethod
    def on_alert_received(self, alert: Alert) -> None:
        pass


    @abstractmethod
    def on_alert_ack_timeout(self, alert:Alert):
        pass


    @abstractmethod
    def set_healthy_state(self, service_id:str):
        pass


    @abstractmethod
    def on_alert_ack_received(self, alert: Alert):
        pass