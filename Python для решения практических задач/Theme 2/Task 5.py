"""
Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно, составив справочник продуктов с
указанием калорийности на 100 грамм, а также содержание белков, жиров и углеводов на 100 грамм продукта.
Ему не удалось найти всю информацию, поэтому некоторые ячейки остались незаполненными
(можно считать их значение равным нулю). Также он использовал какой-то странный офисный пакет и разделял целую и дробную
часть чисел запятой. Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx

Вася составил раскладку по продуктам на весь поход (она на листе "Раскладка") с указанием номера дня, названия продукта
и его количества в граммах. Для каждого дня посчитайте 4 числа: суммарную калорийность и граммы белков, жиров и
углеводов. Числа округлите до целых вниз и введите через пробел. Информация о каждом дне должна выводиться в отдельной
строке.
"""


import xlrd
import math

read_file = xlrd.open_workbook('tab_for_task_5.xlsx')
sheet = read_file.sheet_by_index(1)

product = {}
for row in range(1, sheet.nrows):
    value = sheet.row_values(row)
    product[int(value[0])] = (value[1], value[2] * 2) if int(value[0]) in product.keys() else (value[1], value[2])

sheet = read_file.sheet_by_index(0)
result = {}

for row in range(1, sheet.nrows):
    value_p = sheet.row_values(row)
    result[value_p[0]] = [value_p[1], value_p[2], value_p[3], value_p[4]]

res = {key: [0, 0, 0, 0] for key in product.keys()}

print(res)
for key, value in product.items():
    for i in range(len(result[value[0]])):
        res[key][i] += result[value[0]][i] * (value[1] / 100) if result[value[0]][i] != '' else 0

print(res)
