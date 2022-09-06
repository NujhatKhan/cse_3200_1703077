from cgitb import text
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
cur.execute("select class_name,password_class from class_instructor where password_class=(select variable from random order by id desc limit 1)")
row=cur.fetchone()
#cur.execute("insert into random (variable) values (%s)",row[0])
var1="welcome to "+row[0]
con.commit()
con.close
tool_frame=Frame(root,bg="#CDC2AE")
tool_frame.place(x=0,y=0,relwidth=1,height=90)
welcome_label=Label(tool_frame,text=var1,font=("times new roman",20,"bold"),bg="#CDC2AE",fg="#48494B").place(x=580,y=0)



#stream function
def stream():
    root.destroy()
    import stream_student


def class_work():
    return



#people function
"""def people():
    con=pymysql.connect(host="localhost",user="root",password="",database="virtual-classroom")
    cur=con.cursor()
    cur.execute("select class_name from class_instructor where password_class=(select variable from random order by id desc limit 1)")
    row=cur.fetchone()
    var1="welcome to "+row[0]
    root.destroy()
    secondary=Tk()
    secondary.title("main window_teacher")
    secondary.geometry("1350x700+0+0")
    secondary.state('zoomed')
    secondary.config(bg="white")
    tool_frame=Frame(secondary,bg="#CDC2AE")
    tool_frame.place(x=0,y=0,relwidth=1,height=90)
    welcome_label=Label(tool_frame,text=var1,font=("times new roman",20,"bold"),bg="#CDC2AE",fg="#48494B").place(x=580,y=0)

    j=1
    ins_label=Label(secondary,text="Teachers",font=("times new roman",30,"bold","underline"),bg="white",fg="#48494B").place(x=450,y=140)
    try:
        con=pymysql.connect(host="localhost",user="root",password="",database="virtual-classroom")
        cur=con.cursor()
        cur.execute("select password_class from class_instructor order by id desc limit 1")
        row=cur.fetchone()
        cur.execute("select instructor_email from class_instructor where password_class=%s",row[0])
        row_1=cur.fetchall()
        for i in row_1:
            cur.execute("select f_name,l_name from users where email=%s",i[0])
            row_2=cur.fetchone()
            row_3=str(j)+") "+str(row_2[0]) +" "+str(row_2[1])
            my_label=Label(secondary,text=row_3,font=("times new roman",20,"bold"),bg="white").place(x=460,y=170+(28*j))
            j+=1
        cur.execute("select student_email from student_class where password_c=%s",row[0])
        row_1=cur.fetchall()
        student_label=Label(secondary,text="Students",font=("times new roman",30,"bold","underline"),bg="white",fg="#48494B").place(x=450,y=170+(28*j))
        k=200+(28*j)
        v=1
        for i in row_1:
            cur.execute("select f_name,l_name from users where email=%s",i[0])
            row_2=cur.fetchone()
            row_3=str(v)+") "+str(row_2[0]) +" "+str(row_2[1])
            my_label=Label(secondary,text=row_3,font=("times new roman",20,"bold"),bg="white").place(x=460,y=k+(28*v))
            v+=1
        con.commit()
        con.close()
    except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)

    btn_stream=Button(tool_frame,text="Stream",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=stream)
    btn_stream.place(x=450,y=50)

    btn_classwork=Button(tool_frame,text="Classwork",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=class_work)
    btn_classwork.place(x=580,y=50)

    btn_people=Button(tool_frame,text="People",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=people)
    btn_people.place(x=720,y=50)

    btn_grads=Button(tool_frame,text="Grades",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=grades)
    btn_grads.place(x=840,y=50)

    secondary.mainloop()"""





def grades():
    root.destroy()
    import grade_student



#for toolbar options
btn_stream=Button(tool_frame,text="Stream",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=stream)
btn_stream.place(x=450,y=50)

#btn_classwork=Button(tool_frame,text="Classwork",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=class_work)
#btn_classwork.place(x=580,y=50)

def people():
    root.destroy()
    import people_student

btn_people=Button(tool_frame,text="People",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=people)
btn_people.place(x=720,y=50)

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