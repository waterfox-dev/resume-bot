from enum import Enum 


class PoolStrategy(Enum):
    
    POPFIRST = 1
    POPRANDOM = 2
    POPSMALLET = 3
    POPBIGGEST = 4
    STOP = 5