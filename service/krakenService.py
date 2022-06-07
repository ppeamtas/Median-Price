import requests

def get_kraken_price(symbols, pair):
    # use session from mutiple connection
    session = requests.Session()

     # send request for each symbol
    result = {}
    for symbol in symbols:
        #send request to api
        query_string = symbol + pair
        url = f'https://api.kraken.com/0/public/Ticker?pair={query_string}'
        response = session.get(url)
        response =  response.json()

        # good response, add price into result
        if 'result' in response:
            result[symbol] = {
                'price': round(float(list(response['result'].values())[0]['c'][0]), 4),
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