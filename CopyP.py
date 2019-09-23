#Программа для копирования файлов!

filename1 = input('Введите название копируемого файла: ')
filename2 = input('Введите название нового файла: ')

file1 = open(filename1, 'rb')
file2 = open(filename2, 'wb')

file2.write(file1.read())

file1.close()
file2.close()

print('Копирование успешно завершено!')

new_file_open = input('Открыть новый файл (y/n): ')

if new_file_open == 'y':
    new_file = open(filename2, 'r')
    print(new_file.read())
    new_file.close()
else:
    'Программа завершена...'
