FILEPATH = 'files/todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        return file_local.readlines()


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# just for testing purposes when I want run directly from this file, if i run from main.py it will nto be execuret
# __main__ means that I run code from this file
if __name__ == "__main__":
    print("test")
    print(get_todos())