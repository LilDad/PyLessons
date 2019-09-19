try:
    eval('print(выа)а')

except SyntaxError:
    print("научись писать, ракушка")

print("Exceptions")


# Ex 1
# try:
#     num1 = 7
#     num2 = '0'
#     print(num1 / num2)
#     print("Done calculation")
#
# except ZeroDivisionError:
#     print("An error occurred")
#     print("due to zero division")
#
# except TypeError:
#     print("Type Error")

# Ex 2
# def exc(text):
#     assert text != ''
#     print(str(text) + '!')
# exc('')

# Ex 3
# def test(number):
#     assert number > 0, "Number should be bigger than 0."
#     print(str(number))
#
# test(-10)