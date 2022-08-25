#Загружаем необходимые модули
import random
import string

# Вспомогательная class Hard_gen_pass
# input     int length
# return    str
class Hard_gen_pass:
    
    def __init__(self, length: int = 33):
        self.length = length

    def gen(self):
        # Список слов Да
        yes = {'y', 'yes', 'Y', 'YES', 'Yes', 'д', 'да', 'Д', 'Да', 'ДА'}
        alphabet = string.ascii_letters
        choise = input('Хотите использовать цыфры в пароле?(да/нет): ')
        if choise in yes:
            alphabet += string.digits
        choise = input('Хотите использовать служебные знаки?(да/нет): ')
        if choise in yes:
            alphabet += string.punctuation
        password = ''
        for i in range(length):
            password += random.choice(alphabet)
        return 'Лови пароль: ' + password

# Начало самой программы
#Что делает программа?     
print('Эта программа создает уникальный пароль')

# Бесконечный цикл. Запрос длины пароля
while True:
    length = input('Длина пароля в знаках? -->  ')
    if length.isdigit():
        length = int(length)

        if length >= 4 and length <= 100:
            break
        else:
            print('Разумно составить пароль из символов (мин 4, макс 100)')
    else:
        print('Некорректный ввод. Напишите число, а не строку!')

# Загружаем класс
res = Hard_gen_pass(length)
print (res.gen())

