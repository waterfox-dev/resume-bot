import sqlite3 as sql 
import json

from core.struct.answer import Answer

class AnswerRecorder: 
    
    
    def __init__(self, db_path: str = 'data/dev.sqlite3') -> None :
        
        self.db_path = db_path
        self.conn = sql.connect(self.db_path, timeout=10)
        
    def record(self, answer: Answer) -> int :
        cursor = self.conn.cursor()
        cursor.execute("""INSERT INTO `RB_ANSWER` 
                (ANSWER_ID, ANSWER_JSON_MESSAGES, ANSWER_RESPONSE, ANSWER_DATE, ANSWER_CALLER_ID) 
                VALUES (?, ?, ?, ?, ?)""", 
                (answer['id'], json.dumps(answer['json_messages']), answer['response'], answer['date'],answer['caller_id']))
        self.conn.commit()
        return answer['id']
    
    def add_thumbsup(self, answer_id: int) -> None :
        
        cursor = self.conn.cursor()
        cursor.execute(f"""UPDATE `RB_ANSWER` SET ANSWER_THUMBS_UP = ANSWER_THUMBS_UP + 1 WHERE ANSWER_ID = {answer_id}""")
        self.conn.commit()
        
    def add_thumbsdown(self, answer_id: int) -> None :
            
        cursor = self.conn.cursor()
        cursor.execute(f"""UPDATE `RB_ANSWER` SET ANSWER_THUMBS_UP = ANSWER_THUMBS_UP - 1 WHERE ANSWER_ID = {answer_id}""")
        self.conn.commit()
    
    def get_answer(self, answer_id: int) -> Answer :
        
        cursor = self.conn.cursor()
        cursor.execute(f"""SELECT * FROM `RB_ANSWER` WHERE ANSWER_ID = {answer_id}""")
        row = cursor.fetchone()
        
        answer = Answer()
        answer['id'] = int(row[0])
        answer['json_messages'] = json.loads(row[1])
        answer['response'] = row[2]
        answer['date'] = row[3]
        answer['caller_id'] = int(row[4])
        
        return answer

    def get_thumbsup(self, answer_id: int) -> int :
        
        cursor = self.conn.cursor()
        cursor.execute(f"""SELECT ANSWER_THUMBS_UP FROM `RB_ANSWER` WHERE ANSWER_ID = {answer_id}""")
        row = cursor.fetchone()
        
        return row[0]
    
    def clear(self) -> None :
        
        cursor = self.conn.cursor()
        cursor.execute("""DELETE FROM `RB_ANSWER`""")