from unittest import TestCase 
from unittest import main

from core.struct.message_pool import MessagePool
from core.struct.message import Message

from core.enum.pool_strategy import PoolStrategy

class TestMessagePool(TestCase) :

    def test_add_with_pool_size_exceded(self) :
        pool = MessagePool()
        pool.MAX_POOL_SIZE = 3
        pool.STRATEGY = PoolStrategy.STOP
        
        with self.assertRaises(Exception) as context :
            for i in range(4) :
                pool.add(Message(id=i, content="content", author="author", date="date"))
        
        self.assertTrue("Stop strategy is enabled. Pool size exceded." in str(context.exception))
        
    def test_add_with_popfirst_strategy(self) :
        pool = MessagePool()
        pool.MAX_POOL_SIZE = 3
        pool.STRATEGY = PoolStrategy.POPFIRST
        
        for i in range(4) :
            pool.add(Message(id=i, content="content", author="author", date="date"))
        
        self.assertEqual(len(pool), 3)
        self.assertEqual(pool[0].id, 1)
        self.assertEqual(pool[1].id, 2)
        self.assertEqual(pool[2].id, 3)
    
    def test_add_with_poprandom_strategy(self) :
        pool = MessagePool()
        pool.MAX_POOL_SIZE = 3
        pool.STRATEGY = PoolStrategy.POPRANDOM
        
        for i in range(4) :
            pool.add(Message(id=i, content="content", author="author", date="date"))
        
        self.assertEqual(len(pool), 3)
        
    def test_add_with_popsmallet_strategy(self) :
        pool = MessagePool()
        pool.MAX_POOL_SIZE = 3
        pool.STRATEGY = PoolStrategy.POPSMALLET
        
        for i in range(4) :
            pool.add(Message(id=i, content=("content"*i), author="author", date="date"))
        
        self.assertEqual(len(pool), 3)
        self.assertEqual(pool[0].id, 1)
        self.assertEqual(pool[1].id, 2)
        self.assertEqual(pool[2].id, 3)
        
    def test_add_with_popbiggest_strategy(self) :
        
        pool = MessagePool()
        pool.MAX_POOL_SIZE = 3
        pool.STRATEGY = PoolStrategy.POPBIGGEST
        
        for i in range(4) :
            pool.add(Message(id=i, content=("content"*i), author="author", date="date"))
        
        self.assertEqual(len(pool), 3)
        self.assertEqual(pool[0].id, 0)
        self.assertEqual(pool[1].id, 1)
        self.assertEqual(pool[2].id, 3)
        
if __name__ == "__main__":
    main()