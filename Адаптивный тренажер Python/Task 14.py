"""
В какой-то момент вам надоело использовать имена файлов с пробелами и вы решили написать программу,
которая переименовывает все файлы, содержащие пробелы в имени, заменив группы пробелов на символ подчёркивания "_".
Для начала нужно написать программу, которая считывает строку и заменяет в ней группы пробельных символов на символ
подчёркивания.
Формат ввода:
Одна строка, содержащая произвольные символы, в том числе и пробельные.
Формат вывода:
Преобразованная строка.
"""


print('_'.join(input().split()))
