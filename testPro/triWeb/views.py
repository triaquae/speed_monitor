from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
# Create your views here.
import redis_connector,json,pickle





def index(request):
        return render_to_response('index.html')
		#return render_to_response('howto-4.html')

def performance_test(request):
        #return render_to_response('index.html')
        
		return render_to_response('simple_code.html')
def dashboard(request):
	return render_to_response('dashboard.html')
def assets(request):
	return render_to_response('assets.html')

def squid_summary(request):
	squid_data = pickle.loads( redis_connector.r['SquidLog::localhost'])
	print squid_data['by_url']	
	return render_to_response('squid_summary.html',{'top_url': squid_data['by_url'] })
	#return render_to_response('test.html',{'top_url': a})

def graph(request):
	return render_to_response('highchart.html')
def get_squid_data(request):
	print request.GET
	squid_data = pickle.loads( redis_connector.r['SquidLog::localhost'])
	#print squid_data['by_hour']
	return HttpResponse(   json.dumps(squid_data) )
#--------------

def  collect_user_data(request):
	for k,v in  request.GET.items():
		print '\033[42;1m%s\033[0m' %k, v
	#print request.MIME
	print '*'*80
	return HttpResponse('done')	


def convert_to_float(status):
        status_list = [float(x ) for x in status[1:]]
	status_list.insert(0,int(status[0])  * 1000 )
	return status_list




def getStatusData(request):
	status_data = json.loads(redis_connector.r.get('STATUS_DATA::localhost'))
	data_list=map(convert_to_float, status_data['memory']['Actual'][4:])
	return HttpResponse(json.dumps(  data_list))



def stock(request):
	return render_to_response('highstock_basic.html')
