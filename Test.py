from typing import Text
from tkinter import *
import pandas as pd
import tkinter as tk

# โปรแกรมนี้เมื่อทำการรัน จะให้ใส่รหัสสินค้าซึ่งอยู่ใน excel
# แล้วทำการตรวจสอบราคาสินค้าของทั้งราคาเก่าและราคาใหม่ใน excel
# และแสดงผลออกมาพร้อมบอกว่าราคาเท่ากัน,ถูกกว่าหรือแพงกว่าราคาเก่า

#  อ่าน excel
Newstore = pd.read_excel (r'New.xlsx')
Oldstore = pd.read_excel (r'Old.xlsx')
# print (Newstore)               # แสดงทั้งหมด
# print (Newstore['รหัสสินค้า'])   # แสดง เป็นแถวตามหัวเรื่อง
# print(Newstore.columns)       # แสดง หัวเรื่องเท่านั้น
# print(Newstore.iloc[1,1])     # row/column

# user input
while True:
    while True:
        try:
            print("โปรดใส่รหัสสินค้า:")
            input_a = input()
            input_a = int(input_a)
    
            break
        except ValueError : #ValueError IndexError
            print ("โปรดใส่รหัสสินค้าเป็นตัวเลขรหัส")

    try:
        resultNew = Newstore[Newstore["รหัสสินค้า"] == input_a ]
        resultOld = Oldstore[Oldstore["รหัสสินค้า"] == input_a ]
        idNew = resultNew["รหัสสินค้า"]
        intidNew = int(idNew)

        break
    except  : 
        print ("โปรดใส่รหัสสินค้าให้ถูกต้องตามที่มีอยู่")
         

# แสดงรายการของรหัสสินค้านั้นๆใน cmd
# resultNew = Newstore[Newstore["รหัสสินค้า"] == input_a ]
# resultOld = Oldstore[Oldstore["รหัสสินค้า"] == input_a ]

# ดึงมาแต่ค่าต่างๆของสินค้านั้นๆ
idNew = resultNew["รหัสสินค้า"]
idOld = resultOld["รหัสสินค้า"]


nameNew = resultNew["ชื่อสินค้า"]
# nameOld = resultOld["ชื่อสินค้า"]

priceNew = resultNew["ราคา"]
priceOld = resultOld["ราคา"]

quantityNew = resultNew["จำนวน"]
# quantityOld = resultOld["จำนวน"]

# intidNew = int(idNew)
tuplenameNew = tuple(nameNew)
intquantityNew = int(quantityNew)
intpriceNew = int(priceNew)
intpriceold =int(priceOld)

# เปรียบเทียบราคาจากทั้ง 2 ตาราง
if intpriceNew > intpriceold:   
    state = "มีราคามากกว่าราคาเก่า"
elif intpriceNew < intpriceold:   
    state = "มีราคาน้อยกว่าราคาเก่า"
else:
    state = " มีราคาเท่ากันกับราคาเก่า"

# หน้าต่างแสดงผล 
window = tk.Tk()  
window.option_add("*Font" , "consolas 18")
window.title("เปรียบเทียบราคาสินค้า")
tk.Label(text="เปรียบเทียบราคาสินค้า").grid()
tk.Label(text=resultNew).grid()
# tk.Label(text=intidNew ).grid()
# tk.Label(text=tuplenameNew).grid()    
# tk.Label(text=intpriceNew).grid()
# tk.Label(text=intquantityNew).grid()
tk.Label(text=state).grid()

window.mainloop()