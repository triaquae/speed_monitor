
log = 'raw_log'

with open(log) as f:
  print "date, t_done, t_page,t_js, response_time , dom_ready"
  for line in f: 
    line = line.split()
    date,hour, t_done, t_page, t_js, response_time, dom_ready, first_paint, dns_time, first_byte, nav_type = line[0],line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10]
    print date, 't_done:',t_done, 't_page:', t_page, 't_js:',t_js, 'response_time:',response_time , 'dom_ready',dom_ready, 'firstPaint:', first_paint, 'dns:',dns_time, 'first_byte:', first_byte, 'nav_type:',nav_type


