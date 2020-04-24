import pytesseract
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
try:
    from PIL import Image
except ImportError:
    import Image

def scan():
    cap = cv2.VideoCapture(0)
    while True:
        _,im=cap.read(0)
    ##    kernel = np.ones((5,5),np.uint8)
    ##    im2=cv2.morphologyEx(im, cv2.MORPH_CLOSE, kernel)
        imgray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        _ , th=cv2.threshold(imgray,90,255,cv2.THRESH_BINARY)
    ##    cv2.imshow('sd1',im)

#         cv2.imshow('sd',im)

        # converts the image to result and saves it into result variable 
        result = pytesseract.image_to_string(th)
#         print(result)
        if len(result)==10 or (cv2.waitKey(1) & 0xFF ==ord('q')):
            break    
    cap.release()
    cv2.destroyAllWindows()
    return result

    


#scan()

