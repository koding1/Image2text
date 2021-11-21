import pyautogui
import clipboard
import mouse
import time
from PIL import ImageGrab
import ocr
import cv2
from functools import partial

def cap():
    img = ImageGrab.grab()
    opencv_image = ocr.convertImage(img)

    # Removes toolbar and status bar
    cv2.namedWindow('1',cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('1', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    cv2.imshow('1', opencv_image)

    while True:
        cv2.waitKey(50)
        if mouse.is_pressed("left"):
            x1, y1 = pyautogui.position() # +키를 순간 마우스의 좌표 저장
            cv2.circle(opencv_image, (x1, y1), 2, (0,0,255), -1)

            cv2.imshow('1', opencv_image)
            cv2.waitKey(1)
            
            time.sleep(0.1)

            while True: 
                
                if mouse.is_pressed("left"):

                    x2, y2 = pyautogui.position()

                    print("두 위치 : ({}, {}), ({}, {})".format(x1,y1,x2,y2))

                    sorted_x_value = sorted([x1, x2])
                    sorted_y_value = sorted([y1, y2])
                    width = sorted_x_value[1] - sorted_x_value[0]
                    height = sorted_y_value[1] - sorted_y_value[0]

                    x_re = sorted_x_value[0] - 20
                    y_re = sorted_y_value[0] - 20
                    width_re = width + 40
                    height_re = height + 40

                    print("영역 : ({}, {}, {}, {})\n".format(x_re, y_re, width_re, height_re))
                    clipboard.copy("({}, {}, {}, {})".format(x_re, y_re, width_re, height_re))

                    pyautogui.screenshot('tmp.png', region=(sorted_x_value[0], sorted_y_value[0], width, height))
                    
                    cv2.destroyWindow('1')

                    break
            break
