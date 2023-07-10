# Python Quiz Coding Challenge

## Weeks II & III

### Instructions
1. Fork and clone this repository.
2. Familiarize yourself with the file structure of this repository.
3. Achieve the following objectives by carefully reading what is being asked and executing.

### Objectives

You are given a file named `users.txt`. Your goal is to validate that each user's username is unique.

# Problem: Name checker
Create a function called `validate_file()` (in `name_checker.py`) which accepts a name of a file to validate. This function validates the [users.txt](users.txt) file and **checks that the first name for each user does not contain any numbers (0123456789)**. This function raises (throws) a `ValidationException` object and is consumed in the following manner:

Test Case:
```python
def test():
    try:
        validate_file("users.txt")
    except ValidationException as ve:
        print(ve)

test()
```

Output:
```
Invalid mileage:  32.13
```

- This tests your ability to read files, select the correct data, manipulate strings and use Exceptions in python.

**GLHF :)**
