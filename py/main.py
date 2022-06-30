import json
import os
import asyncio
from pyodide.http import pyfetch
#import mysql.connector

async def loadJson():
    response = await pyfetch(url="./json/portfolios.json", method="GET")
    output = await response.json()
    out = str(output)
    validOut = out.replace("\'", "\"")
    console.log( validOut )				
    pfList = json.loads( validOut )
    return pfList
    

async def fillTablePfManager():
    pfList = await loadJson()
    tbody = document.getElementById("tbody1")
    i = 0
    for pf in pfList["PortFolios"]:
        tr = document.createElement("tr")
        td1 = document.createElement("td")
        td1.appendChild(document.createTextNode(str(pf["pfName"])))
        tr.appendChild(td1)
        td2 = document.createElement("td")
        td2.appendChild(document.createTextNode(str(pf["tickers"])))
        tr.appendChild(td2)

        td3 = document.createElement("td")
        button = document.createElement("button")
        button.appendChild(document.createTextNode("Modify"))
        button.id = "modifyPf"
        button.className = "btn btn-dark"
        button.type = "button"
        td3.appendChild(button)
        
        tr.appendChild(td3)

        
        tbody.insertBefore( tr, tbody.lastElementChild );
        i += 1

#fillTablePfManager()