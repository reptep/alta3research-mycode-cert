#!/usr/bin/python3

'''
Your script alta3research-requests02.py should demonstrate proficiency with the requests HTTP library. The API you target is up to you, but be sure any data that is returned is "normalized" into a format that is easy for users to understand.
'''
# An object of Flask class is our WSGI application
from flask import Flask
from flask import render_template

import requests
import time

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function

NASAAPI = "https://api.nasa.gov/planetary/apod?"

# this function grabs our credentials
def returncreds():
    try:
        ## first I want to grab my credentials
        with open("/home/student/nasa.creds", "r") as mycreds:
            nasacreds = mycreds.read()
    except:
        ## In case there is no file
        nasacreds = "DEMO_KEY"

    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
   
    return nasacreds

# Endpoint 1:
@app.route("/")
def apod():
    ## first grab credentials
    t_nasacreds = returncreds()

    is_200 = False
    t_cnt = 0

    while (not is_200) and (t_cnt) < 5:
        ## make a call to NASAAPI with our key
        t_apodresp = requests.get(NASAAPI + t_nasacreds + '&count=1')

        if t_apodresp.status_code == 200:
            is_200 = True
        
        time.sleep (5)
        t_cnt = t_cnt + 1

    if is_200:
        ## strip off json
        t_apod = t_apodresp.json()

        return (render_template ("apod.html", i_apod = t_apod))
    else:
        return ("Error accessing Astronomy Picture of the Day (APOD) microservice. Please try again later!")

if __name__ == "__main__":
    # runs the application
    app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
