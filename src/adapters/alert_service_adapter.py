from abc import ABC, abstractmethod
from models.escalation_policy import EscalationPolicy

class AlertServiceAdapter(ABC):

    @abstractmethod
    def on_alert_received(self):
        pass


