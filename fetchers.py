from pycoingecko import CoinGeckoAPI
from datetime import datetime
from abc import ABC, abstractmethod

class CryptoFetcher(ABC):
    """
    Useful if more APIs are added to check prices of cryptos
    """
    @abstractmethod
    def get_price(self) -> dict:
        ...
    
    @abstractmethod
    def get_price_with_time(self, time_format: str) -> dict:
        ...

    @abstractmethod
    def list_coins(self) -> dict:
        ...


class CoinGeckoFetcher(CryptoFetcher):
    """
    CoinGeckoChecker class. This class is in charge of executing requests to coingecko and get prices for cyptocurrencies
    """
    def __init__(self, coin_name, vs='usd'):
        self.coin_name = coin_name
        self.vs_coin_name = vs
        self.cg = CoinGeckoAPI()
        self.current_price = None
    
    def __repr__(self):
        return f'CoinChecker(coin_name={self.coin_name}, vs_coin_name={self.vs_coin_name}, current_price={self.current_price})'
    
    def get_price(self):
        price =  self.cg.get_price(ids=self.coin_name, vs_currencies=self.vs_coin_name)
        self.current_price = price
        return price
    
    def get_price_with_time(self, time_format='%Y-%m-%d %H:%M:%S'):
        price = self.get_price()
        price['request_timestamp'] = datetime.now().strftime(time_format)
        return price
    
    def list_coins(self):
        return self.cg.get_coins_list()

bit = CoinGeckoFetcher('cryptogodz')
print(bit.get_price_with_time())
print(bit.list_coins())
