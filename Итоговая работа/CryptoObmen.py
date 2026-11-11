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



