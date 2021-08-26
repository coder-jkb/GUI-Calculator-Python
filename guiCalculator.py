from tkinter import *
root=Tk()
exp_s=""
exp_l=[]
k=-1
e=Entry(root,width=21,font=('Verdana',16))
def click(number):
 e.insert(y,number)
def AC():
 e.delete(0,END)
def bksp():
 if str(e.get()) != "Error":
  e.delete(len(str(e.get()))-1,END)
 else:
  AC()
def equal():
 expression=str(e.get())
 e.delete(0,END)
 try:
  for i in range(len(expression)):
    if expression[i] =="^":
     expression=expression[:i]+"**"+expression[i+1:]
    elif expression[i] =="x":
     expression=expression[:i]+"*"+expression[i+1:]   
  ans=eval(expression)
  e.insert(y,ans)
 except:
  e.insert(0,"Error")
def exit():
 quit()
#insertbentry wiget
e. grid(row=0,column=0,columnspan=3)
#create and insert buttons
x=100
y=25
b1=Button(root,padx=x,pady=y,text=1,font=('Verdana',16),command=lambda:click(1)).grid(row=1,column=0)
b2=Button(root,text=2,font=('Verdana',16), padx=x,pady=y,command=lambda:click(2)).grid(row=1,column=1)
b3=Button(root,text=3,font=('Verdana',16), padx=x,pady=y,command=lambda:click(3) ).grid(row=1,column=2)
b4=Button(root,text=4,font=('Verdana',16), padx=x,pady=y,command=lambda:click(4) ).grid(row=2,column=0)
b5=Button(root,text=5,font=('Verdana',16), padx=x,pady=y,command=lambda:click(5)).grid(row=2,column=1)
b6=Button(root,text=6,font=('Verdana',16), padx=x,pady=y,command=lambda:click(6)).grid(row=2,column=2)
b7=Button(root,text=7,font=('Verdana',16), padx=x,pady=y,command=lambda:click(7) ).grid(row=3,column=0)
b8=Button(root,text=8,font=('Verdana',16), padx=x,pady=y,command=lambda:click(8) ).grid(row=3,column=1)
b9=Button(root,text=9 ,font=('Verdana',16), padx=x,pady=y,command=lambda:click(9)).grid(row=3,column=2)
b0=Button(root,text=0 ,font=('Verdana',16), padx=x,pady=y,command=lambda:click(0)).grid(row=4,column=1)
b_decimal=Button(root,text="." ,font=('Verdana',20), padx=x,pady=y,command=lambda:click(".")).grid(row=4,column=0)
b_equal=Button(root,text="=" ,font=('Verdana',16), padx=x,pady=y,command=equal).grid(row=4,column=2)
b_add=Button(root,text="+" ,font=('Verdana',16), padx=x,pady=y,command=lambda:click("+")).grid(row=5,column=0)
b_sub=Button(root,text="-" ,font=('Verdana',16), padx=x,pady=y,command=lambda:click("-")).grid(row=5,column=1)
b_mult=Button(root,text="x" ,font=('Verdana',16), padx=x,pady=y,command=lambda:click("x")).grid(row=5,column=2)
b_div=Button(root,text="/" ,font=('Verdana',16), padx=x,pady=y,command=lambda:click("/")).grid(row=6,column=0)
b_powr=Button(root,text="^" ,font=('Verdana',16), padx=x,pady=y,command=lambda:click("^")).grid(row=6,column=1)
b_bksp=Button(root,text="<-" ,font=('Verdana',16), padx=x,pady=y,command=bksp).grid(row=6,column=2)
b_powr=Button(root,text="AC" ,font=('Verdana',16), padx=x,pady=y,command=AC).grid(row=7,column=2)
b_brac_open=Button(root,text="(" ,font=('Verdana',16), padx=x,pady=y,command=lambda:click("(")).grid(row=7,column=0)
b_brac_close=Button(root,text=")" ,font=('Verdana',16), padx=x,pady=y,command=lambda:click(")")).grid(row=7,column=1)
b_exit=Button(root,text="\nEXIT\n",font=('Verdana',16), command=exit).grid(row=8,column=1,pady=20)
root.mainloop()