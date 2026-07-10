import json
filePath = 'todoTasks.txt'

class notThere(Exception):
    '''raised when trying to delete something that don't exsist'''
    pass
class noSelection(Exception):
    '''raised when choice not 1, 2, 3'''
    pass

def main():
    todoList = rTodo()
    choice = input('''what would you like to do:\n 
    create task (1)\n
    remove task (2)\n
    mark as completed (3)\n :''')
    try:
        if choice not in ['1','2','3']:
            raise noSelection
            print('please enter either 1 or 2 or 3')
            main()
        if choice == '1':
            task = input('what task would you like to add to todo list: ')
            createTask(task,'not complete')
        elif choice =='2':
            task = input('what task would you like to delete to todo list: ')
            deleteTask(todoList, task)
        elif choice =='3':
            task = input('which task you would like to mark as completed: ')
            markCompleted(task,'complete', todoList)
    except noSelection:
        print('please select 1, 2, or 3')
        main()


def createTask(task, status):
    wTodo(task, 'not complete')
    main()

def deleteTask(todoList, task):
    
    try:
        if task not in todoList:
            raise notThere
        del todoList[task]
        
    except notThere:
        print(f'{task} does not exsist')
    main()

def markCompleted(task, status, todoList):
    
    try:
        if task not in todoList:
            raise notThere
        wTodo(todoList, task)
    except notThere:
        print(f'{task} does not exsist')
    print(todoList)
    main()

def rTodo():
    with open(filePath, 'r') as file:
        todoList = json.load(file)
        print(todoList)
    return todoList
def wTodo(task,status):
    todoList = rTodo()
    taskAS = {task:status}
    newToDo=todoList.append(taskAS)
    print(newToDo)
    print(taskAS)
    with open(filePath, 'w') as file:
        json.dump(taskAS, file)
main()



