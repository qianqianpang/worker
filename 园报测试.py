import hashlib
import random
import string
import time
import requests

AppId = "meinenghua"
AccessToken = "D315F2FE554D459A91DAA3E54A1ABA3F"
Timestamp = int(round(time.time() * 1000))
seeds = string.digits
random_str = []
for i in range(4):
    random_str.append(random.choice(seeds))
str1 = ''.join(random_str)
Nonce = str(Timestamp)
Nonce += str1
ieFlag = "E"
billNo = "PASU515808982002"

params = {
    "AccessToken": AccessToken,
    "AppId": AppId,
    "billNo": billNo,
    "ieFlag": ieFlag,
    "Nonce": Nonce,
    "Timestamp": Timestamp,
}
signStr = ''
for key, value in params.items():
    signStr += key
    signStr += str(value)

print(signStr)
Signature = hashlib.md5(signStr.encode('utf8')).hexdigest()

url = f'https://xapi.mingboerp.com/api/manifest/subscribe?AppId={AppId}&Timestamp={Timestamp}&Nonce={Nonce}&Signature={Signature}&ieFlag={ieFlag}&billNo={billNo}'
print(url)
payload = {}
headers = {
    'Cookie': 'SERVERID=668f5b848990323a38d0a1b7baab3106|1676443278|1676443278'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
