import json
from datetime import datetime

filePath = 'tasks.json'

class taskNotFound(Exception):
    ''' error thrown when trying remove task that does not exsist'''
    print('task not found')

def loadTasks():
    '''loads task list'''
    with open(filePath, 'r') as file:
        return json.load(file)
    
def saveTasks(tasks):
    with open(filePath, 'w') as file:
        json.dump(tasks, file, indent=4)

def addTask(title, description=''):
    tasks = loadTasks()

    taskId = max([t['id'] for t in tasks], default=0) +1

    new_task = {
        "id": taskId,
        "title": title,
        "description": description,
        "create date": datetime.now().strftime("%Y-%m-%d"),
        "status": "not completed"
    }

    tasks.append(new_task)
    saveTasks(tasks)
    main()
def removeTask(taskId):
    tasks = loadTasks()
    updatedTask = [t for t in tasks if t['id']!=taskId]
    if len(tasks)==len(updatedTask):
        print('please enter task id that is present')
    saveTasks(updatedTask)
    main()
def markCompleted(taskId):
    tasks = loadTasks()
    taskFound=False
    
    for t in tasks:
        if t['id']==taskId:
            t['status']='Completed'
            taskFound = True
            break
    if not taskFound:
        raise taskNotFound
    saveTasks(tasks)
    main()

def main():
    choice = input('what would you like to do \n' \
    '1 for adding task \n 2 for removing task \n ' \
    '3 for marking as complete: ')

    if choice == '1':
        try:
            title, description = input('give title and description separted by space ').split()
            addTask(title, description)
        except:
            print('please enter title of task followed by descripion')
            main()
    elif choice == '2':
        print(loadTasks())
        taskId = int(input('give task id of task you want to remove '))
        removeTask(taskId)
    elif choice == '3':
        print(loadTasks())
        taskId = int(input('give task id of task you want to mark as completed '))
        markCompleted(taskId)
    
main()