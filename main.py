import string
from turtle import ontimer
from typing import Union
from fastapi import FastAPI
from login import *
from historical import *
import os
from process import *

app = FastAPI()

load_dotenv()
apiKey = os.getenv("API_KEY")
historicalOutputDir = os.getenv("HISTORICAL_OUTPUT_DIR")
resultsOutputDir = os.getenv("RESULTS_OUTPUT_DIR")

@app.get("/")
def read_root():
    return "Server running successful"

@app.get("/login")
def login(totp: str):
    return doLogin(totp)

@app.get("/historical")
def historical():
    return getHistoricalData()

@app.get("/process")
def process():
    return processData()