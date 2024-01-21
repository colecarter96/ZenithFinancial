from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

class AlpacaTrading:
    def __init__ (self):
        self.apiKey = "PK982XMHD9WKP2SAODOQ"
        self.apiSecret = "dWiMdoQXTl3MFP1CnBO3AsVOUJOipcGjy4TDYxqn"
        self.tradingClient = TradingClient(self.apiKey, self.apiSecret)
        self.account = self.tradingClient.get_account()

        self.mODList = []
        print('${} is available as buying power.'.format(self.account.buying_power))



    # # Check if our account is restricted from trading.
    def checkBlocked(self):
        if self.account.trading_blocked:
            return True
        return False
    
    # # Check how much money we can use to open new positions.
    def getBuyPower(self):
        return self.account.buying_power
    
    # # Get our account information.
    def getAcctInfo(self):
        return self.tradingClient.get_account()
    
    # # Check our current balance vs. our balance at the last market close
    def getBalChange(self):
        return float(self.account.equity) - float(self.account.last_equity)
    
    # Check if tradeable
    def checkTradable(self, tx):
        asset = self.tradingClient.get_asset(tx)
        return asset.tradable
    
    # Prepare market order data
    def prepMarketOrderBuy(self, symb, qty):
        marketOrderData = MarketOrderRequest(
                    symbol=symb,
                    qty=qty,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                    )
        return marketOrderData
    
     # Prepare market order data
    def prepMarketOrderSell(self, symb, qty):
        marketOrderData = MarketOrderRequest(
                    symbol=symb,
                    qty=qty,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.DAY
                    )
        return marketOrderData
    
    def makeMarketOrder(self, mOD):
        marketOrder = self.tradingClient.submit_order(
                order_data=mOD
               )
        return marketOrder
    

    # Prepares all market Orders given dict made by GetTrades()
    def prepMarketOrders(self, dict):
        self.mODList = []
        tempTrade = None
        for i in dict:
            tempTrade = dict.get(i)
            if tempTrade.getType() == 'Buy':
                marketOrderData = self.prepMarketOrderBuy(tempTrade.getTicker(), 1)
                self.mODList.append(marketOrderData)
            # elif tempTrade.getType() == 'Sell':
            #     marketOrderData = self.prepMarketOrderSell(tempTrade.getTicker(), 1)
            #     self.mODList.append(marketOrderData)

        return self.mODList
    
    # Executes market Orders given market order data
    def executeMarketOrders(self, mOD):
        for i in mOD:
            self.makeMarketOrder(i)
        print("Successfully bought new data")

    