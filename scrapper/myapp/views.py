from django.shortcuts import render
import redis
import json
from django.http import JsonResponse ,HttpResponse
from .download_csv import update_redis_data
import csv

# Create your views here.

def home(req):
 return render(req,'home.html')


def connect_and_find(name):
 name=str(name).upper()
 res=None
 try:
  con=redis.Redis(host="redis-19501.c11.us-east-1-2.ec2.cloud.redislabs.com",
  port="19501",db=0,password="qhArklGwUoE0JAaGlVbccw4nIvR0L23u")
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
 if key=="jd83b*^$n{4)}>;gro67bjk:][49nv3&847vm@v94$kjrg49asgrf437op45nh":
  try:
   update_redis_data()
   return HttpResponse('done')
  except:
   return HttpResponse('not-done')
 else:
   return HttpResponse('not-done')
   
def remove_space(lst):
 lst=list(lst)
 for i,v in enumerate(lst):
  lst[i]=str(v).strip()

 return lst 


def download(req,name):
 data=connect_and_find(str(name))
 response=HttpResponse(content_type='text/csv')
 data=data["content"]
 writer=csv.writer(response)
 writer.writerow(remove_space(data.keys()))
 writer.writerow(remove_space(data.values()))
 response['Content-Disposition']='attachment; filename="results.csv"'
 return response
 return None
