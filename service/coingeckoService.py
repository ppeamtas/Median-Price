import requests

def get_coingecko_price(symbols, pair):
    # use session from mutiple connection
    session = requests.Session()

     # send request for each symbol
    result = {}
    for symbol in symbols:
        # get coin id from search api 
        # because price api request coin id
        search_url = f'https://api.coingecko.com/api/v3/search?query={symbol.lower()}'
        search_response = session.get(search_url)

        # good response from search api
        if search_response.status_code == 200:
            search_response =  search_response.json()

            # check search response symbol is match with input symbol
            if search_response['coins'][0]['symbol'] == symbol:
                # send request to price api
                id = search_response['coins'][0]['id']
                url = f'https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies={pair.lower()}'
                response = session.get(url)
                response =  response.json()

                # good response from price api, add price into result
                if pair in response[id]:
                    result[symbol] = {
                        'price': round(float(response[id][pair.lower()]), 4),
                        'pair': pair,
                        'error': False
                    }
                # bad response from price api, add error into result
                else:
                    result[symbol] = {
                        'message': f'{symbol}-{pair} pairs is not exist',
                        'error': True
                    }
            # symbol do not match, add error into result
            else:
                result[symbol] = {
                    'message': f'{symbol}-{pair} pairs is not exist',
                    'error': True
                }
        # bad response from search api, add error into result
        else:
            result[symbol] = {
                'message': f'{symbol}-{pair} pairs is not exist',
                'error': True
            }
    return result