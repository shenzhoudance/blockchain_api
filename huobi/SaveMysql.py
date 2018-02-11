import pymysql.cursors
import datetime
# connect to the database
def updateMysql(symbol,platform,priceAverage,buyprice,bNum,sellPrice,sNum,allInfo):
    connection = pymysql.connect(host='vanxv.vicp.net',
                                 user='root',
                                 password='1121mysql',
                                 db='blockchain',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        # create a new record
        # sql = "SELECT * FROM marketPrice;"
        sql = 'UPDATE blockchain.marketPrice SET priceAverage='+ priceAverage +' , buyPrice='+ buyprice +' , bNum='+ bNum +' , sellPrice='+ sellPrice +' , sNum='+ sNum +' , allInfo="'+ allInfo +'" WHERE symbol="'+ symbol +'" AND platform="'+ platform+'";'
        # sqlInsert1 = "INSERT INTO marketPrice VALUES('system','huobi','2018-01-20 18:42:11',12,12,11,11,11,'values');"
        # sqlInsert = "INSERT INTO marketPrice VALUES('" + symbol + "','huobi','2018-01-20 18:42:11',12,12,11,11,11,'values');"
        print(sql)
        cursor.execute(sql)
        connection.commit()
        connection.close()

if __name__ == "__main__":
    # execute only if run as a script
    #updateMysql('eoseth','huobi','1','2','3','4','5','6')
    pass