from datetime import datetime
from dataclasses import dataclass, field
from uuid import uuid4, UUID
import itertools

class NotFoundError(Exception):
    '''this error gets raised when task not found'''
    pass


@dataclass
class Task:
    id:int
    title:str
    description:str=''
    status:bool=False
    date: datetime = field(default_factory=datetime.today)

    def mark_completed(self)->None:
        self.status = True

class Task_Manager:

    _id_counter = itertools.count(1)

    def __init__(self):
        self.tasks: list[Task] = []

    def list_tasks(self)->list[Task]:
        return self.tasks

    def add_task(self,title:str, description:str = '')->None:
        task_id = next(self._id_counter)
        task = Task(task_id, title, description)
        self.tasks.append(task)
        


    def remove_task(self, task_id:int)->None:
        is_found = False
        try:
            for i in self.tasks:
                if i.id == task_id:
                    self.tasks.remove(i)
        except:
            pass
            
        
            

    def get_task(self, task_id:int)->Task:
        is_found = False
        try:
            for i in self.tasks:
                if i.id==task_id:
                    is_found = True
                    print(is_found)
                    
                    return i
                    
            
            if not is_found:
                
                raise NotFoundError('task not found')
            
            
        except NotFoundError as e:
            print(str(e))
        except Exception as e:
            print(str(e))

def main():
    t_m = Task_Manager()
    t_m.add_task('gym', 'chest')
    t_m.add_task('work')
    print('testing get')
    t_m.get_task(5)
    t_m.remove_task(1)
    print('testing list and remove')
    print(t_m.list_tasks())
    
    

main()

