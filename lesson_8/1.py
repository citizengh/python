import datetime


class Date:
    date = datetime.date

    def __init__(self, str_date):
        self.date = Date.validate_date(str_date)

    @classmethod
    def from_strdate(cls, str_date):
        try:
            str_list = list(map(int, str_date.split('-')))
            return cls(str_date)
        except ValueError:
            print(f'Неправильные символы в {str_date}')
            return cls(str(datetime.date.today().strftime('%d-%m-%Y')))

    @staticmethod
    def validate_date(str_date):
        try:
            return datetime.datetime.strptime(str_date, '%d-%m-%Y')
        except ValueError:
            print(f'Неправильная дата {str_date}')
            return datetime.date.today()


d = Date.from_strdate('28-02-2022')
print(d.date)
