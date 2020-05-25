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
    input_img = cv.imread('test.jpg',1)
  
    result=pytesseract.image_to_string(input_img)
        
    text=""
    for i in result:
        if i not in ['?',' ','\n']:
            text+=i
            print(i,end='')
    return text
    

#uncomment below line to test run this code before finally running with main GUI Program
#scan()

