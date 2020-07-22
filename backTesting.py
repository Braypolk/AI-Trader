import backtrader as bt
from strategies import TestStrategy

cerebro = bt.Cerebro()
cerebro.addstrategy(TestStrategy)
cerebro.broker.set_cash(1000000)

data = bt.feeds.YahooFinanceCSVData(
    dataname='BA.csv'
)

cerebro.adddata(data)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.plot()