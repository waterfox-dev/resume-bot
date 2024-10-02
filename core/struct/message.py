from dataclasses import dataclass, asdict

@dataclass
class Message:
    """Represents a minimalist message object.
    
    Attributes:
    id: int -- the message's unique id
    content: str -- the content of the message
    author: str -- the author of the message
    send_time: str -- the time the message was sent
    """
    id: int
    content: str
    author: str 
    date: str
    
    def to_json(self) -> dict:
        """Converts the message to a json object.
        
        Returns:
        dict -- the message as a json object
        """
        return asdict(self)
