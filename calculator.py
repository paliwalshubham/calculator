cal = Tk()
cal.title("calculator")
text_input =StringVar()
operator=""
display = Entry(cal,font = ('arial',20,'bold'),textvariable=text_input
                ,bd=30,insertwidth=4,bg = "powder blue",justify='right').grid(columnspan=4)
button7 = Button(cal,bd=8,font=('arial',20,'bold'),fg="black",bg = "powder blue",
                 text = "7",padx=16,command=lambda:btnclick(7)).grid(row=1,column=0)
button8 = Button(cal,bd=8,font=('arial',20,'bold'),fg="black",bg = "powder blue",
                 text = "8",padx=16,command=lambda:btnclick(8)).grid(row=1,column=1)
button9 = Button(cal,bd=8,font=('arial',20,'bold'),fg="black",bg = "powder blue",
                 text = "9",padx=16,command=lambda:btnclick(9)).grid(row=1,column=2)

buttonaddition = Button(cal,bd=8,font=('arial',20,'bold'),fg="black",bg = "powder blue",
                 text = "+",padx=16,command=lambda:btnclick("+")).grid(row=1,column=3)

button4 = Button(cal,bd=8,font=('arial',20,'bold'),fg="black",bg = "powder blue",
                 text = "4",padx=16,command=lambda:btnclick(4)).grid(row=2,column=0)
button5 = Button(cal,bd=8,font=('arial',20,'bold'),fg="black",bg = "powder blue",
                 text = "5",padx=16,command=lambda:btnclick(5)).grid(row=2,column=1)
button6 = Button(cal,bd=8,font=('arial',20,'bold'),fg="black",bg = "powder blue",
                 text = "6",padx=16,command=lambda:btnclick(6)).grid(row=2,column=2)

buttonsubtraction = Button(cal,bd=8,font=('arial',20,'bold'),fg="black",bg = "powder blue",
                 text = "-",padx=16,command=lambda:btnclick("-")).grid(row=2,column=3)

button1 = Button(cal,bd=8,font=('arial',20,'bold'),fg="black",bg = "powder blue",
                 text = "1",padx=16,command=lambda:btnclick(1)).grid(row=3,column=0)
button2 = Button(cal,bd=8,font=('arial',20,'bold'),fg="black",bg = "powder blue",
                 text = "2",padx=16,command=lambda:btnclick(2)).grid(row=3,column=1)
button3 = Button(cal,bd=8,font=('arial',20,'bold'),fg="black",bg = "powder blue",
                 text = "3",padx=16,command=lambda:btnclick(3)).grid(row=3,column=2)

buttonmultiplication = Button(cal,bd=8,font=('arial',20,'bold'),fg="black",bg = "powder blue",
                 text = "*",padx=16,command=lambda:btnclick("*")).grid(row=3,column=3)

button0 = Button(cal,bd=8,font=('arial',20,'bold'),fg="black",bg = "powder blue",
                 text = "0",padx=16,command=lambda:btnclick(0)).grid(row=4,column=0)

buttonclear = Button(cal,bd=8,font=('arial',20,'bold'),fg="black",bg = "powder blue",
                 text = "C",padx=16,command=clear).grid(row=4,column=1)
buttonequals = Button(cal,bd=8,font=('arial',20,'bold'),fg="black",bg = "powder blue",
                 text = "=",padx=16,command=equals).grid(row=4,column=2)
buttondivision = Button(cal,bd=8,font=('arial',20,'bold'),fg="black",bg = "powder blue",
                 text = "/",padx=16,command=lambda:btnclick("/")).grid(row=4,column=3)

cal.mainloop()