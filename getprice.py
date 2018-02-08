import csv
import time
import collections


# -- get mutliple symobl
with open('./huobi.csv', 'r', ) as huobifile:
    reader = csv.DictReader(huobifile)
    timex = time.time()
    print(timex)
    xtuple = []
    for row in reader:
        xtuple.append(row['symbol'])
    temp_dict = {}

    for row in reader:
        xtuple.append(row['symbol'])
        # temp_dict[row['symbol']] = [row['symbol'], row['platform'],
        #                                               row['datetime'],
        #                                               row['priceAverage'],
        #                                               row['buyPrice'],
        #                                               row['bNum'],
        #                                               row['sellPrice'],
        #                                               row['sNum'],
        #                                               row['allInfo']]


x = collections.Counter(xtuple)
getprice = []
for xx,y in x.items():
    if y > 1:
        getprice.append(xx)

# -- get symbol add dict


with open('./huobi.csv', 'r', ) as huobifile:
    reader = csv.DictReader(huobifile)
    temp_dict = {}
    for row in reader:
        temp_dict[row['symbol']+row['platform']] = [row['symbol'], row['platform'],
                                                      row['datetime'],
                                                      row['priceAverage'],
                                                      row['buyPrice'],
                                                      row['bNum'],
                                                      row['sellPrice'],
                                                      row['sNum'],
                                                      row['allInfo']]
for symbol in getprice:
    print(symbol)
    temp_price = {}
    for x,y in temp_dict.items():
        if symbol in x:
            print(x,round(float(y[3]),7))
    print(temp_price)
            #print(y[3])