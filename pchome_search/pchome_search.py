import requests
import json
import prettytable
import os

keyword= input("請輸入關鍵字: ")
os.system("cls")

k_page= 1
while keyword != "":
	r = requests.get(
		"https://ecshweb.pchome.com.tw/search/v3.3/all/results",
		params = {
			"q":keyword,
			"page":k_page,
			"sort":"sale/dc"
		},
		headers = {
			"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
			"Cookie": "_ga=GA1.1.1354779466.1602567773; _gid=GA1.3.604366636.1602567773; uuid=xxx-d981807f-537c-43b0-acbb-6eda0e29368d; puuid=K.20201013134257.12; _pafp=13af2ba8dbd23eb6e2c4ccdcb83719b2; _pafp_t=1602567783; ECC=669aa2b06aa1b28f57df32eb8253bfeda28d55f1.1602567820; _gcl_au=1.1.597299999.1602567827; _ga_9CE1X6J1FG=GS1.1.1602567826.1.1.1602570373.0; gsite=24h; venguid=a849c7f5-f72f-4ff5-8c7e-af4a4ef7328e.wg1-1n4020201013; vensession=3072c088-e7f3-4cc1-9ea5-8b4715c38196.wg1-36wz20201013.se; _fbp=fb.2.1602567841088.218592001; U=333ec112a406787f89eee4331e78b33fd50c6466; ECWEBSESS=e2d4b5a51d.4dbd3bda708bc3e6d46e8cc2515efb27465b4ddb.1602567845; HistoryEC=%7B%22P%22%3A%5B%7B%22Id%22%3A%22DXAO43-A900A0GJP%22%2C%20%22M%22%3A1602569055%7D%5D%2C%20%22T%22%3A1%7D; _gat_UA-115564493-1=1"
		}
	)
	# print(r.text)
	
	data = json.loads(r.text)
	# print(data)

	p = prettytable.PrettyTable(["名稱", "價格"], encoding="utf8")
	p.align["名稱"]="l"
	p.align["價格"]="l"
		
	for d in data['prods']:
		p.add_row([d['name'], d['price']])
	print(p)

	k_page= input("前往頁碼: ")
	os.system("cls")

