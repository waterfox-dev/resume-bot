from core.enum.pool_strategy import PoolStrategy

from core.struct.exceptions.pool_size_exceded import PoolSizeExceded

from core.struct.message import Message

import random 


class MessagePool(list) :
    
    MAX_POOL_SIZE = 100
    STRATEGY = PoolStrategy.POPSMALLET 
    
    def __init__(self) :
        list.__init__(self)
    
    def add(self, message: Message) :
        """Adds a message to the pool.
        
        Arguments:
        message -- the message to add
        """
        if len(self) >= self.MAX_POOL_SIZE :
            match self.STRATEGY :
                case PoolStrategy.POPFIRST :
                    self.pop(0)
                case PoolStrategy.POPRANDOM :
                    self.pop(random.randint(0, len(self) - 1))
                case PoolStrategy.POPSMALLET :
                    self.pop(self.index(min(self, key=lambda x: len(x.content))))
                case PoolStrategy.POPBIGGEST :
                    self.pop(self.index(max(self, key=lambda x: len(x.content))))
                case PoolStrategy.STOP :
                    raise PoolSizeExceded("Stop strategy is enabled. Pool size exceded.")
        
        self.append(message)
        
    def get(self) :
        """Gets the pool.
        
        Returns:
        list -- the pool
        """
        return self
    
    def get_size(self) :
        """Gets the size of the pool.
        
        Returns:
        int -- the size of the pool
        """
        return len(self)
    
    def to_json(self) :
        """Converts the pool to a json object.
        
        Returns:
        dict -- the pool as a json object
        """
        return [message.to_json() for message in self]