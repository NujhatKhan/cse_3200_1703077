from tkinter import *
from tkinter import ttk,messagebox
from tkmacosx import Button
from PIL import Image,ImageTk
import random
import array
import pymysql

root=Tk()
root.title("t_sign_in")
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
                    messagebox.showerror("Error",f"Error due to: {str(es)}",parent=secondary)


    join_btn=Button(secondary,text="Join",font=("times new roman",30),bd=0,fg="#4195a3",bg="#b8b2ad",command=join_cmd).place(x=100,y=200,width=350,height=40)


    def exit_cmd():
        secondary.destroy()
        import login
    join_btn=Button(secondary,text="Exit",font=("times new roman",30),bd=0,fg="#4195a3",bg="#b8b2ad",command=exit_cmd).place(x=100,y=250,width=350,height=40)

    secondary.mainloop()





btn_1=Button(root,text="Join class",font=("times new roman",15),command=join,fg="#DF7861").place(x=450,y=100,height=40)

def create():
    root.destroy()
    secondary=Tk()
    secondary.title("Create class window")
    secondary.geometry("1350x700+0+0")
    secondary.state('zoomed')
    secondary.config(bg="#CDC2AE")
    secondary.config(bg="#ECE5C7")

    #for background color
    left_lbl=Label(secondary,bg="#CDC2AE",bd=0)
    left_lbl.place(x=0,y=0,relheight=1,width=600)

     #frame
    frame_btn=Frame(secondary,bg="white")
    frame_btn.place(x=350,y=200,width=650,height=400)

    title=Label(frame_btn,text="Create class",font=("times new roman",25,"bold"),bg="white",fg="#48494B").place(x=50,y=30)

    #for class name
    class_name=Label(frame_btn,text="Class Name",font=("times new roman",20,"bold"),bg="white",fg="#787276").place(x=50,y=100)
    txt_cname=Entry(frame_btn,font=("times new roman",15),bg="#D6CFC7")
    txt_cname.place(x=50,y=160,width=350)

    def cancel():
        secondary.destroy()
        import t_sign_in

    #cancel button
    btn_cancel=Button(frame_btn,text="Cancel",font=("times new roman",20),bd=0,fg="#4CACBC",bg="#D6CFC7",command=cancel).place(x=150,y=250,width=150,height=27)

    def new():
        if txt_cname.get()=="":
            messagebox.showerror("Error","Class name is required",parent=secondary)
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
                cur.execute("select email from for_login_store order by id desc limit 1")
                row=cur.fetchone()
                cur.execute("insert into class_instructor (class_name,instructor_email,password_class) values (%s,%s,%s)",
                    (
                        txt_cname.get(),
                        row[0],
                        password
                    ))
                con.commit()
                con.close()
                secondary.destroy()
                import main_class
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=secondary)




    #create button 
    btn_create=Button(frame_btn,text="Create",font=("times new roman",20),bd=0,fg="#4CACBC",bg="#D6CFC7",command=new).place(x=350,y=250,width=150,height=27)





btn_2=Button(root,text="Create class",font=("times new roman",15),fg="#DF7861",command=create).place(x=650,y=100,height=40)

def exit():
    root.destroy()
    import login
btn_3=Button(root,text="Exit",font=("times new roman",15),fg="#DF7861",command=exit).place(x=850,y=100,height=40)

lbl_2=Label(root,text="your classes",font=("times new roman",25,"underline"),bg="#CDC2AE",fg="black").place(x=450,y=160)
j=1
def press_button(b):
    con=pymysql.connect(host="localhost",user="root",password="",database="virtual-classroom")
    cur=con.cursor()
    cur.execute("insert into random (variable) value (%s)",str(b))
    con.commit()
    con.close()
    import main_cls_t_sign_in
try:
    con=pymysql.connect(host="localhost",user="root",password="",database="virtual-classroom")
    cur=con.cursor()
    cur.execute("select email from for_login_store order by id desc limit 1")
    row=cur.fetchone()
    cur.execute("select class_name,password_class from class_instructor where instructor_email=%s",row[0])
    row_2=cur.fetchall()
    for i in row_2:
        txt=str(i[0])
        txt_1=str(i[1])
        btn_lbl=Button(root,text=i[0],font=("times new roman",15),fg="#DF7861",command=lambda b=i[1]:press_button(b)).place(x=450,y=180+(j*60),height=40)
        j+=1

    con.commit()
    con.close()

except Exception as es:
    messagebox.showerror("Error",f"Error due to: {str(es)}",parent=root)

root.mainloop()