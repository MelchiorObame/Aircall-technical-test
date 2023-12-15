import unittest
from unittest.mock import patch
from src.models.email_target import EmailTarget
from src.models.service import Service
from src.models.alert import Alert
from src.models.sms_target import SMSTarget
from src.models.slack_target import SlackTarget
from src.models.target import Target
from src.models.escalation_policy import EscalationPolicy
from src.services.pager_service import PagerService
from src.utils.utils import  ServiceState

class TestPagerService(unittest.TestCase):

    def setUp(self):
        self.pager_service = PagerService()
        self.service = Service('service_1', ServiceState.Healthy)
        self.pager_service.register_service(self.service)
        
        ep = EscalationPolicy('service_1')
        
        # Création d'un dictionnaire avec des niveaux et des ensembles de cibles
        levels: dict[int, set[Target]] = {
            1: {EmailTarget("email1@example.com"), SMSTarget("1234567890"), SlackTarget("randomChanelID")},
            2: {EmailTarget("email2@example.com"), SMSTarget("0987654321"), SlackTarget("randomChanelID")},
            3: {EmailTarget("email3@example.com"), SMSTarget("1122334455")},
            4: {EmailTarget("email4@example.com"), SMSTarget("5566778899"), SlackTarget("randomChanelID")}
        }
        ep = EscalationPolicy('service_1',levels )
        self.pager_service.register_policy(ep)




    @patch('src.services.pager_service.PagerService.notify_targets')
    @patch('src.services.pager_service.PagerService.set_acknowledgement_timer')
    def test_healthy_service_receives_alert(self, mock_set_timer, mock_notify_targets):
        alert = Alert('service_1', 'problème on this service!')
        self.pager_service.on_alert_received(alert)
        self.assertEqual(self.service.state, ServiceState.Unhealthy)
        mock_notify_targets.assert_called_once_with('service_1', 1)
        mock_set_timer.assert_called_once_with('service_1', 15 * 60)


    @patch('src.services.pager_service.PagerService.notify_targets')
    @patch('src.services.pager_service.PagerService.set_acknowledgement_timer')
    def test_unhealthy_service_acknowledgement_timeout(self, mock_set_timer, mock_notify_targets):
        self.service.mark_unhealthy()
        alert = Alert('service_1', 'problème persistant!')
        self.pager_service.on_alert_ack_timeout(alert)
        mock_notify_targets.assert_called_once_with('service_1', 2)
        mock_set_timer.assert_called_once_with('service_1', 15 * 60)


    @patch('src.services.pager_service.PagerService.notify_targets')
    def test_unhealthy_service_receives_acknowledgement(self, mock_notify_targets):
        self.service.mark_unhealthy()
        alert = Alert('service_1', 'problème résolu!')
        self.pager_service.on_alert_ack_received(alert)
        mock_notify_targets.assert_not_called()


    @patch('src.services.pager_service.PagerService.notify_targets')
    def test_unhealthy_service_receives_alert(self, mock_notify_targets):
        self.service.mark_unhealthy()
        alert = Alert('service_1', 'nouveau problème!')
        self.pager_service.on_alert_received(alert)
        mock_notify_targets.assert_not_called()
        

    @patch('src.services.pager_service.PagerService.notify_targets')
    def test_unhealthy_service_becomes_healthy(self, mock_notify_targets):
        self.service.mark_unhealthy()
        self.pager_service.set_healthy_state('service_1')
        alert = Alert('service_1', 'service rétabli!')
        self.pager_service.on_alert_ack_timeout(alert)
        self.assertEqual(self.service.state, ServiceState.Healthy)
        mock_notify_targets.assert_not_called()



if __name__ == '__main__':
    unittest.main()
