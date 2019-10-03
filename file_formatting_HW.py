# Урок 19: Форматирование строк, домашка

name = 'Edgar'

str_len = 10
word_len = len(name)

if word_len % 2 == 1:
    str_len -= 1
    print(('{:*^' + str(str_len) + '}').format(name))
else:
    print(('{:*^' + str(str_len) + '}').format(name))