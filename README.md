# SkillFactory
Я изучаю язык Питон. ДЕлаю здесь свои домашки.

День 1
Hello.py

import random
import string

def hard_gen_pass(length=33):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    choise = input('Wanna use some digits?(y/n): ')
    if choise == 'y' or choise == 'yes' or choise == 'Y' or choise == 'YES':
        alphabet += '0123456789'
    choise = input('Wanna use some signs?(y/n): ')
    if choise == 'y' or choise == 'yes' or choise == 'Y' or choise == 'YES':
        alphabet += '!@#$%^&*()<>:/?.,'
    password = ''
    for i in range(length):
        password += random.choice(alphabet)
    return password

length = input('How many? -->  ')
if length :
    res = hard_gen_pass(int(length))
else:
    res = hard_gen_pass()
print (res)

"""
1)воспроизвести
2)проверки на введенные данные
3)поиграйтесь и пофантазируйте

Ivan_passgen.py

"""
