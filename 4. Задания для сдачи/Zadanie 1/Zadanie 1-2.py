n = 8

while True:
    password = input("Введите пароль: ")
    if len(password) >= n:
        print ('Пароль введен')
        break
    print(f"Требуется не менее {n} символов!")