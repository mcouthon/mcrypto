import requests

from .constants import BTC
from .exceptions import APIError

CRYPTO_API_URL = 'https://api.cryptonator.com/api/ticker/{base}-{target}'
EXCHANGE_API_URL = 'http://api.fixer.io/latest?base=USD'
ALL_CURRENCIES_URL = 'https://www.cryptonator.com/api/currencies'


def get_btc_balance(base):
    url = CRYPTO_API_URL.format(base=base, target=BTC)
    try:
        result = requests.get(url).json()
        return float(result['ticker']['price'])
    except requests.RequestException as e:
        raise APIError('Could not get {1} price for {0}: {2}'.format(base,
                                                                     BTC, e))


def get_exchange_rates():
    try:
        return requests.get(EXCHANGE_API_URL).json()
    except requests.RequestException as e:
        raise APIError('Could not get exchange rates: {0}'.format(e))


def get_currencies():
    try:
        result = requests.get(ALL_CURRENCIES_URL).json()
        coins = result['rows']
        return {coin['code']: coin['name'] for coin in coins}
    except requests.RequestException as e:
        raise APIError('Could not update crypto currencies: {0}'.format(e))


def get_balance(coins):
    balance = {}
    for coin in coins:
        balance[coin] = get_btc_balance(coin)
    return balance
