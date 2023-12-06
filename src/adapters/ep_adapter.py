from abc import ABC, abstractmethod
from models.escalation_policy import EscalationPolicy

class EscalationPolicyAdapter(ABC):

    @abstractmethod
    def get_escalation_policy(self, service_id: str) ->  EscalationPolicy:
        pass

    @abstractmethod
    def get_level_targets(self, service_id: str, level: int) :
        pass
