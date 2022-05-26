"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def sum(items_sold):
    sum_items_sold = 0
    for item_sold in items_sold:
        sum_items_sold += item_sold
    return sum_items_sold

sum_items_sold = 0

for one_phone in phones:
    sum_phone = sum(one_phone['items_sold'])
    print(f'Суммарное количество продаж {one_phone["product"]}: {sum_phone}') 

sum_items_sold += sum_phone

print(f'Суммарное количество продаж всех товаров {sum_items_sold * len(phones)}')

def avg(items_sold):
    sum_items_sold = 0
    for item_sold in items_sold:
        sum_items_sold += item_sold
    return sum_items_sold / len(items_sold)

avg_items_sold = 0

for one_phone in phones:
    phone_avg = round(avg(one_phone['items_sold']), 1)
    print(f'Среднее количество продаж {one_phone["product"]}: {phone_avg}')    

avg_items_sold += phone_avg
avg_sold = round(avg_items_sold / len(phones), 1)

print(f'Среднее количество продаж всех товаров {avg_sold}')