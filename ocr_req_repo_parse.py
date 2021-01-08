import requests
import re
import json


def download_ocr(url, img1_file):
    data = requests.post(url=url, data={'compress': 0}, files=img1_file)
    return data.text


def parse_data(f):
    # print(f, type(f))
    data = json.loads(f)
    res = data.get('data').get('raw_out')
    str_out = ''
    for i in res:
        str_out += i[1].strip() + '\n'
    print(str_out)
    ret_data = re.sub(' ', '', str_out)
    return ret_data


if __name__ == '__main__':
    # 'image.jpg'
    image = input('请输入文件名称，之后命令行显示出图片中的文字\n')
    url = 'http://localhost:8089/api/tr-run/'
    img1_file = {
        'file': open(image, 'rb')
    }
    data = download_ocr(url, img1_file)
    resdata = parse_data(data)
