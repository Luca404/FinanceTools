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

#Global Variables
pfName = ""
pfTickers = ""

def getPfData(e):
    savedPfMenu = document.getElementById("savedPfMenu")
    pfOptions = savedPfMenu.getElementsByTagName("option")
    strPf = pfOptions[savedPfMenu.selectedIndex].text
    pfName = strPf.split(": ")[0]
    pfTickers = strPf.split(": ")[1]
    pass
    

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


#Set a proxy for change in the portfolio dropdown menu
selectPfProxy = create_proxy(getPfData)
selectPf = document.getElementById("savedPfMenu")
selectPf.addEventListener("change", selectPfProxy)

getPfData("pollo")

