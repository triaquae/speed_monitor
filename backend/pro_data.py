# -*- coding: utf-8 -*- 
def city_handle(fname):
	pro_dic = {}
	with open(fname) as f:
		for line in f.readlines():
			line = line.split(',')	
			hour = line[1]
			province = line[5]
			city = line[3]
			onLoad = line[6]
			domReady = line[7]
			firstPaint = line[8]
			dnsLookup = line[9]
			firstByte = line[10]
			responseTime = line[11]
			pv = line[13]
def pro_handle(fname,pro_name):
	city_dic = {}
	f = file(fname)
	for line in f.readlines():
		line = line.split(',')
		hour = line[1]
		province = line[5]
		city = line[3]
		onLoad = line[6]
		domReady = line[7]
		firstPaint = line[8]
		dnsLookup = line[9]
		firstByte = line[10]
		responseTime = line[11]
		pv = line[13]
		standardDeviation = line[12]
		if not city_dic.has_key(city):
			city_dic[city] = [[hour,onLoad,domReady,firstPaint,dnsLookup,firstByte,responseTime,pv, standardDeviation ] ]
		else:
			city_dic[city].append(  [hour,onLoad,domReady,firstPaint,dnsLookup,firstByte,responseTime,pv, standardDeviation ])

	return city_dic

filename = '/home/alex/work_data/speed_monitor/backend/prov_raw.csv'
if __name__ == '__main__':
	
	print pro_handle(filename,'山东')

