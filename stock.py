#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stock.py
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
import sqlite3
class stock():
        def __init__(self, id, StockSym, NoShares, CurrentPrice, PurchasePrice, Date):
                self.id=id
                self.StockSym = StockSym
                self.NoShares = NoShares
                self.CurrentPrice = CurrentPrice
                self.PurchasePrice= PurchasePrice
                self.Date = Date

                      
        def earningsFunction(x, y, z):
                a=float(x)
                b=float(y)
                c=int(z)
                earnings=(a - b)*c
                return(earnings)
	
        def percent(a,b, diff):
                diffDays=int(diff)
                x=float(a)
                y=float(b)
                result=((((x-y)/y)/(diffDays)))*100
                return(result)


class bond(stock):
        def __init__(self, id, StockSym, NoShares, CurrentPrice, PurchasePrice, Coupon, Yield, Date):
                self.id=id
                self.StockSym = StockSym
                self.NoShares = NoShares
                self.CurrentPrice = CurrentPrice
                self.PurchasePrice= PurchasePrice
                self.Date = Date
                self.Coupon=Coupon
                self.Yield=Yield
                

