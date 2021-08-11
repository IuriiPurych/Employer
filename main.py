# Задание 3
# Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год поступления на работу.
# Конструктор должен генерировать исключение, если заданы неправильные данные. Введите список работников с клавиатуры.
# Выведите всех сотрудников, которые были приняты после заданного года.

class Employer:
    def __init__(self, f_name, s_name, depart, hired_year):
        self.firs_name = f_name
        self.second_name = s_name
        self.department = depart
        try:
            self.year = int(hired_year)
        except ValueError:
            print('Year have to be integer.')
            raise SystemExit

    def __str__(self):
        return f'The employer: {self.firs_name}, {self.second_name} - hired {self.year} in the {self.department}'


employers = []
for i in range(1, 4):
    print('Input', i, 'employer:')
    first_name = input('Input first name:')
    second_name = input('Input second name:')
    department = input('Input department:')
    year = input('Input hired year:')
    employers.append(Employer(first_name, second_name, department, year))

while True:
    try:
        y = int(input('Input year:'))
        break
    except ValueError as e:
        print('Year must be integer.')

for emp in employers:
    if emp.year >= y:
        print(emp)
