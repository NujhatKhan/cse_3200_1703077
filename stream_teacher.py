from cgitb import text
from os import stat
from sre_parse import State
from tkinter import *
from tkinter import ttk,messagebox
from turtle import width
from tkmacosx import Button
from PIL import Image,ImageTk
import pymysql
root=Tk()
root.title("main window_teacher")
root.geometry("1350x700+0+0")
root.state('zoomed')
root.config(bg="white")

con=pymysql.connect(host="localhost",user="root",password="",database="virtual-classroom")
cur=con.cursor()
cur.execute("select class_name,password_class from class_instructor order by id desc limit 1")
row=cur.fetchone()
cur.execute("insert into random (variable) values (%s)",row[1])
var1="welcome to "+row[0]
con.commit()
con.close
tool_frame=Frame(root,bg="#CDC2AE")
tool_frame.place(x=0,y=0,relwidth=1,height=90)
welcome_label=Label(tool_frame,text=var1,font=("times new roman",20,"bold"),bg="#CDC2AE",fg="#48494B").place(x=580,y=0)

def post():
        input_txt=Text(root,width=72,height=5)
        input_txt.place(x=450,y=140)
        def get_post():
            con=pymysql.connect(host="localhost",user="root",password="",database="virtual-classroom")
            cur=con.cursor()
            cur.execute("select class_name,password_class from class_instructor order by id desc limit 1")
            row=cur.fetchone()
            cur.execute("insert into stream_teacher (password_c,text_box) values (%s,%s)",
            (
                row[1],
                input_txt.get(1.0,"end-1c")
            ))
            con.commit()
            con.close()
            #inp=input_txt.get()
            #lbl.config(text=inp)
            root.destroy()
            import stream_teacher
        post_btn=Button(root,text="post",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=get_post)
        post_btn.place(x=450,y=220,width=510,height=40)
        #lbl=Label(root,text="")
btn_to_post=Button(root,text="Announce something...",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=post)
btn_to_post.place(x=450,y=140,width=500,height=40)

con=pymysql.connect(host="localhost",user="root",password="",database="virtual-classroom")
cur=con.cursor()
cur.execute("select variable from random order by id desc limit 1")
row=cur.fetchone()
cur.execute("select text_box from stream_teacher where password_c=(%s) order by id desc",row[0])
row_1=cur.fetchall()
j=1
for i in row_1:
    txt=str(i[0])
    my_label=Label(root,text=txt,font=("times new roman",20),bg="white",fg="black").place(x=450,y=220+(j*50))
    j+=1
con.commit()
con.close()
#for toolbar options
btn_stream=Button(tool_frame,text="Stream",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7")
btn_stream.place(x=450,y=50)

#btn_classwork=Button(tool_frame,text="Classwork",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7")
#btn_classwork.place(x=580,y=50)

def people():
    root.destroy()
    import people_teacher

btn_people=Button(tool_frame,text="People",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=people)
btn_people.place(x=720,y=50)
def grades():
    root.destroy()
    import grade_teacher
btn_grads=Button(tool_frame,text="Grades",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=grades)
btn_grads.place(x=840,y=50)

def for_pass():
    newWindow = Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("400x400")
    lbl=Label (newWindow,text="class password is " +row[1],font=("times new roman",20,"bold"),bg="#CDC2AE",fg="#48494B").place(x=20,y=10)



btn_pass=Button(tool_frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=for_pass)
btn_pass.place(x=1080,y=50)

def for_exit():
    root.destroy()
    import login

btn_ext=Button(tool_frame,text="Exit",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=for_exit)
btn_ext.place(x=1200,y=50)

root.mainloop()