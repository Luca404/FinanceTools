import json
import os
import asyncio
import pandas
from js import document
from pyodide import create_proxy
#from pandas_datareader import data as wb
from pyodide.http import pyfetch
#import requests
#import mysql.connector

async def loadJson():
    response = await pyfetch(url="./json/portfolios.json", method="GET")
    output = await response.json()
    out = str(output)
    validOut = out.replace("\'", "\"")
    console.log( validOut )				
    pfList = json.loads( validOut )
    return pfList
    

def checkTickerYahoo(event):
    text = document.getElementById("pfInputTicker").value
    if(text[-1] == ","):
        document.getElementById("pfInputTicker").setAttribute("disabled", True)
        document.getElementById("loaderIcon").style.display = "block"
        ticker = text.split(",")[0]
        data = wb.DataReader(ticker, data_source="yahoo")
        console.log(data)
        
    #data = wb.DataReader(ticker, data_source="yahoo")
    #console.log(data)

async def checkTickerYahoo1(event):
    text = document.getElementById("pfInputTicker").value
    if(text[-1] == ","):
        document.getElementById("pfInputTicker").setAttribute("disabled", True)
        document.getElementById("loaderIcon").style.display = "block"
        ticker = text.split(",")[0]
        apiKey = "GBD72Q8YTW5QIDIN"
        url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + ticker + '&apikey=' + apiKey
        response = await pyfetch(
            url,
            method="GET"
        )
        out = await response.json()
        try:        
            tickerName = out["Name"]
            
            console.log(tickerName)
        except:
            console.log("Ticker not found")
            document.getElementById("pfInputTicker").removeAttribute("disabled")
            document.getElementById("loaderIcon").style.display = "none"
            document.getElementById("pfInputTicker").value = ""
        
    #data = wb.DataReader(ticker, data_source="yahoo")
    #console.log(data)

#inputTickerProxy = create_proxy(checkTickerYahoo1)
#inputTicker = document.getElementById("pfInputTicker")
#inputTicker.addEventListener("input", inputTickerProxy)

