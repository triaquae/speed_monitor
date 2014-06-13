import random

def data_gen():
	data_dic = { 'onLoad': [],
		'domReady': [],
		'dnsLookup': [],
		'firstPaint': [],
		'firstByte': [],
		'responseTime': []
	}

	time_start = 1400950861
	time_end = 1402554844
	for i in range(500): #500hours
		for k,v in data_dic.items():
			if k =='onLoad':data_range = random.randrange(6000,10000)
			elif k =='domReady':data_range = random.randrange(4000,6000)
			elif k =='firstPaint':data_range = random.randrange(3400,4000)
			elif k =='firstByte':data_range = random.randrange(2000,3500)
			elif k =='responseTime':data_range = random.randrange(1500,2000)
			elif k == 'dnsLookup':data_range = random.randrange(1500)
			data_dic[k].append( [ (time_start+3600)*1000,data_range ]  )
		time_start +=3600

	return data_dic
	"""print "#"*60
	for k,v in  data_dic.items():
		print k,v
	"""


if __name__ == '__main__':
	print data_gen()
