from tkinter import *
from tkinter import ttk,messagebox
from tkmacosx import Button
from PIL import Image,ImageTk
import pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration window")
        self.root.geometry("1350x700+0+0")
        self.root.state('zoomed')
        self.root.config(bg="white")

        #background image
        self.bg=ImageTk.PhotoImage(file="images/bg1.jpeg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #registration frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=550,y=200,width=700,height=500)

        title=Label(frame1,text="Register Here",font=("times new roman",25,"bold"),bg="white",fg="#48494B").place(x=50,y=30)

        #for first name
        f_name=Label(frame1,text="First Name",font=("times new roman",20,"bold"),bg="white",fg="#787276").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="#D6CFC7")
        self.txt_fname.place(x=50,y=130,width=250)

        #for last name
        l_name=Label(frame1,text="Last Name",font=("times new roman",20,"bold"),bg="white",fg="#787276").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="#D6CFC7")
        self.txt_lname.place(x=370,y=130,width=250)

        #for contact number
        contact=Label(frame1,text="Contact No",font=("times new roman",20,"bold"),bg="white",fg="#787276").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="#D6CFC7")
        self.txt_contact.place(x=50,y=200,width=250)

        #for email
        email=Label(frame1,text="Email",font=("times new roman",20,"bold"),bg="white",fg="#787276").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="#D6CFC7")
        self.txt_email.place(x=370,y=200,width=250)

        #for role_ option
        option=Label(frame1,text="Role",font=("times new roman",20,"bold"),bg="white",fg="#787276").place(x=50,y=240)
        self.txt_option=ttk.Combobox(frame1,font=("times new roman",13),state="readonly") 
        self.txt_option['values']=("Select Your Role","Instructor","Student")
        self.txt_option.place(x=50,y=270,width=250)
        self.txt_option.current(0)

        #for password
        password=Label(frame1,text="Password",font=("times new roman",20,"bold"),bg="white",fg="#787276").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="#D6CFC7")
        self.txt_password.place(x=50,y=340,width=250)

        #confirm password
        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",20,"bold"),bg="white",fg="#787276").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="#D6CFC7")
        self.txt_cpassword.place(x=370,y=340,width=250)

        #for terms and conditions
        self.var_chk=IntVar()
        c_box=Checkbutton(frame1,text="I Agree to the Terms and Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",14)).place(x=50,y=390)

        #for button
        #self.btn_img=ImageTk.PhotoImage(file="images/button_register-now.png")
        #btn=Button(frame1,image=self.btn_img,cursor="hand2",bd="0",bg="#D6CFC7").place(x=250,y=440,width=200,height=40)
        btn_register=Button(frame1,text="Register Now",font=("times new roman",30),bd=0,fg="#4CACBC",bg="#D6CFC7",command=self.register_data).place(x=250,y=440,width=200,height=40)

        #for sign in button
        txt=Label(self.root,text="Already Registered?",font=("times new roman",20,"bold"),fg="#787276").place(x=260,y=400)
        btn_login=Button(self.root,text="Sign In",font=("times new roman",20),bd=0,fg="#4CACBC",command=self.login_window).place(x=300,y=450)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_option.current(0)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.var_chk=0

    #to go to login page
    def login_window(self):
        self.root.destroy()
        import login

        
    #for mysql
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.txt_option.get()=="Select Your Role" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password and confirm password must be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="virtual-classroom")
                cur=con.cursor()
                cur.execute("select * from users where email=%s",self.txt_email.get())
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exists. Please try with another email.",parent=self.root)
                else:
                 cur.execute("insert into users (f_name,l_name,contact,email,role,password) values (%s,%s,%s,%s,%s,%s)",
                 (self.txt_fname.get(),
                 self.txt_lname.get(),
                 self.txt_contact.get(),
                 self.txt_email.get(),
                 self.txt_option.get(),
                 self.txt_password.get()
                 ))
                 cur.execute("insert into for_login_store (email) value (%s)",self.txt_email.get())
                 con.commit()
                 con.close()
                 messagebox.showinfo("Success","Registration successful",parent=self.root)
                 if self.txt_option.get()=="Instructor":
                    self.clear()
                    self.root.destroy()
                    import pg_1
                 elif self.txt_option.get()=="Student":
                    self.clear()
                    self.root.destroy()
                    import pg_2
            

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
            


root=Tk()
obj=Register(root)
root.mainloop()