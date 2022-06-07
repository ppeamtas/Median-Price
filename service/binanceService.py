import requests

def get_binance_price(symbols, pair):
    # use session from mutiple connection
    session = requests.Session()

    # send request for each symbol
    result = {}
    for symbol in symbols:
        #send request to api
        query_string = symbol + pair
        url = f'https://www.binance.com/api/v3/ticker/price?symbol={query_string}'
        response = session.get(url)

        # good response, add price into result
        if response.status_code == 200:
            response =  response.json()
            result[symbol] = {
                'price': round(float(response['price']), 4),
                'pair': pair,
                'error': False
            }
        # bad response, add error into result
        else:
            result[symbol] = {
                'message': f'{symbol}-{pair} pairs is not exist',
                'error': True
            }
    return result