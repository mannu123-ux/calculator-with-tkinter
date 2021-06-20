from tkinter import*


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(l.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        l.update()

    elif text == "C":
        scvalue.set("")
        l.update()

    else:
        scvalue.set(scvalue.get() + text)
        l.update()

window=Tk()
window.geometry("240x400")
window.title("Calculator")
fram=Frame(window ,background="black",borderwidth=2,relief=SUNKEN)
 
b1=Button(fram,text='#' )
b1.pack(side=LEFT)
b1.config(height=2,width=7)
b1.bind("<Button-1>",click)

b2=Button(fram,text='0')
b2.pack(side=LEFT)
b2.config(height=2,width=7)
b2.bind("<Button-1>",click)

b3=Button(fram,text='.')
b3.pack(side=LEFT)
b3.config(height=2,width=7)
b3.bind("<Button-1>",click)

b4=Button(fram,text='=')
b4.pack(side=LEFT)
b4.config(height=2,width=7)
b4.bind("<Button-1>",click)
fram.pack(side=BOTTOM,fill='x')



fram2=Frame(window, borderwidth=2,relief=SUNKEN,background="black")
 
b1=Button(fram2,text='1')
b1.pack(side=LEFT)
b1.config(height=2,width=7)
b1.bind("<Button-1>",click)

b2=Button(fram2,text='2')
b2.pack(side=LEFT)
b2.config(height=2,width=7)
b2.bind("<Button-1>",click)

b3=Button(fram2,text='3')
b3.pack(side=LEFT)
b3.config(height=2,width=7)
b3.bind("<Button-1>",click)

b4=Button(fram2,text='+')
b4.pack(side=LEFT)
b4.config(height=2,width=7)
b4.bind("<Button-1>",click)
fram2.pack(side=BOTTOM,fill='x')


fram3=Frame(window, borderwidth=2,relief=SUNKEN,background="black")
 
b1=Button(fram3,text='4')
b1.pack(side=LEFT)
b1.config(height=2,width=7)
b1.bind("<Button-1>",click)

b2=Button(fram3,text='5')
b2.pack(side=LEFT)
b2.config(height=2,width=7)
b2.bind("<Button-1>",click)

b3=Button(fram3,text='6')
b3.pack(side=LEFT)
b3.config(height=2,width=7)
b3.bind("<Button-1>",click)

b4=Button(fram3,text='-')
b4.pack(side=LEFT)
b4.config(height=2,width=7)
b4.bind("<Button-1>",click)
fram3.pack(side=BOTTOM,fill='x')


fram4=Frame(window, borderwidth=2,relief=SUNKEN,background="black")
 
b1=Button(fram4,text='7')
b1.pack(side=LEFT)
b1.config(height=2,width=7)
b1.bind("<Button-1>",click)

b2=Button(fram4,text='8')
b2.pack(side=LEFT)
b2.config(height=2,width=7)
b2.bind("<Button-1>",click)

b3=Button(fram4,text='9')
b3.pack(side=LEFT)
b3.config(height=2,width=7)
b3.bind("<Button-1>",click)

b4=Button(fram4,text='*')
b4.pack(side=LEFT)
b4.config(height=2,width=7)
b4.bind("<Button-1>",click)
fram4.pack(side=BOTTOM,fill='x')

fram5=Frame(window, borderwidth=2,relief=SUNKEN,background="black")
 
b1=Button(fram5,text='C')
b1.pack(side=LEFT)
b1.config(height=2,width=7)
b1.bind("<Button-1>",click)

b2=Button(fram5,text='**')
b2.pack(side=LEFT)
b2.config(height=2,width=7)
b2.bind("<Button-1>",click)

b3=Button(fram5,text='%')
b3.pack(side=LEFT)
b3.config(height=2,width=7)
b3.bind("<Button-1>",click)

b4=Button(fram5,text='/')
b4.pack(side=LEFT)
b4.config(height=2,width=7)
b4.bind("<Button-1>",click)
fram5.pack(side=BOTTOM,fill='x')


scvalue=StringVar()
scvalue.set("")
fram6=Frame(window,borderwidth=2,relief=SUNKEN)
fram6.pack(side=BOTTOM,fill='x')
l= Entry(fram6, textvar=scvalue)
l.pack(fill='x')
