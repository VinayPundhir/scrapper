# Python/Django Webscraping App 
( Latest Stock Market Equity information )

Live @ https://myscrappingapp.herokuapp.com




# Api
_________________________________________________
replace COMPANY_NAME with the name you search

get json response

- https://myscrappingapp.herokuapp.com/name/COMPANY_NAME

get csv file of equity result

- https://myscrappingapp.herokuapp.com/download/COMPANY_NAME

api to manually update the redis with new data

- https://myscrappingapp.herokuapp.com/update/APIKEY

 


# Deployment Steps 
_______________________________

Create a Redis account on https://Redislabs.com or somewhere else.

write the redis account credentials inside settings.py file @ scrapper/scrapper/settings.py

Create an app on Heroku with app name (in this case myscrappingapp)
 
- myscrappingapp

Click on open app to see url of this project (In this case myscrappingapp.herokuapp.com)

Go to project settings file inside scrapper/scrapper/settings.py then add Heroku given url in ALLOWED_HOSTS list

- ALLOWED_HOSTS=['myscrappingapp.herokuapp.com']


Open  deploy tab in Heroku , select deployment method as GitHub

Go to app connect to GitHub, search for repository 
 
- scrapper

Select the auto deployement.

At last select deploy branch button  in manual deploy section .

After successfull deployment open url to fetch details about equity bhav 

- Using appropriate name.

Get a cronjob account somewhere eg. https://cron-job.org

which sould point to update api 

- https://myscrappingapp.herokuapp.com/update/APIKEY

replace APIKEY with orginal key placed in project file scrapper/settings.py

- RKEY

if cronjob is created on the same hosting plateform then uncomment
worker in Procfile and set schedule time in update.py.


# Errors
____________________________

if during deployment error occurs go to requirement.txt and try to change the version of module  According to Heroku suggest.





# Offline Deployment
______________________________
Download the project using git command
 
- git clone https://GitHub.com/VinayPundhir/scrapper

Install requirements.txt using command
 
- pip3 install -r requirements.txt



After successfull installation .

Add "127.0.0.1" in ALLOWED_HOSTS list in scrapper/scrapper/settings.py

Go to project root directory where manage.py exists

Open terminal run command
 
- python3 manage.py runserver 







 
