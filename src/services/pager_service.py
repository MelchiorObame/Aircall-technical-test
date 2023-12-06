import logging
from src.models.alert import Alert
from src.models.escalation_policy import EscalationPolicy
from src.models.service import Service
from src.models.target import Target
from src.utils.utils import NotificationType, ServiceState

class PagerService:
    def __init__(self):
        self.services = {}  # {service_id: Service}
        self.policies = {}  # {service_id: EscalationPolicy}
        self.logger = logging.getLogger(self.__class__.__name__)

    def register_service(self, service: Service):
        self.services[service.id] = service

    def register_policy(self, ep: EscalationPolicy):
        self.policies[ep.service_id] = ep

    
    def on_alert_received(self, alert: Alert) -> None:
        service = self.services.get(alert.service_id)
        if service and service.state == ServiceState.Healthy:
            service.mark_unhealthy()
            self.notify_targets(service.id, 1)  # Assuming level 1 for first notification
            self.set_acknowledgement_timer(service.id, 15 * 60)



    def set_acknowledgement_timer(self, service_id:str, timeout):
        self.logger.info(f"service {service_id}, timeout = {timeout} seconds")
        pass
    
    

    def notify_targets(self, service_id: str, escalation_level: int): 
        escalation_policy = self.policies.get(service_id)
        if not escalation_policy:
            self.logger.error(f"No escalation policy found for {service_id}")
            return

        targets = escalation_policy.get_targets_by_level(escalation_level)
        for target in targets:
            if target.type == NotificationType.SMS:
                # self.sms_adapter.send_notification(target)
                pass  # Simulate SMS notification
            elif target.type == NotificationType.EMAIL:
                # self.email_adapter.send_notification(target)
                pass  # Simulate email notification
            else:
                self.logger.error("Unsupported notification type")


    #------------ scenarios 


    def on_alert_ack_timeout(self, alert:Alert):
        service = self.services.get(alert.service_id)
        if service.state == ServiceState.Unhealthy and not alert.Acknowledged:
            alert.increment_level()
            self.notify_targets(service.id, alert.level)
            self.set_acknowledgement_timer(service.id, 15 * 60)


    def set_healthy_state(self, service_id:str):
        service = self.services.get(service_id)
        if service.state == ServiceState.Unhealthy:
            service.mark_healthy()


    def on_alert_ack_received(self, alert: Alert):
        service = self.services.get(alert.service_id)
        if service.state == ServiceState.Unhealthy and alert.Acknowledged:
            self.persistence_adapter.save_alert(alert)
