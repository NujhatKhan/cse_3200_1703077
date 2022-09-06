from tkinter import *
from tkinter import ttk,messagebox
from tkmacosx import Button
from PIL import Image,ImageTk
import pymysql

root=Tk()
root.title("page_1")
root.geometry("1350x700+0+0")
root.state('zoomed')
root.config(bg="#CDC2AE")

lbl=Label(root,text="welcome to virtual classroom",font=("times new roman",25),bg="#CDC2AE",fg="black").place(x=450,y=40)
def join():
    root.destroy()
    secondary=Tk()
    secondary.title("Join class window")
    secondary.geometry("500x500+0+0")
    secondary.config(bg="#CDC2AE")

    join_label=Label(secondary,text="Enter class code",font=("times new roman",25,"bold"),bg="#CDC2AE",fg="black").place(x=100,y=100)
    join_label_entry=Entry(secondary,font=("times new roman",20),bg="#D6CFC7")
    join_label_entry.place(x=100,y=150,width=350)
    def join_cmd():
        if join_label_entry.get()=="":
             messagebox.showerror("Error","Must enter class code",parent=secondary)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="virtual-classroom")
                cur=con.cursor()
                cur.execute("select * from class_instructor where password_class=%s",join_label_entry.get())
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid class code",parent=secondary)
                else:
                    cur.execute("select email from for_login_store order by id desc limit 1")
                    row_1=cur.fetchone()
                    cur.execute("select class_name from class_instructor where password_class=%s",join_label_entry.get())
                    var1=cur.fetchone()
                    cur.execute("insert into student_class (student_email,class_name,password_c) values (%s,%s,%s)",
                    (
                        row_1[0],
                        row[1],
                        join_label_entry.get()

                    ))
                    cur.execute("insert into random (variable) value (%s)",join_label_entry.get())
                    con.commit()
                    con.close()
                    secondary.destroy()
                    import main_class_2
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=secondary)



    join_btn=Button(secondary,text="Join",font=("times new roman",30),bd=0,fg="#4195a3",bg="#b8b2ad",command=join_cmd).place(x=100,y=200,width=350,height=40)
    def exit_cmd():
        secondary.destroy()
        import login
    join_btn=Button(secondary,text="Exit",font=("times new roman",30),bd=0,fg="#4195a3",bg="#b8b2ad",command=exit_cmd).place(x=100,y=250,width=350,height=40)

    secondary.mainloop()





btn_1=Button(root,text="Join class",font=("times new roman",15),fg="#DF7861",command=join).place(x=450,y=100,height=40)
def exit():
    root.destroy()
    import login
btn_2=Button(root,text="Exit",font=("times new roman",15),fg="#DF7861",command=exit).place(x=650,y=100,height=40)

lbl_2=Label(root,text="your classes",font=("times new roman",25,"underline"),bg="#CDC2AE",fg="black").place(x=450,y=160)
j=1
def press_button(b):
    con=pymysql.connect(host="localhost",user="root",password="",database="virtual-classroom")
    cur=con.cursor()
    cur.execute("insert into random (variable) value (%s)",str(b))
    con.commit()
    con.close()
    import main_class_2
try:
    con=pymysql.connect(host="localhost",user="root",password="",database="virtual-classroom")
    cur=con.cursor()
    cur.execute("select email from for_login_store order by id desc limit 1")
    row=cur.fetchone()
    cur.execute("select class_name,password_c from student_class where student_email=%s",row[0])
    row_2=cur.fetchall()
    for i in row_2:
        txt=str(i[0])
        txt_1=str(i[1])
        btn_lbl=Button(root,text=i[0],font=("times new roman",15),fg="#DF7861",command=lambda b=i[1]:press_button(b)).place(x=450,y=180+(j*60),height=40)
        j+=1
        #txt=str(row_2[0])
        #btn_lbl=Button(root,text=txt,font=("times new roman",15),fg="#DF7861").place(x=450,y=180+(j*60),height=40)

    con.commit()
    con.close()

except Exception as es:
    messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)

root.mainloop()