def pers_data_print(name, surname, city, birthday, email, phone):
    print(f'{name} {surname}, born {birthday} in {city}, tel:{phone}, email:{email}')


pers_data_print(phone='100', birthday='01.01.2002', email='test@gmail.ru', name='Andrey', surname='Smith',
                city='London')
