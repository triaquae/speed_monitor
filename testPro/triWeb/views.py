# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
import redis_connector,json,pickle
import sample_highstock_data 
import pro_data

def login(request):
	return render_to_response('login.html')

def login_auth(request):
	print request.POST
	username,password = request.POST.get('email'), request.POST.get('password')
	user = auth.authenticate(username = username , password = password)
	print '++++++', user
	if user is not None: #means authentications is correct
		auth.login(request, user)
		return HttpResponseRedirect('/')
	else:
		return render_to_response('login.html',{'login_err':"Wrong user name or password!"})
		

	return HttpResponse( request.POST )

def logout(request):
	c_user = request.user
	auth.logout(request)
	return HttpResponse("user %s has logged out, please <a href='/login/'>click to re_login</a>" % c_user)


@login_required
def index(request):
        return render_to_response('index.html')
		#return render_to_response('howto-4.html')

def performance_test(request):
        #return render_to_response('index.html')
        
		return render_to_response('simple_code.html')

@login_required
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

def getCityList(request):
	print request.GET
	city_list = {
		#ranking   avg_log  standard_deviation   pv 
		'QingDao': {'summary': [1,u'青岛', 7845, 32.332, 498533  ],
			    'trend' : ['some data'] },
                'YanTai': {'summary': [3, u'烟台',532, 3.92, 563487  ],
                            'trend' : ['some data'] },
	}
	city_name = request.GET.get('cityName')	
	print '_____________________________'
	city_list =  pro_data.pro_handle(city_name.encode('utf8') )
	return HttpResponse( json.dumps(city_list ))

def stock(request):
	print request.POST,'*'*40
	graph_name = request.POST.get('name')
	if graph_name == 'page_load_trend':
		g_title = "全国用户平均加载速度趋势"
	elif graph_name == 'bw_type_trend':
		g_title = "加载速度by浏览器维度"
	return render_to_response('highstock_basic.html',
		{ 'graph_title': g_title }

	)
def getReport(request):
	data_set= request.GET.get('key_name')
	stock_data = sample_highstock_data.data_gen()
	
	return HttpResponse( json.dumps( stock_data[data_set] ) )
