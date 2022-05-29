from random import random
from time import time
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from main import Face_Recognition_System



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("login")
        self.root.geometry("1550x800+0+0")

        #lavender blush
        main_frame=Frame(self.root,bd=2,bg="dark grey")
        main_frame.place(x=0,y=0,width=1530,height=910)

        dark_frame=Frame(self.root,bd=2,bg="grey")
        dark_frame.place(x=420,y=140,width=850,height=550)

        login_frame=Frame(self.root,bd=2,bg="floral white")
        login_frame.place(x=400,y=160,width=850,height=550)

        user_logo=Image.open(r"image\login_logo.jpg")
        user_logo=user_logo.resize((150,100),Image.ANTIALIAS)
        self.photouser_logo=ImageTk.PhotoImage(user_logo)
        f_lbl=Label(login_frame,image=self.photouser_logo)
        f_lbl.place(x=150,y=10,width=150,height=100)

        get_str=Label(login_frame,text="Register Here",font=("times new roman",20,"bold"),fg="Dark Green")
        get_str.place(x=140,y=100)


        form_frame=Frame(login_frame,bd=2,bg="floral white")
        form_frame.place(x=150,y=150,width=820,height=500)

        self.var_fname=StringVar()
        first_name_label=Label(form_frame,text="First Name",font=("times new roman",12,"bold"),fg="black")
        first_name_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)
        first_name_entry=ttk.Entry(form_frame,textvariable=self.var_fname,font=("times new roman",10,"bold"))
        first_name_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        self.var_lname=StringVar()
        last_name_label=Label(form_frame,text="Last Name",font=("times new roman",12,"bold"),fg="black")
        last_name_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)
        last_name_entry=ttk.Entry(form_frame,textvariable=self.var_lname,font=("times new roman",10,"bold"))
        last_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        self.var_email=StringVar()
        email_label=Label(form_frame,text="Email",font=("times new roman",12,"bold"),fg="black")
        email_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)
        email_entry=ttk.Entry(form_frame,textvariable=self.var_email,font=("times new roman",10,"bold"))
        email_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        self.var_contact=StringVar()
        contact_label=Label(form_frame,text="Contact No.",font=("times new roman",12,"bold"),fg="black")
        contact_label.grid(row=1,column=2,padx=2,pady=10,sticky=W)
        contact_entry=ttk.Entry(form_frame,textvariable=self.var_contact,font=("times new roman",10,"bold"))
        contact_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        self.var_security_q=StringVar()
        security_q_label=Label(form_frame,text="Security Query",font=("times new roman",12,"bold"))
        security_q_label.grid(row=2,column=0)

        security_q_combo=ttk.Combobox(form_frame,textvariable=self.var_security_q,font=("times new roman",12,"bold"),state="readonly",width=17)
        security_q_combo["values"]=("--Select security Query--","What is your oldest sibling’s middle name?"," What was your childhood nickname?","What was your childhood phone number including area code?","What is the name of your favorite childhood friend?")
        security_q_combo.current(0)
        security_q_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        self.var_security_a=StringVar()
        security_a_label=Label(form_frame,text="Security answer:",font=("times new roman",12,"bold"),fg="black")
        security_a_label.grid(row=2,column=2,padx=2,pady=10,sticky=W)
        security_a_entry=ttk.Entry(form_frame,textvariable=self.var_security_a,font=("times new roman",10,"bold"))
        security_a_entry.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        self.var_pass=StringVar()
        pass_label=Label(form_frame,text="Password",font=("times new roman",12,"bold"),fg="black")
        pass_label.grid(row=3,column=0,padx=2,pady=10,sticky=W)
        pass_entry=ttk.Entry(form_frame,textvariable=self.var_pass,font=("times new roman",10,"bold"))
        pass_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        self.var_con_pass=StringVar()
        con_pass_label=Label(form_frame,text="Confirm Password",font=("times new roman",12,"bold"),fg="black")
        con_pass_label.grid(row=3,column=2,padx=2,pady=10,sticky=W)
        con_pass_entry=ttk.Entry(form_frame,textvariable=self.var_con_pass,font=("times new roman",10,"bold"))
        con_pass_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        register_button=Button(login_frame,text="Register",command=self.register,font=("times new roman",16,"bold"),fg="white",bg="dark green",activebackground="dark green",activeforeground="white")
        register_button.place(x=140,y=460,width="150",height="30")

        back_login_button=Button(login_frame,text="<-Back to login",command=self.back_login,font=("times new roman",16,"bold"),fg="white",bg="dark green",activebackground="dark green",activeforeground="white")
        back_login_button.place(x=140,y=500,width="150",height="30")

    def register(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_email.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_con_pass.get():
            messagebox.showerror("Error","Confirm password is not matched with password",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="face_recogniser")
                my_cursor=conn.cursor()
                query=("SELECT * FROM `login` where email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exits, please try another email id",parent=self.root)
                else:
                    my_cursor.execute("INSERT INTO `login` (`fname`, `lname`, `email`, `contact_no`,`sec_q`, `seq_a`, `pass`) VALUES (%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_email.get(),
                        self.var_contact.get(),
                        self.var_security_q.get(),
                        self.var_security_a.get(),
                        self.var_pass.get()
                    ))
                    conn.commit()
                    # self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","User registered successfully",parent=self.root)
                    self.var_fname.set(""),
                    self.var_lname.set(""),
                    self.var_email.set(""),
                    self.var_contact.set(""),
                    self.var_security_q.set("--Select security Query--"),
                    self.var_security_a.set(""),
                    self.var_pass.set(""),
                    self.var_con_pass.set("")

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def back_login(self):
        self.root.destroy()


if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()