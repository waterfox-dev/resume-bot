from unittest import TestCase

from core.database.answer_recorder import AnswerRecorder
from core.struct.answer import Answer


class AnswerRecorderTest(TestCase):

    def setUp(self) -> None:
        
        self.answer = Answer()
        self.answer['id'] = 1
        self.answer['json_messages'] = '[{"id": 1, "content": "Hello", "author": "Alice", "date": "2022-01-01"}]'
        self.answer['response'] = "Hello Alice"
        self.answer['caller_id'] = 1
        self.answer['date'] = "2022-01-01"
        
        self.answer_recorder = AnswerRecorder('data/mock.sqlite3')
        self.answer_recorder.clear()
        
        return super().setUp()
    
    def test_record(self):
        self.assertEqual(self.answer_recorder.record(self.answer), 1)
    
    def test_add_thumbsup(self):
        self.answer_recorder.record(self.answer)
        self.answer_recorder.add_thumbsup(1)
        self.assertEqual(self.answer_recorder.get_thumbsup(1), 1)
    
    def test_add_thumbsdown(self):
        self.answer_recorder.record(self.answer)
        self.answer_recorder.add_thumbsdown(1)
        self.assertEqual(self.answer_recorder.get_thumbsup(1), -1)
        
    def test_get_answer(self):
        self.answer_recorder.record(self.answer)
        self.assertEqual(self.answer_recorder.get_answer(1), self.answer)
    