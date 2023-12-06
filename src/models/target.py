
from src.utils.utils import NotificationType


class Target:

        def __init__(self,
                type:NotificationType,
                contact:str):
            self.type = type        # 'email' or 'SMS'
            self.contact = contact  # Email address or phone number
