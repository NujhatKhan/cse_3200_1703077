from tkinter import *
from tkinter import ttk,messagebox
from tkmacosx import Button
from PIL import Image,ImageTk
import pymysql

root=Tk()
root.title("Grade window")
root.geometry("1350x700+0+0")
root.state('zoomed')
root.config(bg="white")

con=pymysql.connect(host="localhost",user="root",password="",database="virtual-classroom")
cur=con.cursor()
cur.execute("select class_name from class_instructor where password_class=(select variable from random order by id desc limit 1)")
row=cur.fetchone()
cur.execute("select variable from random order by id desc limit 1")
r=cur.fetchone()

var1="welcome to "+row[0]
con.commit()
con.close
tool_frame=Frame(root,bg="#CDC2AE")
tool_frame.place(x=0,y=0,relwidth=1,height=90)
welcome_label=Label(tool_frame,text=var1,font=("times new roman",20,"bold"),bg="#CDC2AE",fg="#48494B").place(x=580,y=0)

option=Label(root,text="Enter which ct",font=("times new roman",20,"bold"),bg="white",fg="#787276").place(x=450,y=100)
txt_option=ttk.Combobox(root,font=("times new roman",13),state="readonly") 
txt_option['values']=("CT_1","CT_2","CT_3","CT_4")
txt_option.place(x=550,y=140,width=250)

def enter():
  if txt_option.get()=="":
      messagebox.showerror("Error","which ct is required",parent=root)
  elif txt_option.get()=="CT_1":
     con=pymysql.connect(host="localhost",user="root",password="",database="virtual-classroom")
     cur=con.cursor()
     cur.execute("select s_roll from student_table_1 where student_email=(select email from for_login_store order by id desc limit 1)")
     l=cur.fetchone()
     if l==None:
        messagebox.showerror("Error","ct marks not available",parent=root)
     else:
      cur.execute("select ct_1 from grade where s_roll=%s and password_c=%s",
      (
          l[0],
          r[0]
      ))
      l_2=cur.fetchone()
     con.commit()
     con.close()
     lbl=Label(root,text=l_2[0],font=("times new roman",20,"bold"),bg="white",fg="#787276").place(x=650,y=240)

bt=Button(root,text="enter",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=enter)
bt.place(x=650,y=200)


btn_stream=Button(tool_frame,text="Stream",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7")
btn_stream.place(x=450,y=50)

#btn_classwork=Button(tool_frame,text="Classwork",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7")
#btn_classwork.place(x=580,y=50)

def people():
    root.destroy()
    import people_student

btn_people=Button(tool_frame,text="People",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=people)
btn_people.place(x=720,y=50)

btn_grads=Button(tool_frame,text="Grades",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7")
btn_grads.place(x=840,y=50)

def for_pass():
    newWindow = Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("400x400")
    lbl=Label (newWindow,text="class password is " +r[0],font=("times new roman",20,"bold"),bg="#CDC2AE",fg="#48494B").place(x=20,y=10)



btn_pass=Button(tool_frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=for_pass)
btn_pass.place(x=1080,y=50)

def for_exit():
    root.destroy()
    import login

btn_ext=Button(tool_frame,text="Exit",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=for_exit)
btn_ext.place(x=1200,y=50)

root.mainloop()