"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user(user_say):
    """
    Замените pass на ваш код
    """
    try:
      while user_say != 'Хорошо':
        user_say = input('Как дела? ')
    except KeyboardInterrupt:
        print('Пока!')
    
if __name__ == "__main__":
    hello_user(input('Как дела? '))
