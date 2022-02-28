class IsNotDigitEx(Exception):
    def __init__(self, message):
        self.message = message

    @staticmethod
    def check(elem):
        try:
            return float(elem.replace(',','.'))
        except ValueError:
            raise IsNotDigitEx(f'"{elem}" не является числом!')


inp = ''
mylist = []
while inp.lower() != 'stop':
    try:
        inp = input('Введите число: ')
        mylist.append(IsNotDigitEx.check(inp))
    except IsNotDigitEx as err:
        print(err.message)

print(mylist)
