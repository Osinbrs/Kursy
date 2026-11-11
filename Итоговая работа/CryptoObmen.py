from tkinter import *                 #добавляю библиотеку tkinter для создания графического окна
from tkinter import messagebox as mb  #библиотека для всплывающих окон предупреждения
from tkinter import ttk               #библиотека виджета выпадающих списков
import requests                       #библиотека для HTTP-запросов к API

#функции отображения выбранной криптовалюты
def update_base_label(event):
    base_label.config(text=crypto_display.get(base_combobox.get(), '')) #показывает название и расшифровку криптовалюты


def update_currency_label(event):
    target_label.config(text=cash_display.get(target_combobox.get(), '')) #показывает название и расшифровку валюты


#Основная функция обмена
def exchange():
    crypto = base_combobox.get()  #код криптовалюты, выбранный в списке криптовалют
    cash = target_combobox.get()  #код валюты, выбранный в списке валют

    if crypto and cash:  #если выбраны все поля происходит запрос к api
        try:
            url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_api_ids[crypto]}&vs_currencies={cash_codes[cash]}'
            response = requests.get(url, timeout=5)  # Отправляем запрос (таймаут 5 сек)
            response.raise_for_status()  #проверка статуса на ошибку с сервера
            data = response.json()  #формируем JSON-ответ в словарь

            #получаем курсы
            rate = data[crypto_api_ids[crypto]][cash_codes[cash]]

            #демонстрируется курс обмена во всплывающем окне
            mb.showinfo('Курс обмена', f'1 {crypto_display[crypto]} = {rate:.2f} {cash_display[cash]}')
        except Exception as er:
            mb.showerror('Ошибка', er)  #сообщение об ошике в окне
    else:
        mb.showwarning('Внимание', 'Выберите криптовалюту и валюту')  #если что-то не выбрано во выпадающих списках

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

