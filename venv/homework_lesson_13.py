class MyError(ValueError):
   pass

def get_new_password():
    while True:
        try:
            pas = input('Enter password: ')
            pas_r = input('Repeat password: ')
            if len(pas) < 8:
                raise MyError('NotEnoughLengthError')
            if any(map(str.isdigit, pas)) == False:
                raise MyError('NumbersNotFoundError')
            if pas != pas_r:
                raise MyError('PasswordNotMatchError')

            print(pas)
            break
        except MyError as e:
            print(e)


get_new_password()


