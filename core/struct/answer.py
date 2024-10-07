from typing import TypedDict

from core.struct.message_pool import MessagePool

class Answer(TypedDict) :
    
    id: int
    json_messages: MessagePool
    response: str
    date: str 
    caller_id: int