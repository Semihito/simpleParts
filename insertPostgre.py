# -*- coding: shift_jis -*-

#引数として日付を受け取る

#import package
import csv
import pprint
import pgdb
import sys

#PostgreSQL接続設定
con = pgdb.Connection(host="HOST",database="DATABASE",user="USER",password="PASSWORD")
cur = con.cursor()

#csvを開く
with open(r'D:/xxx/file.csv', newline='') as csvfile:
    read = csv.reader(csvfile)
    args = sys.argv
    date = args[1]
    #最初の一行目を飛ばす
    next(csvfile)
    #Excelの一番下の行まで読み込みつつ、SQL実行
    for row in read:
       #シーケンスとタイムスタンプ使用      
        sql = "INSERT INTO table VALUES(nextval('xxx_seq'),%(引数名)s,'{}','{}','{}','{}','{}',{},{},{},{},{})"
        sql = sql.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],int(row[7]),float(row[8]),int(row[9]),int(row[10]),int(row[11]))
        cur.execute(sql, {'引数名': (引数名,)})
        con.commit()

cur.close()
con.close()
