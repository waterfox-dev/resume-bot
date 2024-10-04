from unittest import TestCase 
from unittest import main

from core.struct.message import Message


class MessageTest(TestCase) :
    
    def test_to_json(self) :
        message = Message(id=1, content="content", author="author", date="date")
        
        self.assertEqual(message.to_json(), {
            "id": 1,
            "content": "content",
            "author": "author",
            "date": "date"
        })
        
    def test_to_json_with_empty_message(self) :
        
        message = Message(id=0, content="", author="", date="")
        
        self.assertEqual(message.to_json(), {
            "id": 0,
            "content": "",
            "author": "",
            "date": ""
        })
        
if __name__ == "__main__":
    main()