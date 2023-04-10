import requests
import time


# Здесь необходимо ввести API-ключ и секретный ключ Binance
api_key = 'ваш_api_ключ'
api_secret = 'ваш_секретный_ключ'

#  Здесь ввести URL для получения текущей цены фьючерсов на Binance
url = 'https://fapi.binance.com/fapi/v1/ticker/price'

#  оздал словарь для хранения максимальных цен за последний час
max_prices = {}

while True:
    # Отправляю запрос к API биржи Binance
    response = requests.get(url, headers={'X-MBX-APIKEY': api_key})

    # Получаю текущие цены фьючерсов на Binance
    prices = response.json()

    # Обрабатываю каждую пару
    for p in prices:
        # Получаю символ пары и текущую цену
        symbol = p['symbol']
        price = float(p['price'])

        # Если пары еще нет в словаре, она добавлется и далее устанавливаем максимальную цену равной текущей цене
        if symbol not in max_prices:
            max_prices[symbol] = price

        # Обновляем максимальную цену, если текущая цена выше
        if price > max_prices[symbol]:
            max_prices[symbol] = price
            
           

        # Проверяем, упала ли цена на 1% от максимальной цены за последний час
        if price < 0.99 * max_prices[symbol]:
            print(f'Цена фьючерса {symbol} упала на 1% от максимальной цены за последний час!')

    # Задержка в 1 секунду перед следующим запросом
    time.sleep(1)

    
    
# Отвечая на второй вопрос, чтобы получить все пары, можно изменить URL
# на 'https://fapi.binance.com/fapi/v1/exchangeInfo' и получить список всех пар,
# которые торгуются на Binance. Затем можно использовать этот список, чтобы
# получать текущую цену каждой пары и обрабатывать их, как в приведенном
# выше коде
