# Урок 19: Форматирование строк

name = 'Edgar'
age = 29

# %
print('Привет, %s!\nТебе уже %d год!' % (name, age))

# .format()
print('Привет, {}!\nТебе уже {} год!'.format(name, age))


# Заполнение строк

print('{:*^11}'.format(name))