class Alert:

    def __init__(self, service_id:str,
                message:str,
                Acknowledged:bool=False,
                level:int=1):
        """_summary_
        Args:
            service_id (str): _description_
            message (str): _description_
            Acknowledged (bool): _description_
            level (_type_, optional): current level of the alert based on EP. Defaults to 1.
        """
        self.service_id = service_id
        self.message = message
        self.Acknowledged = Acknowledged
        self.level = level


    def increment_level(self) -> None:
        self.level +=1
    
    def setLevel(self, value:int)->None:
        self.level = value
    
    def setAcknowledged(self, value) ->None : 
        self.Acknowledged = value

        
        
        
