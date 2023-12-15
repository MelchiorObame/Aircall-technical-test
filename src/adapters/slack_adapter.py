from adapters import notification_adapter
from models.slack_target  import SlackTarget

class SlackAdapter(notification_adapter):

    def send_notification(self, target : SlackTarget):
        pass
