# milestone1-kflowers9
# API Access#
1)For API access to Spotify:

-Create a .env file in your root directory, and create a variable named (exactly) "CLIENT_ID" and "CLIENT_SECRET"
-Go to Spotify Devlopers page, login, and create your app with Spotify and put your client ID and Secret from the dashboard into your .env file for each variable respectively. 
-REMEMBER!: Put .env file under your .gitignore file 

2) For API access to Genius 
- Do the same thing for Genius you did for spotify, but instead just follow the instructions on the website in order to get an access token with your CLIENT_ID/CLIENT_SECRET. Since Genius ddoesn't require much for Apps that don't reach an endpoint that looks at User information, we will be using the link that generates an access token for us. This token lasts forever, so we can put that in our GACCESS_TOKEN section in  our .env variable. 

# What to do to get started#
1) Install all requiremeents in the requirement.txt file onto a virtual environment, so that program can run the functions
2) Clone the repo to a local machine and set the port to 5000 so that it can runn locally

# Technical Problems #

1) Recieving authorization for Spotify. I just created a way to constantly create a new access token since Access Tokens only lasted about an hour after they were created. 

2) Going through the JSON data and searching for specific information. i just did a ferw google searches and I was able to figure out the fast and most efficient way to comb through the JSON format of information we recieved. 

# Problems left to be fixed#

1) Searching for the exact song everytime we use the Genius link. The problem is, the Song ID on Spotify is different from the ID in Genius, so there has to be a way to search specifically for the song with out the occassional mis information from showing. 

# heroku link#
https://appp1m1.herokuapp.com/