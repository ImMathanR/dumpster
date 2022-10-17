import string
from typing import Union
from fastapi import FastAPI
from login import *

app = FastAPI()

@app.get("/")
def read_root():
    return "Server running successful"

@app.get("/login")
def login(totp: str):
    return doLogin(totp)