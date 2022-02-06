from statistics import mode
from tokenize import Number
import cv2
import dropbox
import time
import random
start_time=time.time()

def take_picture():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        result=False
    return img_name
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_files(img_name):
    access_token="sl.BAom6_Q1J1gsQajJlwmcwnkJfFwwYU0LZIH8A-7csev_6U8WYLsIQe25sMld303v5x_JHoa7sxuSgqGelN7N4-16mo1eTEds3M2zD3A8rG8C_JAk3A_IZXyl37SWaJuPuEYj6897pvMH"
    file=img_name
    file_from=file
    file_to="/testfolder/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb')as c:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overWrite)
        print("File uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_picture()
            upload_files(name)

main()