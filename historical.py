from importlib import import_module
from login import *
import token_details
import json
import pandas as pd
import main
import time

def getHistoricalData(): 
    #Historic api
    f = open("assets/historical_data_config.json")
    requestConfigs =  json.load(f)
    
    try:
        for config in requestConfigs:
            time.sleep(1)
            result = token_details._obj.getCandleData(config)
            if len(result['data']) > 0 :
                df = pd.DataFrame.from_dict(result['data'])
                fileName = config['name'] + "_" + config['interval'] + "_" + config['fromdate'][0:10] + "_" + config['todate'][0:10] + ".csv"
                outputFile = main.historicalOutputDir + "/" + fileName
                df.to_csv(outputFile, encoding='utf-8', index=False, header=False)
        return "Success"
    except Exception as e:
        print("Historic Api failed: {}".format(e.message))
        return "Failure: " + e
    
    