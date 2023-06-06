# from functions import get_todos, write_todos
from modules import functions
import time

# now = time.strftime("%b %d, %Y %H:%M:%S")

user_prompt = "Type add, show, edit, complete, or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos_arg=todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        # list comprehension
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a  new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos_arg=todos)

        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos_arg=todos)

            message = f"ToDo {todo_to_remove} was remove form the list."
            print(message)

        except IndexError:
            print('There is no item with that number.')
            continue

    elif user_action.startswith('exit'):
        print("bye")
        break
    else:
        print('Command is not valid')

