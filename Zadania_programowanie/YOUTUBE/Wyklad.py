import requests
url="https://danepubliczne.imgw.pl/api/data/synop/format/csv"
req=requests.get(url)
all_data=req.content
all_data=all_data.splitlines()
for r in range(0,len(all_data)):
    print(all_data[r])


