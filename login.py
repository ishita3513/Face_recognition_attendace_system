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
from register import Register


class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("login")
        self.root.geometry("1550x800+0+0")


        main_frame=Frame(self.root,bd=2,bg="lavender blush")
        main_frame.place(x=0,y=0,width=1530,height=910)


        img1=Image.open(r"image\img1.jpg")
        img1=img1.resize((500,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=510,height=200)

        

        img2=Image.open(r"image\img2.jpg")
        img2=img2.resize((500,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=510,y=0,width=508,height=200)

        img3=Image.open(r"image\img3.jpg")
        img3=img3.resize((500,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1010,y=0,width=505,height=200)


        #bg image
        img4=Image.open(r"image\imgBg.jpg")
        img4=img4.resize((1530,910),Image.ANTIALIAS)
        self.photoimgBg=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimgBg)
        bg_img.place(x=0,y=195,width=1530,height=910)
        title_lbl=Label(bg_img,text="Face Recognition System",font=("times new roman",35,"bold"),bg="blue",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        

        dark_frame=Frame(self.root,bd=2,bg="peach puff")
        dark_frame.place(x=605,y=265,width=350,height=460)

        login_frame=Frame(self.root,bd=2,bg="floral white")
        login_frame.place(x=610,y=270,width=340,height=450)

        user_logo=Image.open(r"image\login_logo.jpg")
        user_logo=user_logo.resize((150,100),Image.ANTIALIAS)
        self.photouser_logo=ImageTk.PhotoImage(user_logo)
        f_lbl=Label(login_frame,image=self.photouser_logo)
        f_lbl.place(x=100,y=10,width=150,height=100)

        get_str=Label(login_frame,text="Get Started",font=("times new roman",20,"bold"),fg="black")
        get_str.place(x=98,y=100)



        form_frame=Frame(login_frame,bd=2,bg="floral white")
        form_frame.place(x=50,y=150,width=240,height=400)

        self.var_name=StringVar()
        name_label=Label(form_frame,text="Username",font=("times new roman",12,"bold"),fg="black")
        name_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)
        name_entry=ttk.Entry(form_frame,textvariable=self.var_name,font=("times new roman",10,"bold"))
        name_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        self.var_pass=StringVar()
        pass_label=Label(form_frame,text="Password",font=("times new roman",12,"bold"),fg="black")
        pass_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)
        pass_entry=ttk.Entry(form_frame,textvariable=self.var_pass,font=("times new roman",10,"bold"))
        pass_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        login_button=Button(login_frame,text="Login",command=self.login,font=("times new roman",20,"bold"),fg="white",bg="red",activebackground="red",activeforeground="white")
        login_button.place(x=130,y=250,width="100",height="40")

        register_button=Button(login_frame,text="New User Register",command=self.register,font=("times new roman",15,"bold"),fg="white",bg="SlateBlue3",activebackground="SlateBlue3",activeforeground="white")
        register_button.place(x=80,y=350,width="200",height="30")

        forgot_pass_button=Button(login_frame,command=self.forgot_pass, text="Forgot password",font=("times new roman",15,"bold"),fg="white",bg="SlateBlue3",activebackground="SlateBlue3",activeforeground="white")
        forgot_pass_button.place(x=80,y=390,width="200",height="30")

        logout_button=Button(login_frame,text="Logout",command=self.logout,font=("times new roman",15,"bold"),fg="white",bg="blue",activebackground="blue",activeforeground="white")
        logout_button.place(x=130,y=300,width="100",height="30")

    def register(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
    def logout(self):
        self.root.destroy()


    def login(self):
        if self.var_name.get()=="" or self.var_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        # elif (self.var_name.get()=="ishita" and self.var_pass.get()=="123"):
        #     messagebox.showinfo("Success","Welcome for face recogniton",parent=self.root)
        else:
            # messagebox.showerror("Error","Invalid username or password",parent=self.root)
            conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="face_recogniser")
            my_cursor=conn.cursor()
            my_cursor.execute("SELECT * FROM `login` where email=%s and pass=%s",(
                self.var_name.get(),
                self.var_pass.get()
            ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username or password",parent=self.root)
            else:
                # open_main=messagebox.askyesno("YesNo","Access only admin")
                # if open_main>0:
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition_System(self.new_window)
                # else:
                #     if not open_main:
                #         return
            conn.commit()
            conn.close()

    
    def forgot_pass(self):
        if self.var_name.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset the password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="face_recogniser")
            my_cursor=conn.cursor()
            my_cursor.execute("SELECT * FROM `login` where email=%s",(self.var_name.get(),))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","User does not exits, please enter valid username",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+270")
                l=Label(self.root2,text="Reset Password",font=("times new roman",12,"bold"),bg="white",fg="green")

                form_frame=Frame(self.root2,bd=2,bg="floral white")
                form_frame.place(x=0,y=0,width=820,height=500)
                self.var_security_q=StringVar()
                security_q_label=Label(form_frame,text="Security Query",font=("times new roman",12,"bold"))
                security_q_label.grid(row=0,column=0)

                security_q_combo=ttk.Combobox(form_frame,textvariable=self.var_security_q,font=("times new roman",12,"bold"),state="readonly",width=17)
                security_q_combo["values"]=("--Select security Query--","What is your oldest sibling’s middle name?"," What was your childhood nickname?","What was your childhood phone number including area code?","What is the name of your favorite childhood friend?")
                security_q_combo.current(0)
                security_q_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

                self.var_security_a=StringVar()
                security_a_label=Label(form_frame,text="Security answer:",font=("times new roman",12,"bold"),fg="black")
                security_a_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)
                security_a_entry=ttk.Entry(form_frame,textvariable=self.var_security_a,font=("times new roman",10,"bold"))
                security_a_entry.grid(row=1,column=1,padx=2,pady=10,sticky=W)

                self.var_reset_pass=StringVar()
                reset_pass_label=Label(form_frame,text="Reset Password",font=("times new roman",12,"bold"),fg="black")
                reset_pass_label.grid(row=2,column=0,padx=2,pady=10,sticky=W)
                reset_pass_entry=ttk.Entry(form_frame,textvariable=self.var_reset_pass,font=("times new roman",10,"bold"))
                reset_pass_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

                self.var_con_pass1=StringVar()
                con_pass1_label=Label(form_frame,text="Confirm Password",font=("times new roman",12,"bold"),fg="black")
                con_pass1_label.grid(row=3,column=0,padx=2,pady=10,sticky=W)
                con_pass1_entry=ttk.Entry(form_frame,textvariable=self.var_con_pass1,font=("times new roman",10,"bold"))
                con_pass1_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

                save_button=Button(form_frame,text="Save password",command=self.resetPass,font=("times new roman",16,"bold"),fg="white",bg="dark green",activebackground="dark green",activeforeground="white")
                save_button.place(x=50,y=200,width="150",height="30")

    def resetPass(self):
        conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="face_recogniser")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM `login` where sec_q=%s and seq_a=%s",(
            self.var_security_q.get(),
            self.var_security_a.get()
        ))
        row=my_cursor.fetchone()
        if row==None:
            messagebox.showerror("Error","Invalid sequrity question-answer",parent=self.root2)
        
        else:
            # if 
            if self.var_reset_pass.get()!=self.var_con_pass1.get():
                messagebox.showerror("Error","Confirm password is not matched with password",parent=self.root2)
            else:
                my_cursor.execute("UPDATE `login` SET `pass` = %s WHERE `email`=%s",(
                        self.var_reset_pass.get(),
                        self.var_name.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Password updated successfully!!!")
                self.var_security_q.set("--Select security Question--"),
                self.var_security_a.set(""),
                self.var_con_pass1.set(""),
                self.var_reset_pass.set("")
                self.root2.destroy()



if __name__=="__main__":
    root=Tk()
    app=login_window(root)
    root.mainloop()

        


