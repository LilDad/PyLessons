filename1 = input('Введите имя копируемого файла: ')

file1 = open(filename1, 'rb')
file2 = open('backup_' + filename1, 'wb')

file2.write(file1.read())

file1.close()
file2.close()

print('Бэкап произведен успешно!')