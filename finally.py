'''
from tkinter import *  # 注意模块导入方式，否则代码会有差别
import os

def xunlian():
    os.system('python test2.py')

def huoqu():
    os.system('python run.py')

def jiance():
    os.system('python do')


master = Tk()

# Button是一种按钮组件，与Label类似，只是多出了响应点击的功能

xunlian1=Button(master, text="训练",command=xunlian,).pack(side=TOP, anchor=W, fill=X, expand=YES)
huoqu1=Button(master, text="获取",command=huoqu).pack(side=TOP, anchor=W, fill=X, expand=YES)
jiance1=Button(master, text="检测",command=jiance).pack(side=TOP, anchor=W, fill=X, expand=YES)
# xunlian1.pack(side=LEFT, fill=BOTH, expand=YES)
# huoqu1.pack(side=LEFT, fill=BOTH, expand=YES)
# jiance1.pack(side=LEFT, fill=BOTH, expand=YES)

    # fm2 = master
    # Button(fm2, text='Left').pack(side=LEFT)
    # Button(fm2, text='This is the Center button').pack(side=LEFT)
    # Button(fm2, text='Right').pack(side=LEFT)
    # fm2.pack(side=LEFT, padx=10)

mainloop()
'''
# -*- coding:utf-8 -*-
from tkinter import *
from PIL import Image, ImageTk
import threading
import imageio
import imutils
import time
import cv2
import os

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, bg='black')
        self.pack(expand=YES, fill=BOTH)
        self.window_init()
        self.createWidgets()

    def window_init(self):
        self.master.title('welcome to video-captioning system')
        self.master.bg = 'black'
        width, height = self.master.maxsize()
        self.master.geometry("{}x{}".format(width, height))

    def createWidgets(self):
        # fm1
        self.fm1 = Frame(self, bg='black')
        self.titleLabel = Label(self.fm1, text="课堂点名签到系统", font=('微软雅黑', 64), fg="white", bg='black')
        self.titleLabel.pack()
        self.fm1.pack(side=TOP, expand=YES, fill='x', pady=20)

        # fm2
        self.fm2 = Frame(self, bg='black')
        self.fm2_left = Frame(self.fm2, bg='black')
        self.fm2_right = Frame(self.fm2, bg='black')
        self.fm2_left_top = Frame(self.fm2_left, bg='black')
        self.fm2_left_bottom = Frame(self.fm2_left, bg='black')
        self.fm2_left_medium = Frame(self.fm2_left, bg='black')
        self.fm2_left_test2 = Frame(self.fm2_left, bg='black')
        self.fm2_left_txt = Frame(self.fm2_left, bg='black')
        # ------------------------------------------------------------------------------------------#
        self.predictEntry = Button(self.fm2_left_top, text='按Q停止',font=('微软雅黑', 36), width='16', bg='#FF4081', fg='white')
        self.predictButton = Button(self.fm2_left_top, text='开始点名', bg='#FF4081', fg='white',
                                    font=('微软雅黑', 36), width='16', command=self.output_predict_sentence)
        self.predictButton.pack(side=LEFT)
        self.predictEntry.pack(side=LEFT, fill='y', padx=20)
        self.fm2_left_top.pack(side=TOP, fill='x')
        # ------------------------------------------------------------------------------------------#
        self.xunliananniu = Button(self.fm2_left_top, text='收集信息', bg='#FF4081', fg='white',
                                    font=('微软雅黑', 36), width='16', command=self.xunlian)
        self.xunliananniu.pack(side=LEFT)
        self.fm2_left_medium.pack(side=LEFT, fill='y',padx=20)
        # ------------------------------------------------------------------------------------------#
        self.ceshitubiao = Entry(self.fm2_left_bottom, font=('微软雅黑', 24), width='20', fg='#22C9C9')
        self.ceshianniu = Button(self.fm2_left_bottom, text='开始训练', bg='#22C9C9', fg='white',
                                  font=('微软雅黑', 36), width='16', command=self.ceshi)
        self.ceshianniu.pack(side=LEFT)
        self.ceshitubiao.pack(side=LEFT, fill='y', padx=20)
        self.fm2_left_test2.pack(side=TOP, pady=10, fill='x')
        #------------------------------------------------------------------------------------------#
        self.truthEntry = Entry(self.fm2_left_txt, font=('微软雅黑', 24), width='72', fg='#22C9C9')
        self.truthButton = Button(self.fm2_left_bottom, text='查看缺勤学生', bg='#22C9C9', fg='white',
                                  font=('微软雅黑', 36), width='16', command=self.output_ground_truth)
        self.truthButton.pack(side=LEFT)
        self.truthEntry.pack(side=LEFT, fill='y', padx=20)
        self.fm2_left_bottom.pack(side=TOP, pady=10, fill='x')
        self.fm2_left_txt.pack(side=LEFT, pady=20, fill='y')
        # ------------------------------------------------------------------------------------------#
        self.fm2_left.pack(side=LEFT, padx=60, pady=20, expand=YES, fill='x')
        self.nextVideoImg = ImageTk.PhotoImage(file='./01.jpg')

        self.nextVideoButton = Button(self.fm2_right, image=self.nextVideoImg, text='next video', bg='black',
                                      command=self.start_play_video_thread)
        self.nextVideoButton.pack(expand=YES, fill=BOTH)
        self.fm2_right.pack(side=BOTTOM, padx=10)
        self.fm2.pack(side=TOP, expand=YES, fill="x")

        # fm3
        self.fm3 = Frame(self, bg='black')
        load = Image.open('./01.jpg')
        initIamge = ImageTk.PhotoImage(load)
        self.panel = Label(self.fm3, image=initIamge)
        self.panel.image = initIamge
        self.panel.pack()
        self.fm3.pack(side=TOP, expand=YES, fill=BOTH, pady=10)

    def output_predict_sentence(self):
        os.system('python do.py')
        # predicted_sentence_str = 'hello world.'
        # self.predictEntry.delete(0, END)
        # self.predictEntry.insert(0, predicted_sentence_str)

    def xunlian(self):

        os.system('python run.py')

    def ceshi(self):
        os.system('python test2.py')
        predicted_sentence_str = '模型训练完成'
        self.ceshitubiao.delete(0, END)
        self.ceshitubiao.insert(0,predicted_sentence_str)

    def output_ground_truth(self):
        os.system('python different.py')
        rea = open('baidu.txt','r')
        ream = rea.readlines()
        ground_truth = ream
        self.truthEntry.delete(0, END)
        self.truthEntry.insert(0, ground_truth)

    def start_play_video_thread(self):
        self.thread = threading.Thread(target=self.play_next_video, args=())
        self.thread.start()

    def play_next_video(self):
        self.predictEntry.delete(0, END)
        self.truthEntry.delete(0, END)

        # to play video
        self.video_path = './01.jpg'
        self.video = imageio.get_reader(self.video_path, 'ffmpeg')
        for self.videoFrame in self.video:
            self.videoFrame = imutils.resize(self.videoFrame, width=1760, height=1080)  # to do
            self.image = cv2.cvtColor(self.videoFrame, cv2.COLOR_BGR2RGB)
            self.image = Image.fromarray(self.image)
            self.image = ImageTk.PhotoImage(self.image)

            self.panel.configure(image=self.image)
            self.panel.image = self.image

            time.sleep(0.02)


if __name__ == '__main__':
    app = Application()
    # to do
    app.mainloop()

