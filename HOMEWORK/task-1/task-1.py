import random
from string import printable

RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m'

while True:
    try:
        length = int(input('Введите желаемую длинну пароля: '))
        password = ''
        if length >= 0:
            for i in range(length):
              password += random.choice(printable[:62])     
            print(GREEN + password + RESET)   
            break    
        else:
            print(RED + 'Ну как я тебе отрицательную длинну выведу!?' + RESET)
                        
    except:
         print(RED + 'Требуется ввести число!!!' + RESET)
         
    