import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()


#c.execute('''create table stocks(date text, trans text, symbol text, qty real, price real)''')

# 插入一行数据 insert a row of data
c.execute("insert into stocks values('2016-01-05', 'buy', 'rhat',100,35.14)")


conn.commit()
conn.close()

conn = sqlite3.connect('example.db')
c = conn.cursor()

#永远做这个 -- 插入
symbol = 'RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# 做这个插入
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

purchases = [('2006-03-28', 'BUY', 'IBM', 1000,45.00),
                        ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                        ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
                        ]
c.executemany('INSERT INTO stocks VALUES(?,?,?,?,?)', purchases)
c.execute('SELECT * FROM stocks')
for N in c.fetchall():
    print(N)

