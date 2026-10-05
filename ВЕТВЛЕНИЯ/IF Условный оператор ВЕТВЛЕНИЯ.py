n = input ('Введите число: ')
if n[0] == '-':
    n = n[1:]
proverka = n.isdigit()
# print(proverka)
print(n.isdigit())
n = int(n)
# if n < 0:
#     print('Число отрицательное')
# elif n >0:
#     print('Число положительное')
# else:
#     print('Число ноль')

if proverka: #с вложенными условиями
    if n < 0:
        print('Число отрицательное')
    elif n >0:
        print('Число положительное')
    else:
        print('Число ноль')
else:
    print ('Вы ввели не число')