from tkinter import *
from tkinter import ttk,messagebox
from tkmacosx import Button
import pymysql

class pg_1:
    def __init__(self,root):
        self.root=root
        self.root.title("Virtual-Classroom")
        self.root.geometry("1350x700+0+0")
        self.root.state('zoomed')
        self.root.config(bg="#CDC2AE")

        #for background color
        left_lbl=Label(self.root,bg="#ECE5C7",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        #frame
        frame_btn=Frame(self.root,bg="white")
        frame_btn.place(x=350,y=200,width=750,height=450)

        #create class button
        btn_create=Button(frame_btn,text="Create class",font=("times new roman",30),bd=0,fg="#4CACBC",bg="#D6CFC7",command=self.create).place(x=120,y=140,width=500,height=40)

        #join class button 
        btn_join=Button(frame_btn,text="Join class",font=("times new roman",30),bd=0,fg="#4CACBC",bg="#D6CFC7",command=self.join).place(x=120,y=240,width=500,height=40)

        #exit button
        btn_exit=Button(frame_btn,text="Exit",font=("times new roman",30),bd=0,fg="#4CACBC",bg="#D6CFC7",command=self.for_exit).place(x=250,y=340,width=250,height=40)
    def create(self):
        self.root.destroy()
        import create_class

    def for_exit(self):
        self.root.destroy()
        import login

    def join(self):
        self.root.destroy()
        secondary=Tk()
        secondary.title("Join class window")
        secondary.geometry("500x500+0+0")
        secondary.config(bg="#CDC2AE")

        #for label
        join_label=Label(secondary,text="Enter class code",font=("times new roman",25,"bold"),bg="#CDC2AE",fg="black").place(x=100,y=100)
        join_label_entry=Entry(secondary,font=("times new roman",20),bg="#D6CFC7")
        join_label_entry.place(x=100,y=150,width=350)

        #join function
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
                        cur.execute("select email from users order by id desc limit 1")
                        row=cur.fetchone()
                        cur.execute("select class_name from class_instructor where password_class=%s",join_label_entry.get())
                        var1=cur.fetchone()
                        cur.execute("insert into class_instructor (class_name,instructor_email,password_class) values (%s,%s,%s)",
                        (
                            var1[0],
                            row[0],
                            join_label_entry.get()
                        ))
                        
                        con.commit()
                        con.close()
                        secondary.destroy()
                        import main_class

                except Exception as es:
                    messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
                

        #join button
        join_btn=Button(secondary,text="Join",font=("times new roman",30),bd=0,fg="#4195a3",bg="#b8b2ad",command=join_cmd).place(x=100,y=200,width=350,height=40)

        secondary.mainloop()
root=Tk()
obj=pg_1(root)
root.mainloop()
