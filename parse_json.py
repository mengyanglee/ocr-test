import json
import re
with open('data.json','r') as f:
    data= json.load(f)
res=data.get('data').get('raw_out')
str_out=''
for i in res:
    str_out += i[1].strip()+'\n'
print(str_out)
print(re.sub(' ','',str_out))
