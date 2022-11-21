myToDoList = []

validActions = ['add', 'delete']

while True:
    print('Your To Do List:')

    for index, toDoItem in enumerate(myToDoList):
        print(f'{index} . {toDoItem}')
    action = ''

    while action not in validActions:
        action = input('What action would you like to do? ("add", "delete")')

    if action == 'add':
        newToDoItem = input('What do you want to add to your To Do List?: ')
        myToDoList.append(newToDoItem)
    elif action == 'delete':
        index = int(input('What item do you want to delete?'))
        myToDoList.pop(index)


