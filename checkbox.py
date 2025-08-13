from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("500x500")
root.title("check box")
root.config(bg="salmon")
c1=IntVar()
c2=IntVar()
c3=IntVar()
def add():
    if(c1.get()==1):
        val=chk1.cget("text")
        print(val)
        messagebox.showinfo("message",val)
    if(c2.get()==1):
        val=chk2.cget("text")
        print(val)
        messagebox.showinfo("message",val)
    if(c3.get()==1):
        val=chk3.cget("text")
        print(val)
        messagebox.showinfo("message",val)

def remove():
    chk1.deselect()
    chk2.deselect()
    chk3.deselect()
    messagebox.showinfo("this message says","checkbox is cleared")
lb=Label(root,text="checkbutton",bg="wheat",fg="orange",padx=30,pady=10,font=("algerian",20,"italic"))
lb.pack(fill=X)
chk1=Checkbutton(root,text="java",variable=c1,onvalue=1,offvalue=0,bg="salmon")
chk2=Checkbutton(root,text="python",variable=c2,onvalue=1,offvalue=0,bg="salmon")
chk3=Checkbutton(root,text="c,c+",variable=c3,onvalue=1,offvalue=0,bg="salmon")
btn_save=Button(root,text="save",bg="blue",fg="white",padx=30,pady=10,width=10,font=("times",20,"bold"),command=add)
btn_remove=Button(root,text="clear",bg="blue",fg="white",padx=30,pady=10,width=10,font=("times",20,"bold"),command=remove)
chk1.pack()
chk2.pack()
chk3.pack()
btn_save.pack()
btn_remove.pack()
root.mainloop()
