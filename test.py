from time import sleep
import pyautogui
from PIL import ImageGrab, Image
import time
a=time.time()
#事先对按钮截图
Img1= Image.open("1.PNG")
Img2= Image.open("2.PNG")
Img3= Image.open("3.PNG")
Img4= Image.open("4.PNG")
Img5= Image.open("5.PNG")
Img6= Image.open("6.PNG")
Img7= Image.open("7.PNG")
Img8= Image.open("8.PNG")
Img9= Image.open("9.PNG")
Img10= Image.open("10.PNG")
#截图当前屏幕并找到之前加载的按钮截图
while True:
    msg = pyautogui.locateOnScreen(Img1, grayscale=True,confidence=.9)
    if msg==None: 
        print ("没找到")
    else:
        x,y,width,height=msg
        print ("该图标在屏幕中的位置是：X={},Y={}，宽{}像素,高{}像素".format(x,y,width,height))
        #左键点击屏幕上的这个位置
        pyautogui.click(x,y,button='left')

    msg = pyautogui.locateOnScreen(Img2, grayscale=True,confidence=.9)
    if msg==None: 
        print ("没找到")
    else:
        x,y,width,height=msg
        print ("该图标在屏幕中的位置是：X={},Y={}，宽{}像素,高{}像素".format(x,y,width,height))
        #左键点击屏幕上的这个位置
        pyautogui.click(x,y,button='left')

    msg = pyautogui.locateOnScreen(Img3, grayscale=True,confidence=.9)
    if msg==None: 
        print ("没找到")
    else:
        x,y,width,height=msg
        print ("该图标在屏幕中的位置是：X={},Y={}，宽{}像素,高{}像素".format(x,y,width,height))
        #左键点击屏幕上的这个位置
        pyautogui.click(x,y,button='left')

    msg = pyautogui.locateOnScreen(Img4, grayscale=True,confidence=.9)
    if msg==None: 
        print ("没找到")
    else:
        x,y,width,height=msg
        print ("该图标在屏幕中的位置是：X={},Y={}，宽{}像素,高{}像素".format(x,y,width,height))
        #左键点击屏幕上的这个位置
        pyautogui.click(x,y,button='left')

    msg = pyautogui.locateOnScreen(Img5, grayscale=True,confidence=.9)
    if msg==None: 
        print ("没找到")
    else:
        x,y,width,height=msg
        print ("该图标在屏幕中的位置是：X={},Y={}，宽{}像素,高{}像素".format(x,y,width,height))
        #左键点击屏幕上的这个位置
        pyautogui.click(x,y,button='left')

    msg = pyautogui.locateOnScreen(Img6, grayscale=True,confidence=.9)
    if msg==None: 
        print ("没找到")
    else:
        x,y,width,height=msg
        print ("该图标在屏幕中的位置是：X={},Y={}，宽{}像素,高{}像素".format(x,y,width,height))
        #左键点击屏幕上的这个位置
        pyautogui.click(x,y,button='left')

    msg = pyautogui.locateOnScreen(Img7, grayscale=True,confidence=.9)
    if msg==None: 
        print ("没找到")
    else:
        x,y,width,height=msg
        print ("该图标在屏幕中的位置是：X={},Y={}，宽{}像素,高{}像素".format(x,y,width,height))
        #左键点击屏幕上的这个位置
        pyautogui.click(x,y,button='left')
    msg = pyautogui.locateOnScreen(Img8, grayscale=True,confidence=.9)
    if msg==None: 
        print ("没找到")
    else:
        x,y,width,height=msg
        print ("该图标在屏幕中的位置是：X={},Y={}，宽{}像素,高{}像素".format(x,y,width,height))
        #左键点击屏幕上的这个位置
        pyautogui.click(x,y,button='left')
    print('已用',time.time()-a,'秒')
    time.sleep(1)
