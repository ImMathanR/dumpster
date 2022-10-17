# package import statement
from logging import error
from mimetypes import init
from smartapi import SmartConnect
from dotenv import load_dotenv
import os
from token_details import *

def doLogin(totp): 
    #create object of call
    load_dotenv()
    apiKey = os.getenv("API_KEY")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    obj=SmartConnect(api_key=apiKey)

    data = obj.generateSession(username,password,totp)
    if len(data['errorcode']) != 0:
        error(data['message'])
        return "Login failed: " + data['message']
    else:
        _bearerToken = data['data']['jwtToken']
        print("Token: ", _bearerToken)
        return "Login successful"