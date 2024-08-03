from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text== "=":
            if scvalue.get().isdigit():
                value= int(scvalue.get())
            else:
                try:
                    value= eval(screen.get())
                    
                except Exception as e:
                    value="Error"
                
                
            scvalue.set(value)
            screen.update()
    elif text== "AC":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+ text)
        screen.update()

root=Tk()
root.geometry("300x500")
root.maxsize(400,500)
root.title("Calculator")
root.wm_iconbitmap("calc.ico")
root.config(bg="black")

# values k liye entry bar
scvalue= StringVar()
scvalue.set("")
screen= Entry(root, textvar= scvalue, font=" lucida 20 bold")
screen.pack(fill=X, ipadx=8, padx=10, pady=8)

# frame for digits-->
f1= Frame(root, bg="grey")
b1= Button(f1, text="AC", font="lucida 19 bold", padx=5, pady=4, bg="red")
b1.pack(side=LEFT, padx=9, pady=4)
b1.bind('<Button-1>', click)

b1= Button(f1, text="*", font="lucida 17 bold", padx=15, pady=8, bg="orange")
b1.pack(side=LEFT, padx=10, pady=4)
b1.bind('<Button-1>', click)

b1= Button(f1, text="/", font="lucida 17 bold", padx=15, pady=8, bg="orange")

b1.pack(side=LEFT, padx=10, pady=4)
b1.bind('<Button-1>', click)

f1.pack()


f1= Frame(root, bg="grey")
b1= Button(f1, text="7", font="lucida 20 bold", padx=10, pady=4)
b1.pack(side=LEFT, padx=10, pady=4)
b1.bind('<Button-1>', click)

b1= Button(f1, text="8", font="lucida 20 bold", padx=10, pady=4)
b1.pack(side=LEFT, padx=10, pady=4)
b1.bind('<Button-1>', click)

b1= Button(f1, text="9", font="lucida 20 bold", padx=10, pady=4)
b1.pack(side=LEFT, padx=10, pady=4)
b1.bind('<Button-1>', click)

f1.pack()

f1= Frame(root, bg="grey")
b1= Button(f1, text="4", font="lucida 20 bold", padx=10, pady=4)
b1.pack(side=LEFT, padx=10, pady=4)
b1.bind('<Button-1>', click)

b1= Button(f1, text="5", font="lucida 20 bold", padx=10, pady=4)
b1.pack(side=LEFT, padx=10, pady=4)
b1.bind('<Button-1>', click)

b1= Button(f1, text="6", font="lucida 20 bold", padx=10, pady=4)
b1.pack(side=LEFT, padx=10, pady=4)
b1.bind('<Button-1>', click)

f1.pack()

f1= Frame(root, bg="grey")
b1= Button(f1, text="1", font="lucida 20 bold", padx=10, pady=4)
b1.pack(side=LEFT, padx=10, pady=4)
b1.bind('<Button-1>', click)

b1= Button(f1, text="2", font="lucida 20 bold", padx=10, pady=4)
b1.pack(side=LEFT, padx=10, pady=4)
b1.bind('<Button-1>', click)

b1= Button(f1, text="3", font="lucida 20 bold", padx=10, pady=4)
b1.pack(side=LEFT, padx=10, pady=4)
b1.bind('<Button-1>', click)

f1.pack()

f1= Frame(root, bg="grey")
b1= Button(f1, text="0", font="lucida 20 bold", padx=10, pady=4)
b1.pack(side=LEFT, padx=10, pady=4)
b1.bind('<Button-1>', click)

b1= Button(f1, text=".", font="lucida 18 bold", padx=15.8, pady=4, bg="orange")
b1.pack(side=LEFT, padx=10, pady=4)
b1.bind('<Button-1>', click)

b1= Button(f1, text="%", font="lucida 17 bold", padx=11.5, pady=4, bg="orange")
b1.pack(side=LEFT, padx=9, pady=4)
b1.bind('<Button-1>', click)

f1.pack()

f1= Frame(root, bg="grey")
b1= Button(f1, text="+", font="lucida 20 bold", padx=10, pady=4, bg="orange")
b1.pack(side=LEFT, padx=10, pady=4)
b1.bind('<Button-1>', click)

b1= Button(f1, text="-", font="lucida 20 bold", padx=14, pady=4, bg="orange")
b1.pack(side=LEFT, padx=11, pady=4)
b1.bind('<Button-1>', click)


b1= Button(f1, text="=", font="lucida 19 bold", padx=9, pady=4, bg="green")
b1.pack(side=LEFT, padx=10, pady=4)
b1.bind('<Button-1>', click)

f1.pack()






root.mainloop()