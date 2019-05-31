import tushare as ts
import matplotlib.pyplot as plt
import datetime
import pandas as pd

pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 4000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

def test():
    ticker = '600050'
    finace = ts.get_hist_data(ticker, '2019-02-01', '2019-04-30')

    open = [a for a in finace["open"]]
    dates = [datetime.datetime.strptime(a.encode('utf-8'), "%Y-%m-%d") for a in finace.index]
    price_change = [q for q in finace["price_change"]]
    dates = [datetime.datetime.strptime(q.encode('utf-8'), "%Y-%m-%d") for q in finace.index]
    ma = [x for x in finace["ma5"]]
    dates = [datetime.datetime.strptime(x.encode('utf-8'), "%Y-%m-%d") for x in finace.index]

    empty = []
    for i in ma:
        i = (i / 2)
        empty.append(i)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    # ax.plot_date(dates, open, '-')
    # ax.plot_date(dates, price_change, '-')
    # ax.plot_date(dates, ma, '-')
    ax.plot_date(dates, empty, '-')
    fig.autofmt_xdate()
    plt.show()

def get_another():
    pepe = ts.get_stock_basics()
    pe2 = [p for p in pepe["pe"]]
    #pepe = ts.get_cashflow_data(2018,4)
    #pepe.to_csv('d:/test/growth.csv')
    #print(pepe)
    calc = []
    for t in pe2:
        t = (t/2)
        calc.append(t)

    print(calc)
    print(pe2)

def peg():
    basic = ts.get_stock_basics()
    peinpeg = [g for g in basic["pe"]]

    growth181 = ts.get_growth_data(2018,1)
    nprg181 = [a for a in growth181["nprg"]]
    growth182 = ts.get_growth_data(2018,2)
    nprg182 = [b for b in growth182["nprg"]]
    growth183 = ts.get_growth_data(2018,3)
    nprg183 = [c for c in growth183["nprg"]]
    growth184 = ts.get_growth_data(2018,4)
    nprg184 = [d for d in growth184["nprg"]]
    average = [nprg181[i]+nprg182[i]+nprg183[i]+nprg184[i] for i in range(0,len(nprg181))]

    print(average)

if __name__ == '__main__':
    peg()
