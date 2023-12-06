from src.utils.utils import ServiceState


class Service:

    def __init__(self, id, state= ServiceState.Healthy):
        self.id = id
        self.state = state


    def mark_unhealthy(self):
        self.state = ServiceState.Unhealthy 


    def mark_healthy(self):
        self.state = ServiceState.Healthy 
