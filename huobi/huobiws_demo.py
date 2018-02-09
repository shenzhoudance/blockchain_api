# -*- coding: utf-8 -*-
#author: 半熟的韭菜

from websocket import create_connection
import gzip
import time
import datetime
from multiprocessing import Pool
Number = 1
#if __name__ == '__main__':
    # 订阅 KLine 数据
    #tradeStr="""{"sub": "market.ethusdt.kline.1min","id": "id10"}"""

    # 请求 KLine 数据
    # tradeStr="""{"req": "market.ethusdt.kline.1min","id": "id10", "from": 1513391453, "to": 1513392453}"""

    #订阅 Market Depth 数据
    #tradeStr="""{"sub": "market.ethusdt.depth.step0", "id": "id10"}"""

    #请求 Market Depth 数据
    # tradeStr="""{"req": "market.ethusdt.depth.step5", "id": "id10"}"""

    #订阅 Trade Detail 数据
    # tradeStr="""{"sub": "market.ethusdt.trade.detail", "id": "id10"}"""

    #请求 Trade Detail 数据
    # tradeStr="""{"req": "market.ethusdt.trade.detail", "id": "id10"}"""

    #请求 Market Detail 数据
    # tradeStr="""{"req": "market.ethusdt.detail", "id": "id12"}"""

def huobiws(symbol):
    while(3):
        time.sleep(2)
        try:
            ws = create_connection("wss://api.huobipro.com/ws")
            tradeStr='{"sub": "market.'+ symbol +'.depth.step1", "id": "id10"}'
            ws.send(tradeStr)
            number = 1
        except:
            continue
        while number < 4:
            try:
                compressData = ws.recv()
                result=gzip.decompress(compressData).decode('utf-8')
                if result[:7] == '{"ping"':
                    pass
                else:
                    number += 1
                    #print(symbol,result)
                    print(datetime.datetime.now(),symbol,result)
            except:
                print(datetime.datetime.now(),symbol,number)
                time.sleep(1)
                continue

with Pool(150) as pool:
    symbol = ['omgusdt', 'linkbtc', 'naseth', 'eoseth', 'swftcbtc', 'zecusdt', 'dashbtc', 'paybtc', 'evxbtc', 'mdseth', 'tntbtc', 'qasheth', 'smteth', 'bchbtc', 'iosteth', 'tnbbtc', 'gnxeth', 'thetabtc', 'sntusdt', 'datbtc', 'eosusdt', 'chateth', 'manabtc', 'xrpbtc', 'ltcusdt', 'qtumusdt', 'letbtc', 'sntbtc', 'bcdbtc', 'cvcusdt', 'elfeth', 'gnteth', 'utkbtc', 'sbtcbtc', 'neousdt', 'mcobtc', 'osteth', 'rcnbtc', 'bt2btc', 'qunbtc', 'topceth', 'hsreth', 'salteth', 'aidoceth', 'waxbtc', 'cvceth', 'dtaeth', 'btcusdt', 'powreth', 'adxeth', 'gaseth', 'saltbtc', 'neobtc', 'btmbtc', 'ekoeth', 'bateth', 'ekobtc', 'appcbtc', 'cmtbtc', 'veneth', 'qtumeth', 'reqbtc', 'bifibtc', 'btmeth', 'icxbtc', 'zecbtc', 'actbtc', 'dgdeth', 'dateth', 'etcusdt', 'ostbtc', 'iostusdt', 'mcoeth', 'storjbtc', 'hsrbtc', 'quneth', 'elfbtc', 'cmteth', 'venbtc', 'gntbtc', 'dbcbtc', 'storjusdt', 'waxeth', 'powrbtc', 'dtabtc', 'nasbtc', 'tnbeth', 'swftceth', 'ltcbtc', 'eosbtc', 'linketh', 'iostbtc', 'yeebtc', 'rdnbtc', 'gnxbtc', 'leteth', 'evxeth', 'astbtc', 'acteth', 'bchusdt', 'dashusdt', 'icxeth', 'bcxbtc', 'propyeth', 'dgdbtc', 'xrpusdt', 'zrxbtc', 'thetaeth', 'ethbtc', 'dbceth', 'reqeth', 'wicceth', 'smtbtc', 'rpxbtc', 'tnteth', 'ethusdt', 'itcbtc', 'omgbtc', 'payeth', 'venusdt', 'mdsbtc', 'adxbtc', 'etcbtc', 'aidocbtc', 'kncbtc', 'hsrusdt', 'qtumbtc', 'cvcbtc', 'qspbtc', 'qspeth', 'btgbtc', 'batbtc', 'qashbtc', 'itceth', 'xembtc', 'manaeth', 'gasbtc', 'chatbtc', 'bt1btc', 'omgeth', 'utketh', 'rcneth', 'topcbtc', 'mtlbtc', 'gntusdt', 'appceth', 'propybtc', 'wiccbtc', 'rdneth', 'yeeeth']
    #symbol = ['eoseth','eosbtc']
    pool.map(huobiws,symbol)
    #pool.map(huobiws,['omgusdt', 'linkbtc', 'naseth', 'eoseth', 'swftcbtc'])