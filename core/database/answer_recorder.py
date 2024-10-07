import sqlite3 as sql 

from core.struct.answer import Answer

class AnswerRecorder: 
    
    
    def __init__(self, db_path: str = 'data/dev.sqlite3') -> None :
        
        self.db_path = db_path
        self.conn = sql.connect(self.db_path)
        
    def record(self, answer: Answer) -> int :
        
        cursor = self.conn.cursor()
        cursor.execute(f"""INSERT INTO `RB_ANSWER` 
                        (ANSWER_ID, ANSWER_JSON_MESSAGES, ANSWER_REPONSE, ANSWER_CALLER_ID) 
                        VALUES ({answer['id']}, {answer['json_messages']}, {answer['response']}, {answer['caller_id']})""")
        self.conn.commit() 
        return answer['id']
    
    def add_thumbsup(self, answer_id: int) -> None :
        
        cursor = self.conn.cursor()
        cursor.execute(f"""UPDATE `RB_ANSWER` SET ANSWER_THUMBS_UP = ANSWER_THUMBS_UP + 1 WHERE ANSWER_ID = {answer_id}""")
        self.conn.commit()