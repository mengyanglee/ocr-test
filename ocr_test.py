
import pytesseract
from PIL import Image
img = Image.open('image.jpg')
pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
s = pytesseract.image_to_string(img, lang='chi_sim')  #不加lang参数的话，默认进行英文识别
print(s)
# image = Image.open('image.jpg')
# content = pytesseract.image_to_string(image)  # 解析图片
# print(content)