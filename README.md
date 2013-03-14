WebPython_FinalProject
======================

Final Project for Internet Programming with Python
Pho Diep (March 2013)

Link to deployed app:
http://block647046-fpb.blueboxgrid.com


Link to Github:
https://github.com/phodiep/WebPython_FinalProject.git

Goal:
My final project was meant to be an expansion of the mashup we prepared in class using web scrapping techniques and other web api's available. The original mashup was that of craigslist apartment listing with restaurants nearby. The goal of my final project was to deploy that mashup to a working site.

Outcome:
Successfully deployed the site on the VM, with the app written using Bottle. The decision to use bottle in place of some of the other frameworks introduced in class was due to the fact that the site does not save any user information, therefore no database needed. Each visit to the site is a fresh query. The final mashup was that of Craislist apartment listings (with latitude and longitude information provided) with google street view api. I was hoping to include an interactive street view directly from the deployed site, however google only provides a static image of the street view with their api. Therefore to get around this, I embedded a link to the google street view url to the static image provided. I had previously tried to deploy the app on Heroku, however Craigslist has blocked Heroku from it's servers.

Instructions to run Locally:
1. setup virtualenv with the following installed: beautifulsoup4, bottle, oauth2
2. download project from github
3. activate virtualenv and navigate to project folder
4. run $ python CLapp.py
5. in browser, load http://localhost:8080


