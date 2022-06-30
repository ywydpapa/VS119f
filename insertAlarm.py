import pymysql


def dbquery(query):
    db = pymysql.connect(host='192.168.108.25', user='swcore', password='core2020', db='vs119f', charset='utf8')
    cur = db.cursor()
    cur.execute(query)
    db.commit()
    db.close()
