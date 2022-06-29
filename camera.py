import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
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
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #얼굴용
        face_rects = face_cascade.detectMultiScale(gray, 1.3, 5) # 얼굴용
        fire = fire_cascade.detectMultiScale(image, 12, 5)
        for (x, y, w, h) in face_rects: #얼굴용
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2) #얼굴용
            #인식후 화면 저장 및 데이터베이스 인서트
            break #얼굴용

        for (x, y, w, h) in fire: #불꽃용
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # 인식후 화면 저장 및 데이터베이스 인서트
            break
            
        ret, jpeg = cv2.imencode('.jpg', image) #겸용
        return jpeg.tobytes()
