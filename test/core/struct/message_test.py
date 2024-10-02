from unittest import TestCase 

from core.struct.message import Message


class MessageTest(TestCase) :
    
    def test_to_json(self) :
        message = Message(id=1, content="content", author="author", send_time="send_time")
        
        self.assertEqual(message.to_json(), {
            "id": 1,
            "content": "content",
            "author": "author",
            "send_time": "send_time"
        })
        
    def test_to_json_with_empty_message(self) :
        
        message = Message(id=0, content="", author="", send_time="")
        
        self.assertEqual(message.to_json(), {
            "id": 0,
            "content": "",
            "author": "",
            "send_time": ""
        })