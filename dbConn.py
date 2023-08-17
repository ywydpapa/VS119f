import pymysql


def dbins(query):
    db = pymysql.connect(host='192.168.108.102', user='swcore', password='core2020', db='vtekmon', charset='utf8')
    cur = db.cursor()
    cur.execute(query)
    db.commit()
    db.close()


def dbsel(query):
    db = pymysql.connect(host='192.168.108.102', user='swcore', password='core2020', db='vtekmon', charset='utf8')
    cur = db.cursor()
    cur.execute(query)
    result = cur.fetchall()
    return result
    db.close()


def dbupd(query):
    db = pymysql.connect(host='192.168.108.102', user='swcore', password='core2020', db='vtekmon', charset='utf8')
    cur = db.cursor()
    cur.execute(query)
    db.commit()
    db.close()