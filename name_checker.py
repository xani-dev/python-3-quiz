from ValidationException import ValidationException

def validate_file(file_path):
    pass #TODO: Only add code inside this function.


def test():
    try:
        validate_file("users.txt")
    except ValidationException as ve:
        print(ve)

test()
