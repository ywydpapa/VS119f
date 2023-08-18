import cv2
from dbConn import dbins


fire_cascade = cv2.CascadeClassifier('fire-cascade.xml')
ds_factor = 0.8


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture("carfireAVI.mp4")

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        image = cv2.resize(image, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
        sql = "insert into vsAlarm (siteID,alarmType,locationX,locationY,alarmTime) values ('100001','FIRE',%u,%u,now())" % (0, 0)
        dbins(sql)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fire = fire_cascade.detectMultiScale(image, 12, 5)
        for (x, y, w, h) in fire:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
#            sql = "insert into vsAlarm (siteID,alarmType,locationX,locationY,alarmTime) values ('100001','FIRE',%u,%u,now())" % (x, y)
#            dbins(sql)
            break

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
