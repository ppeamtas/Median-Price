import statistics


def get_all_median_price(all_price, pair):
    # get each median price or error message
    result = {}
    for symbol in all_price:
        result[symbol] = get_median_price(all_price[symbol], symbol, pair)

    return result


def get_median_price(price_list, symbol, pair):
    # if list is empty return error
    if len(price_list) == 0:
        return {
            'message': f'{symbol}-{pair} pairs is not exist in all sources',
            'error': True
        }

    # if price in list is less than 3 price return error
    if len(price_list) < 3:
        return {
            'message': f'{symbol}-{pair} pairs has less than 3 sources',
            'error': True
        }

    # return median price
    return {
            'price': round(statistics.median(price_list), 4),
            'pair': pair,
            'error': False
        }