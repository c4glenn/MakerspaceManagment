import sqlite3
import os
import dataclasses

@dataclasses.dataclass()
class User:
    ID: int
    fname: str
    lname: str
    want_to_go_to_comp: bool
    class_status: str
    agab: str
    expected_grad: int
    email: str
    attendance_num: int
    volunteer_num: float
    
    def calc_travel_score(self, volunteer_cutoff: float) -> float:
        volunteer = min(self.volunteer_num, volunteer_cutoff)
        vterm = (10*volunteer)/(volunteer + 10)
        return (vterm/7)*self.attendance_num + (self.attendance_num / 2)
    
    def get_name(self) -> str:
        return f"{self.fname} {self.lname}"
    

class Users:
    pass
    

if __name__ == "__main__":
    DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'data/testDatabase.sqlite3')
    
    