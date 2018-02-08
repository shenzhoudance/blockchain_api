#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-20 15:40:03
# @Author  : KlausQiu
# @QQ      : 375235513
# @github  : https://github.com/KlausQIU

from Utils import *
import datetime
import csv
import time
'''
Market data API
'''


# 获取KLine
def get_kline(symbol, period, size=150):
    """
    :param symbol
    :param period: 可选值：{1min, 5min, 15min, 30min, 60min, 1day, 1mon, 1week, 1year }
    :param size: 可选值： [1,2000]
    :return:
    """
    params = {'symbol': symbol,
              'period': period,
              'size': size}

    url = MARKET_URL + '/market/history/kline'
    return http_get_request(url, params)


# 获取marketdepth
def get_depth(symbol, type):
    """
    :param symbol
    :param type: 可选值：{ percent10, step0, step1, step2, step3, step4, step5 }
    :return:
    """
    params = {'symbol': symbol,
              'type': type}
    
    url = MARKET_URL + '/market/depth'
    return http_get_request(url, params)


# 获取tradedetail
def get_trade(symbol):
    """
    :param symbol
    :return:
    """
    params = {'symbol': symbol}

    url = MARKET_URL + '/market/trade'
    return http_get_request(url, params)


# 获取merge ticker
def get_ticker(symbol):
    """
    :param symbol: 
    :return:
    """
    params = {'symbol': symbol}

    url = MARKET_URL + '/market/detail/merged'
    return http_get_request(url, params)


# 获取 Market Detail 24小时成交量数据
def get_detail(symbol):
    """
    :param symbol
    :return:
    """
    params = {'symbol': symbol}

    url = MARKET_URL + '/market/detail'
    return http_get_request(url, params)

# 获取  支持的交易对
def get_symbols(long_polling=None):
    """

    """
    params = {}
    if long_polling:
        params['long-polling'] = long_polling
    path = '/v1/common/symbols'
    return api_key_get(params, path)

'''
Trade/Account API
'''


def get_accounts():
    """
    :return: 
    """
    path = "/v1/account/accounts"
    params = {}
    return api_key_get(params, path)


# 获取当前账户资产
def get_balance(acct_id=None):
    """
    :param acct_id
    :return:
    """

    if not acct_id:
        accounts = get_accounts()
        acct_id = accounts['data'][0]['id'];

    url = "/v1/account/accounts/{0}/balance".format(acct_id)
    params = {"account-id": acct_id}
    return api_key_get(params, url)


# 下单

# 创建并执行订单
def send_order(amount, source, symbol, _type, price=0):
    """
    :param amount: 
    :param source: 如果使用借贷资产交易，请在下单接口,请求参数source中填写'margin-api'
    :param symbol: 
    :param _type: 可选值 {buy-market：市价买, sell-market：市价卖, buy-limit：限价买, sell-limit：限价卖}
    :param price: 
    :return: 
    """
    try:
        accounts = get_accounts()
        acct_id = accounts['data'][0]['id']
    except BaseException as e:
        print ('get acct_id error.%s' % e)
        acct_id = ACCOUNT_ID

    params = {"account-id": acct_id,
              "amount": amount,
              "symbol": symbol,
              "type": _type,
              "source": source}
    if price:
        params["price"] = price

    url = '/v1/order/orders/place'
    return api_key_post(params, url)


# 撤销订单
def cancel_order(order_id):
    """
    
    :param order_id: 
    :return: 
    """
    params = {}
    url = "/v1/order/orders/{0}/submitcancel".format(order_id)
    return api_key_post(params, url)


# 查询某个订单
def order_info(order_id):
    """
    
    :param order_id: 
    :return: 
    """
    params = {}
    url = "/v1/order/orders/{0}".format(order_id)
    return api_key_get(params, url)


# 查询某个订单的成交明细
def order_matchresults(order_id):
    """
    
    :param order_id: 
    :return: 
    """
    params = {}
    url = "/v1/order/orders/{0}/matchresults".format(order_id)
    return api_key_get(params, url)


# 查询当前委托、历史委托
def orders_list(symbol, states, types=None, start_date=None, end_date=None, _from=None, direct=None, size=None):
    """
    
    :param symbol: 
    :param states: 可选值 {pre-submitted 准备提交, submitted 已提交, partial-filled 部分成交, partial-canceled 部分成交撤销, filled 完全成交, canceled 已撤销}
    :param types: 可选值 {buy-market：市价买, sell-market：市价卖, buy-limit：限价买, sell-limit：限价卖}
    :param start_date: 
    :param end_date: 
    :param _from: 
    :param direct: 可选值{prev 向前，next 向后}
    :param size: 
    :return: 
    """
    params = {'symbol': symbol,
              'states': states}

    if types:
        params[types] = types
    if start_date:
        params['start-date'] = start_date
    if end_date:
        params['end-date'] = end_date
    if _from:
        params['from'] = _from
    if direct:
        params['direct'] = direct
    if size:
        params['size'] = size
    url = '/v1/order/orders'
    return api_key_get(params, url)


# 查询当前成交、历史成交
def orders_matchresults(symbol, types=None, start_date=None, end_date=None, _from=None, direct=None, size=None):
    """
    
    :param symbol: 
    :param types: 可选值 {buy-market：市价买, sell-market：市价卖, buy-limit：限价买, sell-limit：限价卖}
    :param start_date: 
    :param end_date: 
    :param _from: 
    :param direct: 可选值{prev 向前，next 向后}
    :param size: 
    :return: 
    """
    params = {'symbol': symbol}

    if types:
        params[types] = types
    if start_date:
        params['start-date'] = start_date
    if end_date:
        params['end-date'] = end_date
    if _from:
        params['from'] = _from
    if direct:
        params['direct'] = direct
    if size:
        params['size'] = size
    url = '/v1/order/matchresults'
    return api_key_get(params, url)



# 申请提现虚拟币
def withdraw(address_id, amount, currency, fee=0, addr_tag=""):
    """

    :param address_id: 
    :param amount: 
    :param currency:btc, ltc, bcc, eth, etc ...(火币Pro支持的币种)
    :param fee: 
    :param addr-tag:
    :return: {
              "status": "ok",
              "data": 700
            }
    """
    params = {'address-id': address_id,
              'amount': amount,
              "currency": currency,
              "fee": fee,
              "addr-tag": addr_tag}
    url = '/v1/dw/withdraw/api/create'

    return api_key_post(params, url)

# 申请取消提现虚拟币
def cancel_withdraw(address_id):
    """

    :param address_id: 
    :return: {
              "status": "ok",
              "data": 700
            }
    """
    params = {}
    url = '/v1/dw/withdraw-virtual/{0}/cancel'.format(address_id)

    return api_key_post(params, url)


'''
借贷API
'''

# 创建并执行借贷订单


def send_margin_order(amount, source, symbol, _type, price=0):
    """
    :param amount: 
    :param source: 'margin-api'
    :param symbol: 
    :param _type: 可选值 {buy-market：市价买, sell-market：市价卖, buy-limit：限价买, sell-limit：限价卖}
    :param price: 
    :return: 
    """
    try:
        accounts = get_accounts()
        acct_id = accounts['data'][0]['id']
    except BaseException as e:
        print ('get acct_id error.%s' % e)
        acct_id = ACCOUNT_ID

    params = {"account-id": acct_id,
              "amount": amount,
              "symbol": symbol,
              "type": _type,
              "source": 'margin-api'}
    if price:
        params["price"] = price

    url = '/v1/order/orders/place'
    return api_key_post(params, url)

# 现货账户划入至借贷账户


def exchange_to_margin(symbol, currency, amount):
    """
    :param amount: 
    :param currency: 
    :param symbol: 
    :return: 
    """
    params = {"symbol": symbol,
              "currency": currency,
              "amount": amount}

    url = "/v1/dw/transfer-in/margin"
    return api_key_post(params, url)

# 借贷账户划出至现货账户


def margin_to_exchange(symbol, currency, amount):
    """
    :param amount: 
    :param currency: 
    :param symbol: 
    :return: 
    """
    params = {"symbol": symbol,
              "currency": currency,
              "amount": amount}

    url = "/v1/dw/transfer-out/margin"
    return api_key_post(params, url)

# 申请借贷
def get_margin(symbol, currency, amount):
    """
    :param amount: 
    :param currency: 
    :param symbol: 
    :return: 
    """
    params = {"symbol": symbol,
              "currency": currency,
              "amount": amount}
    url = "/v1/margin/orders"
    return api_key_post(params, url)

# 归还借贷
def repay_margin(order_id, amount):
    """
    :param order_id: 
    :param amount: 
    :return: 
    """
    params = {"order-id": order_id,
              "amount": amount}
    url = "/v1/margin/orders/{0}/repay".format(order_id)
    return api_key_post(params, url)

# 借贷订单
def loan_orders(symbol, currency, start_date="", end_date="", start="", direct="", size=""):
    """
    :param symbol: 
    :param currency: 
    :param direct: prev 向前，next 向后
    :return: 
    """
    params = {"symbol": symbol,
              "currency": currency}
    if start_date:
        params["start-date"] = start_date
    if end_date:
        params["end-date"] = end_date
    if start:
        params["from"] = start
    if direct and direct in ["prev", "next"]:
        params["direct"] = direct
    if size:
        params["size"] = size
    url = "/v1/margin/loan-orders"
    return api_key_get(params, url)


# 借贷账户详情,支持查询单个币种
def margin_balance(symbol):
    """
    :param symbol: 
    :return: 
    """
    params = {}
    url = "/v1/margin/accounts/balance"
    if symbol:
        params['symbol'] = symbol
    return api_key_get(params, url)


if __name__ == '__main__':
    get_symbols_inf = get_symbols()['data']
    get_symbols_all = []
    for x in get_symbols_inf:
        get_symbols_all.append(x['base-currency'] + x['quote-currency'])
    # x = 0
    # for N in get_symbols_inf:
    #     x +=1
    #     print(N)
    # print(x)
    #print(get_detail('btcusdt'))
    #print(get_trade('btcusdt'))
    #print(get_ticker('btcusdt'))
    print(datetime.datetime.now())
    #btcusdt = get_depth(symbol='btcusd', type='step5')

    #print(btcusdt)
    #print(btcusdt['bids'])
    #print(btcusdt['asks'])
    print('----')


    # etcbtc = get_depth(symbol='eoseth', type='step5')['tick']
    # print(etcbtc['bids'])
    # print(etcbtc['asks'])


    def save_csv_get_depth(symbol):
        print(symbol)
        symbolname = symbol
        symbol = symbolname.replace('_','')
        platForm = 'huobi'
        filednames = ['symbol', 'platform', 'datetime', 'priceAverage', 'buyPrice', 'bNum', 'sellPrice', 'sNum',
                      'allInfo']

        symbolprice = get_depth(symbol=symbol, type='step0')['tick']
        with open('../huobi.csv', 'r', ) as huobifile:

            reader = csv.DictReader(huobifile)
            timex = time.time()
            temp_dict = {}
            for row in reader:
                temp_dict[row['symbol'] + row['platform']] = [row['symbol'], row['platform'],
                                                              row['datetime'],
                                                              row['priceAverage'],
                                                              row['buyPrice'],
                                                              row['bNum'],
                                                              row['sellPrice'],
                                                              row['sNum'],
                                                              row['allInfo']]

            symbolTrue = symbol+platForm

        if symbolTrue in temp_dict:
            temp_dict[symbolTrue] =[symbol,platForm,
                                    datetime.datetime.now(),
                                    str((symbolprice['asks'][-1][0] + symbolprice['bids'][0][0]) * 0.5),
                                    symbolprice['bids'][0][0], symbolprice['bids'][0][1],
                                    symbolprice['asks'][0][0], symbolprice['asks'][0][1],
                                    symbolprice]

            with open('../huobi.csv', 'w', ) as huobifile:
                csvwriter = csv.DictWriter(huobifile, fieldnames=filednames)
                csvwriter.writeheader()
                for name, key in temp_dict.items():
                    csvwriterValue = {'symbol': key[0], 'platform': key[1], 'datetime': key[2], 'priceAverage': key[3],
                                      'buyPrice': key[4], 'bNum': key[5], 'sellPrice': key[6], 'sNum': key[7],
                                      'allInfo': key[8]}
                    csvwriter.writerow(csvwriterValue)
        else:
            with open('../huobi.csv', 'a', ) as huobifile:
                csvwriter = csv.DictWriter(huobifile, fieldnames=filednames)
                csvwriterValue = {'datetime': datetime.datetime.now(), 'platform': platForm, 'symbol': symbol}
                csvwriterValue['priceAverage'] = round((symbolprice['asks'][-1][0] + symbolprice['bids'][0][0]) * 0.5, 5)
                csvwriterValue['buyPrice'] = symbolprice['bids'][0][0]
                csvwriterValue['bNum'] = symbolprice['bids'][0][1]
                csvwriterValue['sellPrice'] = symbolprice['asks'][0][0]
                csvwriterValue['sNum'] = symbolprice['asks'][0][1]
                csvwriterValue['allInfo'] = symbolprice
                csvwriter.writerow(csvwriterValue)
            # -- save data -- #
        print(time.time()-timex)
    # --huobi_symbols_all--#
    # ['omgusdt', 'linkbtc', 'naseth', 'eoseth', 'swftcbtc', 'zecusdt', 'dashbtc', 'paybtc', 'evxbtc', 'mdseth', 'tntbtc', 'qasheth', 'smteth', 'bchbtc', 'iosteth', 'tnbbtc', 'gnxeth', 'thetabtc', 'sntusdt', 'datbtc', 'eosusdt', 'chateth', 'manabtc', 'xrpbtc', 'ltcusdt', 'qtumusdt', 'letbtc', 'sntbtc', 'bcdbtc', 'cvcusdt', 'elfeth', 'gnteth', 'utkbtc', 'sbtcbtc', 'neousdt', 'mcobtc', 'osteth', 'rcnbtc', 'bt2btc', 'qunbtc', 'topceth', 'hsreth', 'salteth', 'aidoceth', 'waxbtc', 'cvceth', 'dtaeth', 'btcusdt', 'powreth', 'adxeth', 'gaseth', 'saltbtc', 'neobtc', 'btmbtc', 'ekoeth', 'bateth', 'ekobtc', 'appcbtc', 'cmtbtc', 'veneth', 'qtumeth', 'reqbtc', 'bifibtc', 'btmeth', 'icxbtc', 'zecbtc', 'actbtc', 'dgdeth', 'dateth', 'etcusdt', 'ostbtc', 'iostusdt', 'mcoeth', 'storjbtc', 'hsrbtc', 'quneth', 'elfbtc', 'cmteth', 'venbtc', 'gntbtc', 'dbcbtc', 'storjusdt', 'waxeth', 'powrbtc', 'dtabtc', 'nasbtc', 'tnbeth', 'swftceth', 'ltcbtc', 'eosbtc', 'linketh', 'iostbtc', 'yeebtc', 'rdnbtc', 'gnxbtc', 'leteth', 'evxeth', 'astbtc', 'acteth', 'bchusdt', 'dashusdt', 'icxeth', 'bcxbtc', 'propyeth', 'dgdbtc', 'xrpusdt', 'zrxbtc', 'thetaeth', 'ethbtc', 'dbceth', 'reqeth', 'wicceth', 'smtbtc', 'rpxbtc', 'tnteth', 'ethusdt', 'itcbtc', 'omgbtc', 'payeth', 'venusdt', 'mdsbtc', 'adxbtc', 'etcbtc', 'aidocbtc', 'kncbtc', 'hsrusdt', 'qtumbtc', 'cvcbtc', 'qspbtc', 'qspeth', 'btgbtc', 'batbtc', 'qashbtc', 'itceth', 'xembtc', 'manaeth', 'gasbtc', 'chatbtc', 'bt1btc', 'omgeth', 'utketh', 'rcneth', 'topcbtc', 'mtlbtc', 'gntusdt', 'appceth', 'propybtc', 'wiccbtc', 'rdneth', 'yeeeth']
    get_symbols_all.remove('bt1btc')
    get_symbols_all.remove('bt2btc')
    # get_symbols_all.remove('kncbtc')
    # get_symbols_all.remove('propybtc')
    # get_symbols_all.remove('wiccbtc')
    # get_symbols_all.remove('rdneth')


    # for x in get_symbols_all:
    #     print(x)
    #     #save_csv_get_depth('eoseth')
    #     save_csv_get_depth(x)

    from multiprocessing import Pool

    if __name__ == '__main__':
        with Pool(80) as p:
            print(p.map(save_csv_get_depth, get_symbols_all))

