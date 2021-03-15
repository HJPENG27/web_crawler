import requests
from bs4 import BeautifulSoup
import prettytable

r = requests.post(
	# "https://www.cwb.gov.tw/V8/C/W/County_TempTop.html", 
	"https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html?",
	# params= {"ID":"Wed Oct 14 2020 15:24:37 GMT 0800 (台北標準時間)"}, 
	# 有的設定日期後的結果不受影響, 是因為避免大量使用網路去抓資源, 避免用到緩存資料.
	headers = {
		"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
		"Cookie": "TS010c55bd=0107dddfef5917bb8be0644f8cbefa499f98bd91d026fff18e83edd16a048d5b4e47586a1c17a2b6b9de00551dbda5c1c3aa24abf7; TS558d33eb027=08dc4bbcbbab20000455c98f3eb2407bc3dbc1929a4d61d71811091615c4f7939d37828968d5edc10813ee45a2113000a08e5b7524a95a9fe802cbe0ecc4231cab784e66a84c5fdb086853d77fe468db08cd3298e182eaa5f56107fc6381e637; _ga=GA1.3.1318229044.1602653264; _gid=GA1.3.12234599.1602653264"
		}
	)

b = BeautifulSoup(r.text, "html.parser")
all_info = b.find_all("tr") ## <tr> 各地氣溫地點所在地等等的所有資訊List, 然後再往下一層找

p = prettytable.PrettyTable(["地區", "氣溫"], encoding="utf8")
p.align["地區"]="c" # 預設就是置中 "c"
p.align["氣溫"]="c"

for i in all_info:
	location = i.find("th")
	temp = i.find("span") # 或是可以這樣作: temp=i.find_all("span")  --> temp[0].text
	# print(location.text, temp[0].text) #--> 印出地區與溫度, 但沒有在表裡, 少了中括號[].
	p.add_row([location.text, temp.text])
print(p)
	 








