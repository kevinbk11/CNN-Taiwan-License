import CutAndNet
import Detect
import find
import cv2
import threading as th
import os

def g():
    os.system("python .vscode\car\GUI.py")
cam=th.Thread(target=g)
cam.start()

cap = cv2.VideoCapture(0)
x=0
while(1):

    if(cap.isOpened()):
        ReadOrNot=False
        img,ReadOrNot = Detect.open(cap)
        if(ReadOrNot):
            FindOrNot,car=find.lpr(img)
            if(FindOrNot): 
                ans=CutAndNet.read(car) 
                fp=open(r"C:\Users\User\Desktop\c++\.vscode\car\data.pt","r")
                base=[]
                base=fp.readlines() 
                fp.close()  
                Out=True
                for x in base:
                    x=x.replace("\n","")
                    if ans==x:
                        print("歡迎")
                        Out=False
                        break
                if Out:
                    print("查無此車牌") 
            else:
                print("錯誤")
                continue      