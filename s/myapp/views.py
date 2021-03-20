from django.shortcuts import render
import redis
import json
from django.http import JsonResponse
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
