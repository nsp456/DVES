import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\kjsce_comp164\AppData\Local\Tesseract-OCR\tesseract.exe'
try:
    from PIL import Image
except ImportError:
    import Image

def scan():
    result=pytesseract.image_to_string(Image.open('test.jpg'))
    text=""
    for i in result:
        if i not in ['?',' ','\n']:
            text+=i
            print(i,end='')
    return text
    





"""
    with open('abc.txt',mode ='a+') as file:      
          for i in text:
                file.write(i) 
                #print(result)
          file.write('\n')
"""
