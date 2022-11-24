myToDoList = []

validActions = ['add', 'delete']

def print_to_do_list(to_do_list):
    if len(to_do_list) == 0:
        print('There are no items in the to do list')
        return

    print('Your To Do List:')
    for index, toDoItem in enumerate(to_do_list):
        print(f'{index} . {toDoItem}')

while True:
    print_to_do_list(myToDoList)

    action = ''

    while action not in validActions:
        action = input('What action would you like to do? ("add", "delete")')

    if action == 'add':
        newToDoItem = input('What do you want to add to your To Do List?: ')
        myToDoList.append(newToDoItem)
    elif action == 'delete':
        index = int(input('What item do you want to delete?'))
        myToDoList.pop(index)


