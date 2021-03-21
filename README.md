# Python Webscraping App :




# deployment steps :
_______________________________
Create an app on Heroku with app name (in this case myscrappingapp)
 - myscrappingapp

Click on open app to see url of this project
(In this case myscrappingapp.herokuapp.com)

Go to project settings file inside scrapper/scrapper/settings.py
Then add Heroku given url in ALLOWED_HOSTS list

- ALLOWED_HOSTS=['myscrappingapp.herokuapp.com']

Open  deploy tab in Heroku , select deployment method as GitHub

Go to app connect to GitHub, search for repository
scrapper

Select the auto deployement.

At last select deploy branch button  in manual deploy section .

After successfull deployment open url to fetch details about equity bhav 
Using appropriate name.




#ERRORS
____________________________
if during deployment error occurs go to requirement.txt and try to change the version of module 
According to Heroku suggest.



#offline deployment
______________________________
Download the project using git command
 - git clone https://GitHub.com/VinayPundhir/scrapper

Install requirements.txt using command
    pip3 install -r requirements.txt

After successfull installation .
Add "127.0.0.1" in ALLOWED_HOSTS list in scrapper/scrapper/settings.py

Go to project root directory where manage.py exists
Open terminal run command
 - python3 manage.py runserver 

**Happy deploy**
 




 
