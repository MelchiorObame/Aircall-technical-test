from adapters import notification_adapter
from models.sms_target import SMSTarget

class SMSAdapter(notification_adapter):

    def send_notification(self, target : SMSTarget):
        pass
