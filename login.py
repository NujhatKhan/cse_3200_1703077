from tkinter import *
from tkinter import ttk,messagebox
from tkmacosx import Button
from PIL import Image,ImageTk
import pymysql
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Sign In window")
        self.root.geometry("1350x700+0+0")
        self.root.state('zoomed')
        self.root.config(bg="#CDC2AE")
        
        #for background color
        left_lbl=Label(self.root,bg="#ECE5C7",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        #login frame
        frame_sign_in=Frame(self.root,bg="white")
        frame_sign_in.place(x=350,y=200,width=750,height=450)

        title=Label(frame_sign_in,text="Sign In Here",font=("times new roman",25,"bold"),bg="white",fg="#48494B").place(x=70,y=30)

        #for email
        email=Label(frame_sign_in,text="Email",font=("times new roman",25,"bold"),bg="white",fg="#787276").place(x=70,y=80)
        self.txt_email=Entry(frame_sign_in,font=("times new roman",20),bg="#D6CFC7")
        self.txt_email.place(x=70,y=120,width=350)

        #for password
        password=Label(frame_sign_in,text="Password",font=("times new roman",25,"bold"),bg="white",fg="#787276").place(x=70,y=170)
        self.txt_password=Entry(frame_sign_in,font=("times new roman",20),bg="#D6CFC7")
        self.txt_password.place(x=70,y=210,width=350)

        #register button
        btn_reg=Button(frame_sign_in,text="No account? Register Now",font=("times new roman",15),fg="#DF7861",command=self.register_window).place(x=70,y=270)

        #sign in button
        btn=Button(frame_sign_in,text="Sign In",font=("times new roman",30),bd=0,fg="#4CACBC",bg="#D6CFC7",command=self.login).place(x=120,y=340,width=500,height=40)

    #to go to reg. page
    def register_window(self):
        self.root.destroy()
        import register

    #for database
    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="virtual-classroom")
                cur=con.cursor()
                cur.execute("select * from users where email=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Email or Password",parent=self.root)
                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                    cur.execute("insert into for_login_store (email) values (%s)",row[4])
                    cur.execute("select email from for_login_store order by id desc limit 1")
                    row=cur.fetchone()
                    cur.execute("select role from users where email=%s",row[0])
                    r1=cur.fetchone()
                    if r1[0]=='Instructor':
                        self.root.destroy()
                        import t_sign_in
                    else:
                        self.root.destroy()
                        import s_sign_in
                con.commit()
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)



root=Tk()
obj=Login(root)
root.mainloop()