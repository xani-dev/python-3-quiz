from ValidationException import ValidationException

def validate_file(file_path):
    print('Hi, Opening the file: ', file_path)
    
    with open(file_path, 'r') as file_to_validate:
        for line_number, line in enumerate(file_to_validate, start = 1):
            if line_number == 1:
                continue
            first_name = line.partition(',')[0]
            

            
            try: 
               if first_name.isalpha():
                   continue
               else:
                    print('Invalid First Name:',first_name)
            except ValueError:
                raise ValidationException(f'Invalid Name: {first_name}')
            
            

def test():
    try:
        validate_file("users.txt")
    except ValidationException as ve:
        print(ve)

test()
