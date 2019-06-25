'''
import cv2
img1 =cv2.imread("./4.jpg")
face = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
#图片的灰度
gray = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
#检查人脸
faces = face.detectMultiScale(gray)
for(x,y,w,h) in faces:
    #1.标记图片2.人脸左上角的坐标原点3.标记的图案大小4.颜色值5.线宽
    cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),10)
cv2.namedWindow("many faces")
cv2.imshow("face1",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
import cv2
face = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
#打开摄像头
capture = cv2.VideoCapture(0)
#创建窗口
cv2.namedWindow("camera")
while True:
#     #读取摄像头的每一帧画面，会返回两个值，ret会返回两个情况False,True,frame是当前截取的一帧的图片
    ret, frame = capture.read()
    #取图片的灰度（性能提高）
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # # #检查人脸（优化（100,100）， （20,20））
    faces = face.detectMultiScale(gray, 1.1, 3, 0, (20,20))
    # #标记人脸
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    #     #显示图片
        cv2.imshow("camera", frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
#释放资源
capture.release()
# 销毁窗口
cv2.destroyAllWindows()
'''
'''
# -*- coding: utf-8 -*-
#实际运行最终版本
import cv2
import sys
import gc
from face_train import Model

if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage:%s camera_id\r\n" % (sys.argv[0]))
        sys.exit(0)

    # 加载模型
    model = Model()
    model.load_model(file_path='./model/liziqiang.face.model.h5')

    # 框住人脸的矩形边框颜色
    color = (0, 255, 0)

    # 捕获指定摄像头的实时视频流
    cap = cv2.VideoCapture(0)

    # 人脸识别分类器本地存储路径
    cascade_path = 'haarcascade_frontalface_alt.xml'

    # 循环检测识别人脸
    while True:
        ret, frame = cap.read()  # 读取一帧视频

        if ret is True:

            # 图像灰化，降低计算复杂度
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            continue
        # 使用人脸识别分类器，读入分类器
        cascade = cv2.CascadeClassifier(cascade_path)

        # 利用分类器识别出哪个区域为人脸
        faceRects = cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(faceRects) > 0:
            for faceRect in faceRects:
                x, y, w, h = faceRect

                # 截取脸部图像提交给模型识别这是谁
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                faceID = model.face_predict(image)

                # 如果是“我”
                if faceID == 0:
                    cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, thickness=2)

                    # 文字提示是谁
                    cv2.putText(frame, '20150181113',
                                (x + 30, y + 30),  # 坐标
                                cv2.FONT_HERSHEY_SIMPLEX,  # 字体
                                1,  # 字号
                                (255, 0, 255),  # 颜色
                                2)  # 字的线宽
                else:
                    pass

        cv2.imshow("识别", frame)

        # 等待10毫秒看是否有按键输入
        k = cv2.waitKey(10)
        # 如果输入q则退出循环
        if k & 0xFF == ord('q'):
            break

    # 释放摄像头并销毁所有窗口
    cap.release()
'''

#用来截获人脸获取照片
import cv2
import sys
import tkinter.messagebox
from tkinter import *
from PIL import Image
import os
a = input('输入学生学号:')
os.mkdir('./data/'+a)
def CatchPICFromVideo(window_name, camera_idx, catch_pic_num, path_name):
    cv2.namedWindow(window_name)

    # 视频来源，可以来自一段已存好的视频，也可以直接来自USB摄像头
    cap = cv2.VideoCapture(camera_idx)

    # 告诉OpenCV使用人脸识别分类器
    classfier = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')

    # 识别出人脸后要画的边框的颜色，RGB格式
    color = (0, 255, 0)

    num = 0
    while cap.isOpened():
        ok, frame = cap.read()  # 读取一帧数据
        if not ok:
            break

        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将当前桢图像转换成灰度图像

        # 人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(faceRects) > 0:  # 大于0则检测到人脸
            for faceRect in faceRects:  # 单独框出每一张人脸
                x, y, w, h = faceRect

                # 将当前帧保存为图片
                img_name = '%s/%d.jpg' % (path_name, num)
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                cv2.imwrite(img_name, image)
                catch_pic_num = 255
                num += 1
                if num > (catch_pic_num):  # 如果超过指定最大保存数量退出循环
                    break

                # 画出矩形框
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)

                # 显示当前捕捉到了多少人脸图片了
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, 'num:%d' % (num), (x + 30, y + 30), font, 1, (255, 0, 255), 4)

                # 超过指定最大保存数量结束程序
        if num > (catch_pic_num): break

        # 显示图像
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break

            # 释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    CatchPICFromVideo('get face', 0, 1000, './data/'+a)
