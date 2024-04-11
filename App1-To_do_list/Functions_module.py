# Defining a Constant
FILEPATH = r"C:\Users\Rutuja Bhagane\PycharmProjects\Projects\App1-To_do_list\todofile.txt"
def read_file(filepath=FILEPATH):
    """ This is a doc string
    This is use to describe what the function does
    This Function to read the file

    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


# Function to write the file

def write_to_file(todo_agrs, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todo_agrs)


# print("Hello you are importing from a file")
if __name__ == "__main__":
    print("Hello you are importing from a file")
