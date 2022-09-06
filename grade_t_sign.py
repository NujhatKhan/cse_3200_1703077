from cgitb import text
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
row_5=cur.fetchone()
var1="welcome to "+row[0]
cur.execute("select distinct(s_roll) from student_table_1 where student_table_1.student_email in (select student_class.student_email from student_class where password_c=%s)",row_5[0])
row_1=cur.fetchall()
#cur.execute("select s_roll from student_table_1 where student_email=%s",row_1[0])
#row_2=cur.fetchall()
#print(row_1)
con.commit()
con.close
tool_frame=Frame(root,bg="#CDC2AE")
tool_frame.place(x=0,y=0,relwidth=1,height=90)
welcome_label=Label(tool_frame,text=var1,font=("times new roman",20,"bold"),bg="#CDC2AE",fg="#48494B").place(x=580,y=0)
option=Label(root,text="Enter marks",font=("times new roman",20,"bold"),bg="white",fg="#787276").place(x=450,y=100)
txt_option=ttk.Combobox(root,font=("times new roman",13),state="readonly") 
txt_option['values']=("CT_1","CT_2","CT_3","CT_4")
txt_option.place(x=550,y=140,width=250)
#txt_option.current(0)
j=0
e2=[]
for i in row_1:
    lbl=Label(root,text="Roll",font=("times new roman",20,"bold"),bg="white",fg="#787276").place(x=450,y=170+(j*40))
    en_1=Label(root,text=i[0],font=("times new roman",15)).place(x=500,y=170+(j*40))
    mark_lbl=Label(root,text="Marks",font=("times new roman",20,"bold"),bg="white",fg="#787276").place(x=750,y=170+(j*40))
    en_2=Entry(root,font=("times new roman",15)).place(x=820,y=170+(j*40))
    j=j+1
    e2.append(en_2)
def enter_btn():
    if txt_option.get()=="":
        messagebox.showerror("Error","must enter which ct",parent=root)
    else:
        try:
            con=pymysql.connect(host="localhost",user="root",password="",database="virtual-classroom")
            cur=con.cursor()
            if txt_option.get()=="CT_1":
                    k=0
                    for i in row_1:
                        cur.execute("insert into grade (password_c,s_roll) values(%s,%s)",
                        (
                            row_5[0],
                            i[0]
                        ))
                        k+=1
            con.commit()
            con.close()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)
       
btn=Button(root,text="Enter",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=lambda:enter_btn()).place(x=610,y=170+(j*60),width=150)





def stream():
    root.destroy()
    import stream_student
btn_stream=Button(tool_frame,text="Stream",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=stream)
btn_stream.place(x=450,y=50)

def class_work():
    return

#btn_classwork=Button(tool_frame,text="Classwork",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=class_work)
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
    lbl=Label (newWindow,text="class password is " +row[1],font=("times new roman",20,"bold"),bg="#CDC2AE",fg="#48494B").place(x=20,y=10)



btn_pass=Button(tool_frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=for_pass)
btn_pass.place(x=1080,y=50)

def for_exit():
    root.destroy()
    import login

btn_ext=Button(tool_frame,text="Exit",font=("times new roman",15,"bold"),fg="black",bg="#ECE5C7",command=for_exit)
btn_ext.place(x=1200,y=50)

root.mainloop()