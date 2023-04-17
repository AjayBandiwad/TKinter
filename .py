import tkinter as Aj
m = Aj.Tk()
m.title('count seconds')
label1 = Aj.Label(m,text="username")
Label2 = Aj.Label(m,text="passward")
button = Aj.Button(m,text="submit")

text1 = Aj.Entry(m)
text2 = Aj.Entry(m)
label1.grid(row=0,column=0)
Label2.grid(row=1,column=0)
button.grid(row=2,column=1)
text1.grid(row=0,column=1)
text2.grid(row=1,column=1)





m.mainloop()