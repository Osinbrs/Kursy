from tkinter import *                 #добавляю библиотеку tkinter для создания графического окна

#создание графического интерфейса - основного окна, титульное название, его размер
root = Tk()
root.title('Курс криптовалют')
root.geometry('360x220')

#создание словарей с их идентификаторами (id)
crypto_api_ids = {
    'BTC': 'bitcoin', 'ETH': 'ethereum', 'BNB': 'binancecoin',
    'SOL': 'solana', 'GRAM': 'the-open-network', 'USDT': 'tether'
}

#как отражены названия криптовалют
crypto_display = {
    'BTC': 'Биткоин', 'ETH': 'Эфириум', 'BNB': 'Бинанс Коин',
    'SOL': 'Солана', 'GRAM': 'Грамм', 'USDT': 'Tether'
}

#Валюта с их id
cash_codes = {'USD': 'usd', 'RUB': 'rub'}

#как отражены названия криптовалют
cash_display = {'USD': 'Доллар США', 'RUB': 'Российский рубль'}

#создание графического интерфейса - основного окна, титульное название, его размер
root = Tk()
root.title('Курс криптовалют')
root.geometry('360x220')

#создание всплывающих сообщений
Label(root, text='Криптовалюта').pack()  #Название раздела вспылвающих криптовалют
base_combobox = ttk.Combobox(root, values=list(crypto_api_ids.keys()))  #выпадающий список криптовалют
base_combobox.pack(pady=3, padx=10)  #размещение списка в окне
base_combobox.bind('<<ComboboxSelected>>', update_base_label)  #после выбора — пишется название
base_label = ttk.Label()  #метка для расшифровки
base_label.pack()  #размещение метки

# Блок выбора фиатной валюты
Label(root, text='Валюта').pack(padx=10)  # Подпись над списком
target_combobox = ttk.Combobox(root, values=list(cash_codes.keys()))  # Выпадающий список
target_combobox.pack(pady=3, padx=10)  # Размещение списка
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)  # При выборе — обновить подпись
target_label = ttk.Label()  # Метка для расшифровки
target_label.pack()  # Размещение метки

Button(root, text='Получить курс обмена', command=exchange).pack(pady=10, padx=10) #кнопка получения курса обмена

root.mainloop() #включение цикла приложения

