import pymysql.cursors

# connect to the database



symbol = ['omgusdt', 'linkbtc', 'naseth', 'eoseth', 'swftcbtc', 'zecusdt', 'dashbtc', 'paybtc', 'evxbtc', 'mdseth',
          'tntbtc', 'qasheth', 'smteth', 'bchbtc', 'iosteth', 'tnbbtc', 'gnxeth', 'thetabtc', 'sntusdt', 'datbtc',
          'eosusdt', 'chateth', 'manabtc', 'xrpbtc', 'ltcusdt', 'qtumusdt', 'letbtc', 'sntbtc', 'bcdbtc', 'cvcusdt',
          'elfeth', 'gnteth', 'utkbtc', 'sbtcbtc', 'neousdt', 'mcobtc', 'osteth', 'rcnbtc', 'bt2btc', 'qunbtc',
          'topceth', 'hsreth', 'salteth', 'aidoceth', 'waxbtc', 'cvceth', 'dtaeth', 'btcusdt', 'powreth', 'adxeth',
          'gaseth', 'saltbtc', 'neobtc', 'btmbtc', 'ekoeth', 'bateth', 'ekobtc', 'appcbtc', 'cmtbtc', 'veneth',
          'qtumeth', 'reqbtc', 'bifibtc', 'btmeth', 'icxbtc', 'zecbtc', 'actbtc', 'dgdeth', 'dateth', 'etcusdt',
          'ostbtc', 'iostusdt', 'mcoeth', 'storjbtc', 'hsrbtc', 'quneth', 'elfbtc', 'cmteth', 'venbtc', 'gntbtc',
          'dbcbtc', 'storjusdt', 'waxeth', 'powrbtc', 'dtabtc', 'nasbtc', 'tnbeth', 'swftceth', 'ltcbtc', 'eosbtc',
          'linketh', 'iostbtc', 'yeebtc', 'rdnbtc', 'gnxbtc', 'leteth', 'evxeth', 'astbtc', 'acteth', 'bchusdt',
          'dashusdt', 'icxeth', 'bcxbtc', 'propyeth', 'dgdbtc', 'xrpusdt', 'zrxbtc', 'thetaeth', 'ethbtc', 'dbceth',
          'reqeth', 'wicceth', 'smtbtc', 'rpxbtc', 'tnteth', 'ethusdt', 'itcbtc', 'omgbtc', 'payeth', 'venusdt',
          'mdsbtc', 'adxbtc', 'etcbtc', 'aidocbtc', 'kncbtc', 'hsrusdt', 'qtumbtc', 'cvcbtc', 'qspbtc', 'qspeth',
          'btgbtc', 'batbtc', 'qashbtc', 'itceth', 'xembtc', 'manaeth', 'gasbtc', 'chatbtc', 'bt1btc', 'omgeth',
          'utketh', 'rcneth', 'topcbtc', 'mtlbtc', 'gntusdt', 'appceth', 'propybtc', 'wiccbtc', 'rdneth', 'yeeeth']

for N in symbol:
    connection = pymysql.connect(host='vanxv.vicp.net',
                                 user='root',
                                 password='1121mysql',
                                 db='blockchain',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        #create a new record
        sql = "SELECT * FROM marketPrice;"
        #sqlInsert1 = "INSERT INTO marketPrice VALUES('system','huobi','2018-01-20 18:42:11',12,12,11,11,11,'values');"
        sqlInsert = "INSERT INTO marketPrice VALUES('"+ N +"','huobi','2018-01-20 18:42:11',12,12,11,11,11,'values');"
        cursor.execute(sqlInsert)

        connection.commit()
        connection.close()

