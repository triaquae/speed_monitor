import scipy,math

s1 = [5,6,8,9]
s2 = [0,5,9,14]
s3 = [6,7,8,7]


def get_standard_devi(source_list):
	get_avg = scipy.mean(source_list)
	print 'avg:', get_avg
	temp_total = 0
	for n in source_list:
		temp_total += (n - get_avg)**2
	return  math.sqrt(temp_total/len(source_list))

print  get_standard_devi(s1)
print  get_standard_devi(s2)
print  get_standard_devi(s3)
