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
            firstName TEXT,
            lastName TEXT,
            email TEXT,
            wantToGoToComp BOOL,
            classStanding TEXT,
            expectedGrad TEXT,
            agab TEXT
        )""")
    
    def add_user(self, db_connection:sqlite3.Connection, user: User) -> None:
        db_connection.execute(
            'INSERT INTO Users Values (?,?,?,?,?,?,?,?)', 
            (user.ID, user.fname, user.lname, user.email, user.want_to_go_to_comp, user.class_status, 
             user.expected_grad, user.agab,))
    
    def turn_db_row_into_user(self, row: tuple):
        return User(row[0], row[1], row[2], row[4], row[5], row[7], row[6], row[3])
        
    def get_user_by_ID(self, db_connection: sqlite3.Connection, ID:int) -> tuple[str, User|None]:
        data = db_connection.execute("SELECT * FROM Users WHERE id==?", (ID,)).fetchone()
        if data:
            return ('success', self.turn_db_row_into_user(data))
        else:
            return (f'Unknown ID {ID}', None)
        
    def get_all_users(self, db_connection: sqlite3.Connection) -> list[User]:
        users = []
        for row in db_connection.execute("SELECT * FROM Users"):
            users.append(self.turn_db_row_into_user(row))
        return users

if __name__ == "__main__":
    DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'data/testDatabase.sqlite3')
    users = Users()
    
    testUser = User(800000000, "philip", "smith", True, "sophmore", "Male", "Spring 2025", "psmit145@uncc.edu")
    testUser2 = User(800000001, "Tano", "edwards", True, "junior", "Male", "2025", "testemail@gmail.com")
    with sqlite3.connect(DEFAULT_PATH) as connection:
        try: 
            users.create_table(connection)
        except sqlite3.OperationalError:
            connection.execute("DROP TABLE users")
            users.create_table(connection)
        users.add_user(connection, testUser)
        users.add_user(connection, testUser2)
        print(users.get_user_by_ID(connection, 800000000))
        print(users.get_all_users(connection))