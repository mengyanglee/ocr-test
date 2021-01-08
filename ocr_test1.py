import requests
import json
url = 'http://localhost:8089/api/tr-run/'
img1_file = {
    'file': open('image.jpg', 'rb')
}
res = requests.post(url=url, data={'compress': 0}, files=img1_file)
#resout= json.loads(res.text)

fileObject = open('data.json', 'w')
fileObject.write(res.text)
fileObject.close()