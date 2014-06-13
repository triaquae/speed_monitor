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
def pro_handle(pro_name):
	print pro_name
	filename = '/home/alex/work_data/speed_monitor/backend/prov_raw.csv'
	city_dic = {}
	f = file(filename)
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
		if province == pro_name:
			if not city_dic.has_key(city):
				city_dic[city] = { 'summary':[ [hour,city,onLoad,standardDeviation,pv, domReady,firstPaint,dnsLookup,firstByte,responseTime ] ] }
			else:
				city_dic[city]['summary'].append(  [hour,city,onLoad,standardDeviation,pv, domReady,firstPaint,dnsLookup,firstByte,responseTime ])
	for k,v in city_dic.items():
		city_dic[k]['summary'] = v['summary'][-1] 
		#print k,v
	#print city_dic.items()
	sorted_dic = sorted(city_dic.items(), key= lambda x:int(x[1]['summary'][2])  )
	for i,v in  enumerate( sorted_dic ):
		city_dic[ v[0]]['summary'][0] = i
		print i, v[0], city_dic[v[0]] 
		
	print city_dic
	return city_dic


if __name__ == '__main__':
	
	pro_handle('山东')

