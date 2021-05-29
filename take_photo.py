import cv2, os
import numpy as np
import pickle
from PIL import Image

def create_dataset():
    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    Name = input('Ingresar nombre de la persona> ')
    path_user = "dataSet/"+Name
    try:
        os.mkdir(path_user)
    except OSError as e:
        print('Ocurrio un error al crear la carpeta '+e)
        exit()

    sampleNum = 0
    print(cam)
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            print(x,y,w,h)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

            sampleNum=sampleNum + 1
            cv2.imwrite(path_user+"/User."+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
            cv2.putText(img, Name, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN,
                1,(0, 255, 0))
        cv2.imshow('Creando dataset', img)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

        elif sampleNum > 100:
            break

    cam.release()
    cv2.destroyAllWindows()


def recognize():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainner/trainner.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    with open("names.pickle","rb") as f:
        names = pickle.load(f)
    print(names)
    cam = cv2.VideoCapture(0)
    isIdentifyed = False

    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2,5)
        for(x, y, w, h) in faces:
            cv2.rectangle(im,(x, y),(x+w, y+h),(225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            # print()
            label="Buscando..."
            if(conf<100):
                label = names[Id]

            cv2.putText(im,str(label), org=(x,y+h),fontFace=font, color=(255,255,255), fontScale=1)

        cv2.imshow('im',im)
        # if isIdentifyed:
        #     break
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break


    cam.release()
    cv2.destroyAllWindows()

    return isIdentifyed
