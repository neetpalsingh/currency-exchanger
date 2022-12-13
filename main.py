## real time currency exchanger project with tkinter in python
## Developers Name: Neetpal Singh 
def res():
    from forex_python.converter import CurrencyRates
    c=CurrencyRates()
    amount=int(amt.get())
    from_currency=f_currency.get().upper()
    to_currency=t_currency.get().upper()

    result=c.convert(from_currency,to_currency,amount)
    output.config(text=result)

import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Neetpal Singh")
root.geometry("600x500")



s=tk.Scrollbar(root)
s.pack(side="right",fill=tk.Y)

#icon
image_icon=tk.PhotoImage(file="neet.png")
root.iconphoto(False,image_icon)


pic=tk.PhotoImage(file="neet.png")
tk.Label(root,image=pic).place(x=50,y=500)
tk.Label(root,text="Developer: Neetpal Singh",fg="blue",font=("Times",10)).place(x=200,y=585)
tk.Label(root,text="E mail   : neetpalsingh750@gmail.com",fg="blue",font=("Times",10)).place(x=200,y=600)
tk.Label(root,text="contact  : +917505687812",fg="blue",font=("Times",10)).place(x=200,y=615)

photo=tk.PhotoImage(file="img.png")
tk.Label(root,image=photo).place(x=600,y=70)

tk.Label(root,text="World Wide Currency Exchanger",fg="red",font=("Times",15)).place(x=130,y=50)

tk.Label(root,text="Amount:",fg="black",font=("Times",15)).place(x=50,y=150)
amt=tk.Entry(root,width=20,fg="blue",font=("Calbari",14),border="5")
amt.place(x=180,y=150)
tk.Label(root,text="From Currency:",fg="black",font=("Times",15)).place(x=50,y=200)
f_currency=tk.Entry(root,width=20,fg="blue",font=("Calbari",14),border="5")
f_currency.place(x=180,y=200)
tk.Label(root,text="To Currency:",fg="black",font=("Times",15)).place(x=50,y=250)
t_currency=tk.Entry(root,width=20,fg="blue",font=("Calbari",14),border="5")
t_currency.place(x=180,y=250)
b=tk.Button(root,text="Get Amount",width=10,bg="orange",fg="black",font=("Calibri",15),command=res)
b.place(x=190,y=330)
result_label=tk.Label(root,text="Output:",width=20,fg="blue",font=("Calbari",14))
result_label.place(x=20,y=420)
output=tk.Label(root,width=20,fg="green",font=("Calbari",14))
output.place(x=180,y=420)
root.mainloop()