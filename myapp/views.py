from django.shortcuts import render
import redis
import json
from django.http import JsonResponse ,HttpResponse
from .download_csv import update_redis_data
import csv

#importing ProjConfig
from django.conf import settings as ds
HOST=ds.RHOST
DB=ds.RDB
PASSWORD=ds.RPASSWORD
PORT=ds.RPORT 
REDIS_KEY=ds.RKEY


# Create your views here.


def home(req):
 return render(req,'home.html')


def connect_and_find(name):
 name=str(name).upper()
 res=None
 try:
  con=redis.Redis(host=HOST,port=PORT,db=DB,password=PASSWORD)
  if con.exists(name):
   res={'status':200,'content':json.loads(con.get(name).decode('UTF-8'))}
  else:
   res={'status':404}
 except:
  res={'status':503}
 
 return res


def search(req,name):
 res=connect_and_find(name)
 return JsonResponse({'response':res})


def download_today_data(req,key):
 print(key,'your sent')
 if key==REDIS_KEY:
  try:
   update_redis_data()
   return JsonResponse({'response':'updated successfully'})
  except:
   return JsonResponse({'response':"could not update"})
 else:
   return JsonResponse({'response':'wrong key passed'})
   
def remove_space(lst):
 lst=list(lst)
 for i,v in enumerate(lst):
  lst[i]=str(v).strip()

 return lst 


def download(req,name):
 data=connect_and_find(str(name))
 if data['status']==200:
  response=HttpResponse(content_type='text/csv')
  data=data["content"]
  writer=csv.writer(response)
  writer.writerow(remove_space(data.keys()))
  writer.writerow(remove_space(data.values()))
  response['Content-Disposition']='attachment; filename="results.csv"'
  return response
 else:
  return JsonResponse({'response':data})


