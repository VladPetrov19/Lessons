class MyError(ValueError):
   pass

def get_new_password():
    while True:
        try:
            pas = input('Enter password: ')
            if len(pas) < 8:
                raise MyError('NotEnoughLengthError')
            if any(map(str.isdigit, pas)) == False:
                raise MyError('NumbersNotFoundError')
            print(pas)
            break
        except MyError as e:
            print(e)


get_new_password()