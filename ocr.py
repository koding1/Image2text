import cv2
import os
import numpy as np
import clipboard 
import time

def convertImage(img):
        numpy_image=np.array(img) # 1. PIL Image를 np array로 변환
        opencv_image=cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR) # 2. np array를 cv2로 변환
        return opencv_image

def ocr():
    try: 
        from PIL import Image
    except ImportError:
        import Image

    import pytesseract

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' # 테서렉트 설치 경로

    img = Image.open(r'C:\Users\jhj76\Vsprojects\Image2text\tmp.png') # OCR 할 이미지
    print("img 불러오기 완료")
    # convert PIL Image to cv2

    opencv_image = convertImage(img)

    cv2.imshow('test', opencv_image)

    ocr_string = pytesseract.image_to_string(opencv_image) # ocr한 문자열을 저장
    ocr_string =ocr_string[:-1]
    clipboard.copy(ocr_string) # 클립보드에 복사

    # for debug ------
    print(ocr_string)
    # ----------------

    cv2.setWindowProperty('test', cv2.WND_PROP_TOPMOST, 1) # 최상위
    cv2.waitKey(1800)
    cv2.destroyWindow('test')

