import json
from urllib.request import urlopen
url = "https://api.gcore.com/cdn/public-ip-list"
response = urlopen(url)
data = json.loads(response.read())
array = []
array6 = []
for i in data['addresses']:
    array.append(i)
f_path = (r"ip.txt")
with open (f_path ,'w') as d:
       for lang in array:
        d.write("{}\n".format(lang))
for j in data['addresses_v6']:
    array6.append(j)
v_path = (r"ipv6.txt")    
with open (v_path ,'w') as c:
       for lang in array6:
        c.write("{}\n".format(lang))    
response.close()
