import requests 
from bs4 import BeautifulSoup as bs
import pandas as pd
import redis
import json

"""
#download zip file

headers={
  "User-Agent" : "Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0",
  "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language" : "en-US,en;q=0.5"
 }

req=requests.Session()
req.headers.update(headers)

res=req.get("https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx")



#pass zip file in beautifulsoup

parsed=bs(res.content,"html.parser")

csv_data=None

for tag in parsed.find_all('a'):
 if tag.get('id') == 'ContentPlaceHolder1_btnhylZip':
   csv_data=req.get(tag.get('href')).content




# save downloaded zip file

if csv_data!=None:
 f=open('bhavcopy.zip','wb')
 f.write(csv_data)
 f.close()



"""
#read zip file using pandas

from_zip=pd.read_csv('bhavcopy.zip',compression='zip')
"""
SC_CODE = from_zip['SC_CODE']
SC_NAME = from_zip['SC_NAME']
SC_GROUP= from_zip['SC_GROUP']
SC_TYPE = from_zip['SC_TYPE']                          
OPEN = from_zip['OPEN']
HIGH= from_zip['HIGH']
LOW= from_zip['LOW']
CLOSE = from_zip['CLOSE']
LAST= from_zip['LAST']
PREVCLOSE = from_zip['PREVCLOSE']
NO_TRADES= from_zip['NO_TRADES']
NO_OF_SHRS = from_zip[ 'NO_OF_SHRS']
NET_TURNOV= from_zip['NET_TURNOV']
TDCLOINDI=from_zip['TDCLOINDI']"""

cols=[list(from_zip[i]) for i in from_zip.columns]

rows=len(cols[0])

#uploading data to redis
count=1

try:
 print('trying to connect...')
 con=redis.Redis(host="redis-19501.c11.us-east-1-2.ec2.cloud.redislabs.com",port="19501",db=0,password="qhArklGwUoE0JAaGlVbccw4nIvR0L23u")
 print('connection established')
 con.flushall()

 print('trying to upload...')

 for c,n,g,t,o,h,l,cl,lst,pc,nt,ns,nt,tdc in zip(cols[0],cols[1],cols[2],cols[3],
 cols[4],cols[5],cols[6],cols[7],
 cols[8],cols[9],cols[10],cols[11],
 cols[12],cols[13]):
  
     
  row={'code':str(c),'name':str(n),'group':str(g),
  'type':str(t),'open':str(o),'high':str(h),
  'low':str(l),'close':str(cl),'last':str(lst),
  'prevclose':str(pc),'trades':str(nt),
  'shares':str(ns),'turnover':str(nt),
  'tdcloindi':str(tdc)}
  
  row=json.dumps(row).encode('UTF-8')
  con.set(str(n).strip(),row)
  print(count,'row uploaded')
  count+=1 
 print('done uploading')
except:
 print('error occured')
 con.flushall()
 print('data removed')


