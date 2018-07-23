import cv2
# 基于opencv的haarcascade_frontalface_default.xml模板，实现检测，不能实现识别。
# https://blog.csdn.net/wireless_com/article/details/64120516
# C:\Users\gd012\AppData\Local\Continuum\anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml
#模板文件有好几个，如果要引用上面的文件，需要额外load
face_patterns = cv2.CascadeClassifier('D:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
# face_patterns.load('C:\/Users\gd012\AppData\Local\Continuum\/anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
sample_image = cv2.imread('silicon_valley.jpg')

faces = face_patterns.detectMultiScale(sample_image,scaleFactor=1.1,minNeighbors=5,minSize=(10, 10))

for (x, y, w, h) in faces:
    cv2.rectangle(sample_image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imwrite('okkkk.png', sample_image);