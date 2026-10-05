s = 'Здравствуйте, гости!'
# print(s[0])
# print(s[6])
# print(s[-1])
# print(len(s))
# print(s[::1])
# print(s[:12])
# print(s[::-1])
# for i in s:
#     print(i, end=' ')
# print(s[19])
# for i in range(len(s)):
#     print(s[i], end='  ')

print(s.index(','))
print(s.isalpha())
s1 = '12345'

print(s1.isdigit())
print(s1.islower())
print(s1.isupper())
print(s.startswith('3'))
print(s.endswith('!'))
print('res', 'и!' in s)

"""Строковые типы данных/методы строк"""
s = '    ЗдрАвстВуйте, гости!'
print(n := s.lower()) # текст снизу
print(s.upper()) #текст сверху
print(s.title()) #все слова начинаются с Большой Буквы
print(s.capitalize()) #ПЕРЕМЕННАЯ начинается с Большой буквы
print(s.rjust(40)) #ПЕРЕМЕННАЯ пишется в 40 знакоместах - выравнивание по ПРАВОМУ краю
print(s.ljust(40)) #выравнивание по ЛЕВОМУ КРАЮ
print(s.center(40)) #Выравнивание по ЦЕНТРУ
print(s.strip()) #удаляем пробелы по краям
print(s.strip('!З ')) # удалил знаки и пробел
print(s.rstrip()) #удаляю справа
print(s.lstrip()) #удаляю слева
