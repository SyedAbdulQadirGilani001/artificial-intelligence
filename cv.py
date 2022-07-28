# # # # from sre_constants import SUCCESS
# # # # import cv2 as cv
# # # # import cvzone
# # # # from cvzone.FaceMeshModule import FaceMeshDetector
# # # # import sys
# # # # # img=cv.imread('289703448_110389371712160_7438562742188690351_n.jpg')
# # # # # cv.imshow('image',img)
# # # # # cv.waitKey(0)
# # # # cap=cv.VideoCapture(0)
# # # # while True:
# # # #     success,img=cap.read()
# # # #     cv.imshow('image',img)
# # # #     cv.waitKey(1)
# # # # from lib2to3.pgen2.token import GREATER
# # # import numpy as np
# # # import cv2 as cv
# # # # img=cv.imread('image.jpg')
# # # # img=cv.resize(img,(500,500))
# # # # gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# # # # cv.imshow('gray-image',gray)
# # # # cv.waitKey(0)
# # # # cv.destroyAllWindows()
# # # # img=cv.imread('image.jpg')
# # # # gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# # # # (thresh,b_w)=cv.threshold(img,127,255,cv.THRESH_BINARY)
# # # # gray=gray.resize((500,500))
# # # # cv.imshow('b_w',b_w)
# # # # cv.imshow('thresh',thresh)
# # # # cv.imshow('gray-image',gray)
# # # # cv.imshow('img',img)
# # # # cv.waitKey(0)
# # # # # cv.destroyAllWindows()
# # # # import cv2
# # # # originalImage = cv2.imread('image.jpg')
# # # # grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
  
# # # # (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
 
# # # # cv2.imshow('Black white image', blackAndWhiteImage)
# # # # cv2.imshow('Original image',originalImage)
# # # # cv2.imshow('Gray image', grayImage)
  
# # # # cv2.waitKey(0)
# # # # cv2.destroyAllWindows()
# # # import cv2 as cv
# # # import numpy as np
# # # cap=cv.VideoCapture(0)
# # # # while (cap.isOpened()):
# # # #     ret,frame=cap.read()
# # # #     if ret==True:
# # # #         cv.imshow('frame',frame)
# # # #         if cv.waitKey(1) & 0xFF==ord('q'):
# # # #             break
# # # #     else:
# # # #         break
# # # # cap.release()
# # # # cv.destroyAllWindows()
# # # from matplotlib.colors import is_color_like
# # # cap=cv.VideoCapture('Ya_Rahman_-_Qari_Mashary.mp4')
# # # frame_width=int(cap.get(3))
# # # frame_height=int(cap.get(4))
# # # out=cv.VideoWriter('output.avi',cv.VideoWriter_fourcc('M','J','P','G'),10,(frame_width,frame_height),isColor=False)
# # # while (True):
# # #     (ret,frame)=cap.read()
# # #     gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
# # #     if ret==True:
# # #         out.write(gray)
# # #         cv.imshow('frame',gray)
# # #         if cv.waitKey(1) & 0xFF==ord('q'):
# # #             break
# # #     # (thresh,b_w)=cv.threshold(gray,127,255,cv.THRESH_BINARY)
# # #     # cv.imshow('frame',frame)
# # #     # cv.imshow('gray',gray)
# # #     # cv.imshow('b_w',b_w)
# # #     # if cv.waitKey(1) & 0xFF==ord('q'):
# # #     #     break
# # # out.release()
# # # cap.release()
# # # cv.destroyAllWindows()
# # # capture webcam video
# # # import cv2 as cv
# # # # from matplotlib.pyplot import gray
# # # import numpy as np
# # # cap=cv.VideoCapture(0)
# # # frame_width=int(cap.get(3))
# # # frame_height=int(cap.get(4))
# # # out=cv.VideoWriter('output.avi',cv.VideoWriter_fourcc('M','J','P','G'),10,(frame_width,frame_height),isColor=False)
# # # # if cap.isOpened()==False:
# # # #     print('Error opening video stream or file')
# # # while (True):
# # #     (ret,frame)=cap.read()
# # #     gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
# # #     if ret==True:
# # #         out.write(gray_frame)
# # #         cv.imshow('frame',gray_frame)
# # #         if cv.waitKey(1) & 0xFF==ord('q'):
# # #             break
# # # cap.release()
# # # out.release()
# # # cv.destroyAllWindows()
# # # import cv2 as cv
# # # import numpy as np
# # # cap=cv.VideoCapture(0)
# # # cap.set(10,100) # set brightness to 100
# # # cap.set(3,640) # set contrast to 640 we can also use cap.set(3,640) width
# # # cap.set(4,480) # set brightness to 480 height
# # # while (True):
# # #     ret,frame=cap.read()
# # #     if ret==True:
# # #         cv.imshow('frame',frame)
# # #         if cv.waitKey(1) & 0xFF==ord('q'):
# # #             break
# # #     else:
# # #         break
# # # cap.release()
# # # cv.destroyAllWindows()
# # from configparser import InterpolationSyntaxError
# # import cv2 as cv
# # import numpy as np
# # from cv2 import dilate
# # img=cv.imread('049.png')

# # blur_img=cv.GaussianBlur(img,(23,23),0)
# # edge_detection=cv.Canny(img,53,53)
# # # mat_kernel=np.ones((3,3),np.uint8)
# # # dilate_thickness_img=cv.dilate(edge_detection,(mat_kernel),iterations=3)
# # # erode_img=cv.erode(dilate_thickness_img,(mat_kernel),iterations=3)
# # # resize
# # resized_img=cv.resize(img,(350,250))
# # crop_image=resized_img[0:500,0:350]
# # cv.imshow('image',img)
# # cv.imshow('crop',crop_image)
# # # cv.imshow('dilated image',dilate_thickness_img)
# # # cv.imshow('edge_detection',edge_detection)
# # # cv.imshow('erroded image',erode_img)
# # # cv.imshow('blur_image',blur_img)
# # print(img.shape)
# # # cv.imshow('resized_img',resized_img)
# # # gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# # # binary=cv.threshold(img,127,255,cv.THRESH_BINARY)
# # # cv.imshow('gray_img',gray_img)
# # # cv.waitKey(0)
# # # cv.destroyAllWindows()
# # # # if cv.waitKey(1) & 0xFF==ord('q'):
# # # #     break
# # # import argparse
# import cv2 as cv
# from matplotlib.animation import ImageMagickBase
# import numpy as np
# # import argparse
# # parser=argparse.ArgumentParser()
# img=np.zeros((600,600))
# # img1=np.ones((600,600))
# print(img.shape)
# color_img=np.zeros((600,600,3),np.uint8)
# color_img[:]=255,0,255
# color_img[150:230,100:500]=255,188,10
# cv.line(color_img,(100,100),(300,300),(255,255,50),3) 
# # part line
# cv.line(color_img,(0,0),(color_img.shape[0],color_img.shape[1]),(255,0,0),3)
# # cross line
# cv.rectangle(color_img,(50,100),(300,400),(255,255,255),3)
# cv.rectangle(color_img,(50,100),(300,400),(255,255,255),cv.FILLED)
# cv.circle(color_img,(400,300),50,(255,100,0),5)
# cv.circle(color_img,(400,300),50,(255,100,0),cv.FILLED)
# cv.putText(color_img,'Hello, \n How are you',(200,500),cv.FONT_HERSHEY_DUPLEX,1,(255,255,0),1)
# # cv.imshow('black',img)
# cv.imshow('color',color_img)
# # cv.imshow('white',img1)
# cv.waitKey(0)
# cv.destroyAllWindows()
from tkinter import EW
import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)
# hd
def hd_resolution():
    cap.set(3,1280)
    cap.set(4,720)
hd_resolution()
# def sd_resolution():
#     cap.set(3,640)
#     cap.set(4,480)
# sd_resolution()
# def fh_d():
#     cap.set(3,1920)
#     cap.set(4,1080)
# fh_d()
# while (True):
#     ret,frame=cap.read()
#     if ret==True:
#         cv.imshow('frame',frame)
#         if cv.waitKey(1) & 0xFF==ord('q'):
#             break
#     else:
#         break
# cap.release()
# cv.destroyAllWindows()
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
print(frame_width,frame_height)
out=cv.VideoWriter('output.avi',cv.VideoWriter_fourcc('M','J','P','G'),30,(frame_width,frame_height))
while (True):
    ret,frame=cap.read()
    if ret==True:
        out.write(frame)
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()