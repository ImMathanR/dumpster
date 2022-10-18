# package import statement
from logging import error
from mimetypes import init
from smartapi import SmartConnect
from dotenv import load_dotenv
import os
import token_details
import main

def doLogin(totp): 
    #create object of call
    
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    token_details._obj = SmartConnect(api_key=main.apiKey)

    data = token_details._obj.generateSession(username,password,totp)
    if len(data['errorcode']) != 0:
        error(data['message'])
        return "Login failed: " + data['message']
    else:
        _bearerToken = data['data']['jwtToken']
        print("Token: ", _bearerToken)
        return "Login successful"