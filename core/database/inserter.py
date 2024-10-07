import sqlite3 as sql 


class Inserter: 
    
    
    def __init__(self, db_path: str = 'data/dev.sqlite3') -> None :
        
        self.db_path = db_path
        self.conn = sql.connect(self.db_path)