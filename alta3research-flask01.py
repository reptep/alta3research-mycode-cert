#!/usr/bin/python3

'''
Your script alta3research-flask01.py should demonstrate proficiency with the flask library. Ensure your application has at least two endpoints. At least one of your endpoints should return legal JSON.
'''
# An object of Flask class is our WSGI application
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import make_response

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function

t_dict = { 'First Name' : 'Inigo', 'Last Name' : 'Montoya' , 'Quote' : 'Hello. My name is Inigo Montoya. You killed my father. Prepare to die.' }

def setcookie(i_resp, i_cnt):
    # Add a cookie to our response object
    i_resp.set_cookie("visit_cnt", i_cnt)

    # return our response object includes our cookie
    return i_resp

def getcookie():
   # attempt to read the value of userID from user cookie
   t_visit_cnt = request.cookies.get("visit_cnt") # preferred method
   
   if t_visit_cnt is None:
       t_visit_cnt = 0

   return str (t_visit_cnt)

def updtcookie():
   t_cnt = int (getcookie()) 
   t_cnt = t_cnt + 1    

   return str (t_cnt)

# Endpoint 1:
@app.route("/endpoint_1")
@app.route("/")
def endpoint_1():
   t_cnt = updtcookie()

   t_resp = make_response (render_template ("endpoint_1.html", i_quote = t_dict["Quote"], i_cnt = t_cnt))
   t_resp = setcookie(t_resp, t_cnt)

   return t_resp

# Endpoint 2:
@app.route("/endpoint_2")
def endpoint_2():
   return jsonify(t_dict)

if __name__ == "__main__":
   # runs the application
   app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
