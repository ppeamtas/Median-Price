import requests

def get_okx_price(symbols, pair):
    # use session from mutiple connection
    session = requests.Session()

     # send request for each symbol
    result = {}
    for symbol in symbols:
        #send request to api
        query_string = symbol + '-' + pair
        url = (f'https://www.okx.com/api/v5/market/index-tickers?instId={query_string}')
        response = session.get(url)
        response =  response.json()

        # good response, add price into result
        if len(response['data']) > 0:
            result[symbol] = {
                'price': round(float(response['data'][0]['idxPx']), 4),
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