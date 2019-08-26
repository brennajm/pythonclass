#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  assignment8.py
#  
#  Copyright 2019 Brenna Meade <brennameade@Brennas-MacBook-Pro.local>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from datetime import datetime
from stock import *
from investor import *
import json
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

workspace = r'/Users/brennameade/Desktop/'
json_file = workspace + 'AllStocks.json'

with open(json_file) as f:
	dataSet = json.load(f)
	
#print(dataSet)
id=1
YAxis=[]
XAxis=[]
	
for stockInfo in dataSet:
	Date = (stockInfo['Date'])
	StockSym=(stockInfo['Symbol'])
	PP=(stockInfo['Open'])
	CP=(stockInfo['Close'])
	NoShares=(stockInfo['Volume'])
	stocks=stock(id,StockSym, NoShares,CP,PP,Date)
	graph=(stocks.Date, stocks.CurrentPrice)
	YAxis.append(stocks.CurrentPrice)
	XAxis.append(stocks.Date)
	id=id+1
	
	
fig, ax = plt.subplots()

#ax.plot(['01/01/01', '01/01/02', '01/01/0/3'],[12,13,14])
ax.plot(XAxis,YAxis)
ax.set(xlabel='Date(s)', ylabel='Close Price',
       title='Current Price Over Time')
ax.grid()

fig.savefig("test.png")
plt.show()

	
	
