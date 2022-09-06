from cgitb import text
from tkinter import *
from tkinter import ttk,messagebox
from tkmacosx import Button
from PIL import Image,ImageTk
import pymysql

root=Tk()
root.title("student_join_class")
root.geometry("500x500+0+0")
#root.state('zoomed')
root.config(bg="#CDC2AE")

#for roll
roll_label=Label(root,text="Enter your roll",font=("times new roman",25,"bold"),bg="#CDC2AE",fg="black").place(x=100,y=100)
roll_entry=Entry(root,font=("times new roman",20),bg="#D6CFC7")
roll_entry.place(x=100,y=150,width=350)

#for roll command
def roll_cmd():
    if roll_entry.get()=="":
        messagebox.showerror("Error","Must enter roll",parent=root)
    else:
        try:
            con=pymysql.connect(host="localhost",user="root",password="",database="virtual-classroom")
            cur=con.cursor()
            cur.execute("select s_roll from student_table_1 where s_roll=%s",roll_entry.get())
            var1=cur.fetchone()
            if var1==None:
                cur.execute("select email from users order by id desc limit 1")
                row=cur.fetchone()
                cur.execute("insert into for_login_store (email) value (%s)",row[0])
                cur.execute("insert into student_table_1 (student_email,s_roll) values (%s,%s)",
                (
                    row[0],
                    roll_entry.get()
                ))
                con.commit()
                con.close()
                text_label=Label(root,text="Do you want to enter a class?",font=("times new roman",25),bg="#CDC2AE",fg="black").place(x=100,y=50)
                join_label=Label(root,text="Enter class code",font=("times new roman",25,"bold"),bg="#CDC2AE",fg="black").place(x=100,y=100)
                join_label_entry=Entry(root,font=("times new roman",20),bg="#D6CFC7")
                join_label_entry.place(x=100,y=150,width=350)
                def join_cmd():
                    if join_label_entry.get()=="":
                        messagebox.showerror("Error","Must enter class code",parent=root)
                    else:
                        try:
                            con=pymysql.connect(host="localhost",user="root",password="",database="virtual-classroom")
                            cur=con.cursor()
                            #cur.execute("insert into for_login_store ")
                            cur.execute("select email from for_login_store order by id desc limit 1")
                            row=cur.fetchone()
                            if row==None:
                                 messagebox.showerror("Error","Invalid class code",parent=root)
                            else:
                                cur.execute("select email from users order by id desc limit 1")
                                row=cur.fetchone()
                                cur.execute("select class_name from class_instructor where password_class=%s",join_label_entry.get())
                                var1=cur.fetchone()
                                cur.execute("insert into random (variable) value (%s)",join_label_entry.get())
                                cur.execute("insert into student_class (student_email,class_name,password_c) values (%s,%s,%s)",
                                (
                                    row[0],
                                    var1[0],
                                    join_label_entry.get()
                                ))
                                con.commit()
                                con.close()
                                root.destroy()
                                import main_class_2

                        except Exception as es:
                             messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)
                        

                #join button
                join_btn=Button(root,text="Join",font=("times new roman",30),bd=0,fg="#4195a3",bg="#b8b2ad",command=join_cmd).place(x=100,y=200,width=350,height=40)

                #exit_cmd
                def exit_cmd():
                    root.destroy()
                    import login

                #exit button
                exit_button=Button(root,text="exit",font=("times new roman",30),bd=0,fg="#4195a3",bg="#b8b2ad",command=exit_cmd).place(x=210,y=270)

            else:
                messagebox.showerror("Error","Roll already taken",parent=root)
        except Exception as es:
            messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)



roll_btn=Button(root,text="Enter",font=("times new roman",30),bd=0,fg="#4195a3",bg="#b8b2ad",command=roll_cmd).place(x=100,y=200,width=350,height=40)

root.mainloop()