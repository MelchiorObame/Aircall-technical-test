from adapters import notification_adapter
from models.email_target import EmailTarget

class EmailAdapter(notification_adapter):

    def send_notification(self, target : EmailTarget ):
        pass