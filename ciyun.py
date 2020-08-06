import requests
import json
url = "https://api.yimian.xyz/coro/"
data = requests.get(url).text
city_dict = {}
json_data = json.loads(data)
for p in json_data:
    if 'cities' in p:
        for c in p["cities"]:
            city_name = c['cityName']
            cCount = c['confirmedCount']
            sCount = c['suspectedCount']
            total = int(cCount) + int(sCount)
            city_dict[city_name] = total
    else:
        city_name = p['provinceName']
        cCount = p['confirmedCount']
        sCount = p['suspectedCount']
        total = int(cCount) + int(sCount)
        city_dict[city_name] = total
with open('全球新冠疫情感染人数.txt', 'w') as f:
    for k,v in city_dict.items():
        f.write(f"{k}:{v}人\n")
