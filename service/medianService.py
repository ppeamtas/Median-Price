import statistics
import numpy as np


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
    
    # remove outliner
    price_list = remove_outlier(price_list)

    # return median price
    return {
            'price': round(statistics.median(price_list), 4),
            'pair': pair,
            'error': False
        }

def remove_outlier(price_list):
    # Set upper and lower limit to 3 standard deviation
    price_std = np.std(price_list)
    price_mean = np.mean(price_list)
    price_cut_off = price_std * 3
    lower_limit  = price_mean - price_cut_off 
    upper_limit = price_mean + price_cut_off

    # if std is 0 all price are equal, do not remove any price
    if price_std == 0:
        return price_list

    # add price that is not outlier to result
    result = []
    for x in price_list:
        if lower_limit < x < upper_limit:
            result.append(x)
    
    return result