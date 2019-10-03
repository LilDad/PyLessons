# Урок 20: Ф-и для работы сос троками и числами

fruits = ['Лимоны', 'Яблоки', 'Киви', 'Ананас', 'Клубюника']
members = 'James,Jonny,Jassie,Jack,John'

# join, replace, startswith, endswith, lower, upper, split, min, max, abs, sum

# join - вставляют элемент при выводе
print( ', '.join(fruits))

# replace - заменяет
print( 'Привет, Пётр!'.replace('Пётр', 'Александр'))

# startswith - определяет первый символ

name = input('Enter your name: ')

if name.endswith('E'):
    print('Ooooh, yaaa maaan!')
else:
    print('Whaaat?')