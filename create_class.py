from tkinter import *
from tkinter import ttk,messagebox
from tkmacosx import Button
from PIL import Image,ImageTk
import pymysql
import random
import array

class create():
    def __init__(self,root):
        self.root=root
        self.root.title("Virtual-Classroom")
        self.root.geometry("1350x700+0+0")
        self.root.state('zoomed')
        self.root.config(bg="#ECE5C7")

        #for background color
        left_lbl=Label(self.root,bg="#CDC2AE",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

         #frame
        frame_btn=Frame(self.root,bg="white")
        frame_btn.place(x=350,y=200,width=650,height=400)

        title=Label(frame_btn,text="Create class",font=("times new roman",25,"bold"),bg="white",fg="#48494B").place(x=50,y=30)

        #for class name
        class_name=Label(frame_btn,text="Class Name",font=("times new roman",20,"bold"),bg="white",fg="#787276").place(x=50,y=100)
        self.txt_cname=Entry(frame_btn,font=("times new roman",15),bg="#D6CFC7")
        self.txt_cname.place(x=50,y=160,width=350)

        #cancel button
        btn_cancel=Button(frame_btn,text="Cancel",font=("times new roman",20),bd=0,fg="#4CACBC",bg="#D6CFC7",command=self.cancel).place(x=150,y=250,width=150,height=27)

        #create button 
        btn_create=Button(frame_btn,text="Create",font=("times new roman",20),bd=0,fg="#4CACBC",bg="#D6CFC7",command=self.new).place(x=350,y=250,width=150,height=27)

    def clear(self):
        self.txt_cname.delete(0,END)
        #self.txt_password.delete(0,END)

    def cancel(self):
        self.root.destroy()
        import pg_1

    def new(self):
        if self.txt_cname.get()=="":
            messagebox.showerror("Error","Class name is required",parent=self.root)
        #elif self.txt_password.get()=="":
            #messagebox.showerror("Error","Password for class is required",parent=self.root)
        else:
            try:
                MAX_LEN = 7
                DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
                LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's','t', 'u', 'v', 'w', 'x', 'y','z']
 
                UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S','T', 'U', 'V', 'W', 'X', 'Y','Z']
 
                SYMBOLS = ['@', '#', '$', '%']
                COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
                rand_digit = random.choice(DIGITS)
                rand_upper = random.choice(UPCASE_CHARACTERS)
                rand_lower = random.choice(LOCASE_CHARACTERS)
                rand_symbol = random.choice(SYMBOLS)
                temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
                for x in range(MAX_LEN - 4):
                    temp_pass = temp_pass + random.choice(COMBINED_LIST)
                    temp_pass_list = array.array('u', temp_pass)
                    random.shuffle(temp_pass_list)
                password = ""
                for x in temp_pass_list:
                     password = password + x
                con=pymysql.connect(host="localhost",user="root",password="",database="virtual-classroom")
                cur=con.cursor()
                cur.execute("select email from users order by id desc limit 1")
                row=cur.fetchone()
                cur.execute("insert into class_instructor (class_name,instructor_email,password_class) values (%s,%s,%s)",
                    (
                        self.txt_cname.get(),
                        row[0],
                        password
                    ))
                con.commit()
                con.close()
                self.clear()
                self.root.destroy()
                import main_class
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)


root=Tk()
obj=create(root)
root.mainloop()