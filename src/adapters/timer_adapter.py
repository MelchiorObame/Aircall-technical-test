from abc import ABC, abstractmethod


class TimerAdapter(ABC):

    @abstractmethod
    def set_timer(self,service_id:str,  seconds:int):
        pass