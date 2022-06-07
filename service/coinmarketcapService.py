import requests
from dotenv import dotenv_values

env = dotenv_values('.env')
COINMARKETCAP_API_KEY = env['coinmarketcap_api_key']

def get_coinmarketcap_price(symbols,pair):
    # use session from mutiple connection
    session = requests.Session()

     # send request for each symbol
    result = {}
    for symbol in symbols:
        #send request to api
        url = f'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?symbol={symbol.lower()}&convert={pair.lower()}'
        header = {'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY}
        response = session.get(url,headers=header)

        # good response, add price into result
        if response.status_code == 200:
            response =  response.json()
            result[symbol] = {
                'price': round(response['data'][symbol][0]['quote'][pair]['price'], 4),
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

