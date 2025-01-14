"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = int(input('Введите ваш возраст: '))
    if age <= 6:
        print('учится в детском саду')
    elif age <= 17:
        print('учится в школе')
    elif age <= 24:
        print('учится в ВУЗе')
    else:
        print('работающий')

if __name__ == "__main__":
    main()
