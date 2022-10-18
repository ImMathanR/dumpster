import time
from datetime import datetime
import pandas as pd
import os
import main

def processData():
    # CSV to DataFrame
    dirList = os.listdir(main.historicalOutputDir)
    for dir in dirList:
        processStock(main.historicalOutputDir + "/" + dir)
    

def processStock(fileName: str):
    df = pd.read_csv(fileName, header=None)
    date_price_list: list = df.values.tolist()

    outputText = ""

    # date_price_list.reverse()

    BUYING_MARGIN = 0.99
    SELLING_MARGIN = 1.01
    UNITS = 150
    equity_margin = 100000
    NIFTY_BEES_LTP = df.iloc[0,1]
    
    orders = {}
    order_id = 0

    for date_prices in date_price_list:
        date = date_prices[0]

        prices = [date_prices[1], date_prices[4]]
        for price in prices:
            NIFTY_BEES_CTP = price
            if NIFTY_BEES_CTP <= (NIFTY_BEES_LTP * BUYING_MARGIN):
                if UNITS * NIFTY_BEES_CTP <= equity_margin:
                    equity_margin = equity_margin - (UNITS * NIFTY_BEES_CTP)

                    order_id = order_id + 1
                    orders[order_id] = {
                        "buy_date": date,
                        "buy_price": NIFTY_BEES_CTP,
                        "sell_price": NIFTY_BEES_CTP * SELLING_MARGIN,
                        "sold": False
                    }

            for id, order in orders.items():
                if order["sold"] is False and NIFTY_BEES_CTP >= order["sell_price"]:
                    equity_margin = equity_margin + (NIFTY_BEES_CTP * UNITS)

                    order["sold"] = True
                    order["sell_date"] = date
                    orders[id] = order

            NIFTY_BEES_LTP = NIFTY_BEES_CTP

        invested = 0
        for oid, order in orders.items():
            if order["sold"] is False:
                invested = invested + NIFTY_BEES_CTP * UNITS
            if order['buy_date'] == date:
                outputText += (f"\nOrderId: {oid} Order Details: {order}")
            if 'sell_date' in order and order['sell_date'] == date and order['sell_date'] != order['buy_date']:
                outputText += (f"\nOrderId: {oid} Order Details: {order}")
                
        outputText += (f"\ndate: {date}, equity_margin: {equity_margin}, invested: {invested}, ctp: {NIFTY_BEES_CTP}")
        outputText += (f"\nEquity margin: {equity_margin}")
        outputText += (f"\nAmount invested: {invested}")
        writeToFile(os.path.basename(fileName), outputText)


def writeToFile(fileName: str, outputText: str):
    outputPath = main.resultsOutputDir + "/" + fileName[:-4] + ".txt"
    f = open(outputPath, "w")
    f.write(outputText)
    f.close()