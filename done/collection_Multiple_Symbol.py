import pymysql
import datetime
import collections

def collection_Multiple_Symbol():
    connection = pymysql.connect(host='vanxv.vicp.net',
                                     user='root',
                                     password='1121mysql',
                                     db='blockchain',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # create a new record
            #sql = "select symbol from marketPrice where symbol='ethbtc';"
            sql = "select symbol,priceAverage from marketPrice;"
            cursor.execute(sql)
            result = cursor.fetchall()

            # -- get symbol>1
            connectionSymbol = []

            cnt = collections.Counter()
            NN = 1
            for N in result:
                NN +=1
                if N['priceAverage'] == 0:
                    print(N['priceAverage'])
                    continue
                Nlower = N['symbol'].lower()
                cnt[Nlower] += 1
            for x,y in cnt.items():
                if y > 1:
                    connectionSymbol.append(x)
            print(connectionSymbol)
            return connectionSymbol

    finally:
        connection.close()



def differentPrice():
    symbol = collection_Multiple_Symbol()

    connection = pymysql.connect(host='vanxv.vicp.net',
                                 user='root',
                                 password='1121mysql',
                                 db='blockchain',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # create a new record
            # sql = "select symbol from marketPrice where symbol='ethbtc';"
            sqlcommand = ''
            symbolLen = len(symbol)-1
            for N in symbol:
                sqlcommand = sqlcommand +"symbol='"+ N + "'"
                symbolLen -= 1
                if symbolLen > -1:
                    sqlcommand = sqlcommand + ' or '

            sql = "select symbol,platform,priceAverage from marketPrice WHERE "+sqlcommand+";"
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchall()

            return result,symbol

    except:
        pass

def ValuePrice(values,symbol):
    valuesx ={}
    for N in symbol:
        for X in values:
            if X['symbol'].lower() == N:
                valuesx[X['platform']] = X['priceAverage']
        newValues = collections.OrderedDict(sorted(valuesx.items()))
        print(N,newValues)
getPrice,symbol = differentPrice()

ValuePrice(getPrice,symbol)