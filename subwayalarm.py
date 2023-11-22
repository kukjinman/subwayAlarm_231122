import xml.etree.ElementTree as ET
import requests

from lineMessage import lineMessage

seoulsubwayapikey = "684469536a74686136336364556f68"
station = "강남"
url = f"http://swopenAPI.seoul.go.kr/api/subway/{seoulsubwayapikey}/xml/realtimeStationArrival/0/5/{station}"

data = requests.get(url)
print(data.text)

root = ET.fromstring(data.text)
rows = root.findall('.//row')


list = ""

for row in rows:
    updnLine = row.find('updnLine').text
    trainLineNm = row.find('trainLineNm').text
    arvlMsg2 = row.find('arvlMsg2').text
    list += f"\n방향: {updnLine}\n전철방향: {trainLineNm}\n도착시간: {arvlMsg2}\n"
    list += "---------------------------"

print(list)

lineMessage(list)