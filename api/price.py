from fastapi import APIRouter
from starlette.responses import JSONResponse

from service.binanceService import get_binance_price
from service.coingeckoService import get_coingecko_price
from service.coinmarketcapService import get_coinmarketcap_price
from service.krakenService import get_kraken_price
from service.medianService import get_all_median_price
from service.okxService import get_okx_price


router = APIRouter()


def validate_parameter(symbols):
    # check symbols is not empty string
    if not symbols:
        return {'message': 'symbols can not be empty', 'error': True}, True

    # check symbols starting with '[' and ending with ']'
    if symbols[0] != '[' or symbols[-1] != ']':
        return {'message': 'invalid parameter symbols', 'error': True}, True

    symbols = symbols.strip()[1:-1]
    # check symbols is not empty list
    if not symbols:
        return {'message': 'symbols can not be empty', 'error': True}, True

    # change string parameter to list
    validated_parameter = [e.upper() for e in symbols.split(',')]
    return validated_parameter, False


# get all coin price for 5 api than return dictionary
def get_all_api_price(symbols_list, pair):
    binance = get_binance_price(symbols_list,pair)
    coinmarketcap = get_coinmarketcap_price(symbols_list,pair)
    okx = get_okx_price(symbols_list,pair)
    kraken = get_kraken_price(symbols_list,pair)
    coingecko = get_coingecko_price(symbols_list,pair)
    return {
        'binance': binance,
        'coinmarketcap': coinmarketcap,
        'okx': okx,
        'kraken': kraken,
        'coingecko': coingecko
    }


@router.get("/all_price")
async def get_all_price(symbols, pair='usdt'):
    validated_parameter, error = validate_parameter(symbols)
    if error:
        return JSONResponse(content=validated_parameter, status_code=400)

    return get_all_api_price(validated_parameter, pair.upper())


@router.get("/median_price")
async def get_median_price(symbols, pair='usdt'):
    validated_parameter, error = validate_parameter(symbols)
    if error:
        return JSONResponse(content=validated_parameter, status_code=400)

    # get all coin price from 5 api
    api_price = get_all_api_price(validated_parameter, pair.upper())

    # add all 5 price from api into a list
    all_price = {}
    for symbol in validated_parameter:
        all_price[symbol] = []
        for api in api_price:
            if not api_price[api][symbol]['error']:
                all_price[symbol].append(api_price[api][symbol]['price'])

    # get each median price from each list
    return get_all_median_price(all_price, pair.upper())
    

@router.get("/binance_price")
async def binance_price(symbols, pair='usdt'):
    validated_parameter, error = validate_parameter(symbols)
    if error:
        return JSONResponse(content=validated_parameter, status_code=400)

    return get_binance_price(validated_parameter, pair.upper())


@router.get("/coinmarketcap_price")
async def coinmarketcap_price(symbols, pair='usdt'):
    validated_parameter, error = validate_parameter(symbols)
    if error:
        return JSONResponse(content=validated_parameter, status_code=400)

    return get_coinmarketcap_price(validated_parameter, pair.upper())


@router.get("/okx_price")
async def okx_price(symbols, pair ='usdt'):
    validated_parameter, error = validate_parameter(symbols)
    if error:
        return JSONResponse(content=validated_parameter, status_code=400)

    return get_okx_price(validated_parameter, pair.upper())


@router.get("/kraken_price")
async def kraken_price(symbols, pair='usdt'):
    validated_parameter, error = validate_parameter(symbols)
    if error:
        return JSONResponse(content=validated_parameter, status_code=400)

    return get_kraken_price(validated_parameter, pair.upper())


@router.get("/coingecko_price")
async def coingecko_price(symbols, pair='usdt'):
    validated_parameter, error = validate_parameter(symbols)
    if error:
        return JSONResponse(content=validated_parameter, status_code=400)

    return get_coingecko_price(validated_parameter, pair.upper())
