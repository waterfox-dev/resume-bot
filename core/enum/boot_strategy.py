from enum import Enum


class BootStrategy(Enum):
    
    FAILED = 1
    FAILED_SILENTLY = 2
    SEND_EXCEPTION = 3