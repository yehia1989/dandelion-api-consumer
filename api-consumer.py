import json
import urllib2

# change this url to 
API_KEY = "YOUR_API"
# change this url to filter 
url = "https://api.dandelion.eu/datagems/v2/SpazioDati/milanotoday/data?$offset=0&$app_id=%s&$app_key=%s" % (API_KEY,API_KEY)

response = urllib2.urlopen(url);
json_response = json.load( response )


items = json_response['items']
rows = []
for item in items:
	row = ""
	row += (u'%s\t' % (item['title']))
	row += (u'%s\t' % (item['link']))
	row += (u'%s\t' % (item['model']))
	row += (u'%s\t' % (item['topic']))
	row += (u'%s\t' % (item['date']))
	row += (u'%s\t' % (item['timestamp']))
	row += (u'%s\t' % (item['municipality']['acheneID']))
	row += (u'%s\t' % (item['municipality']['name']))
	row += (u'%s\t' % (item['address']))
	row += (u'%s\t' % (item['location']))
	row += (u'%s\t' % (item['geometry']['type'] if(item['geometry']) else ""))
	row += (u'%s\t' % (item['geometry']['coordinates'][0] if(item['geometry']) else "-1")	)
	row += (u'%s' % (item['geometry']['coordinates'][1] if(item['geometry']) else "-1")	)

	e = row.encode('utf-8')
	rows.append(e)


f = open('news.csv','w+')
f.write("\n".join(rows))
f.close()
