from __future__ import annotations
import sqlite3
import os
import dataclasses

SCHEMA_VERSION = 1

@dataclasses.dataclass()
class User:
    ID: int
    fname: str
    lname: str
    want_to_go_to_comp: bool
    class_status: str
    agab: str
    expected_grad: str
    email: str
    
    def get_name(self) -> str:
        return f"{self.fname} {self.lname}"
    

class Users:
    def __init__(self) -> None:
        self.SCHEMA_VERSION = SCHEMA_VERSION
    
    def create_table(self, db_connection: sqlite3.Connection) -> None:
        db_connection.execute("""
        CREATE TABLE Users(
            id INTEGER PRIMARY KEY,
            displayName TEXT,
            firstName TEXT,
            lastName TEXT,
            email TEXT,
            wantToGoToComp BOOL,
            classStanding TEXT,
            expectedGrad TEXT,
            agab TEXT
        )""")
        
    
    
        
        
    

if __name__ == "__main__":
    DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'data/testDatabase.sqlite3')
    
    