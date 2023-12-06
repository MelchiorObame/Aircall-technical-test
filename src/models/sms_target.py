from src.models.target import Target
from src.utils.utils import NotificationType


class SMSTarget(Target):
    def __init__(self, contact: str):
        super().__init__(NotificationType.SMS, contact)