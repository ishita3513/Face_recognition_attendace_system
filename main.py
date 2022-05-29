from tkinter import*
import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter
from PIL import Image,ImageTk
from student import Student
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        img1=Image.open(r"image\img1.jpg")
        img1=img1.resize((500,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=200)

        img2=Image.open(r"image\img2.jpg")
        img2=img2.resize((500,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=200)

        img3=Image.open(r"image\img3.jpg")
        img3=img3.resize((500,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=200)


        #bg image
        img4=Image.open(r"image\imgBg.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimgBg=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimgBg)
        bg_img.place(x=0,y=200,width=1530,height=710)
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        ############## time ###################
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=5,y=0,width=100,height=50)
        time()

        # student
        img5=Image.open(r"image\img5.jpg")
        img5=img5.resize((500,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=20)


        img6=Image.open(r"image\img6.jpg")
        img6=img6.resize((510,205),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(bg_img,image=self.photoimg6,command=self.face_data,cursor="hand2")
        b1.place(x=600,y=100,width=220,height=200)

        b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=600,y=300,width=220,height=20)

        #Help face button
        img7=Image.open(r"image\img7.jpg")
        img7=img7.resize((400,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        # f_lbl=Label(self.root,image=self.photoimg5)
        # f_lbl.place(x=1000,y=0,width=500,height=200)
        b1=Button(bg_img,image=self.photoimg7,command=self.attendance_date,cursor="hand2")
        b1.place(x=1000,y=100,width=220,height=200)

        b1_1=Button(bg_img,text="Attandance",command=self.attendance_date,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=300,width=220,height=20)

         #Help face button
        img8=Image.open(r"image\img8.jpg")
        img8=img8.resize((300,150),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        # f_lbl=Label(self.root,image=self.photoimg5)
        # f_lbl.place(x=1000,y=0,width=500,height=200)
        b1=Button(bg_img,image=self.photoimg8,command=self.train_data,cursor="hand2")
        b1.place(x=200,y=350,width=220,height=200)

        b1_1=Button(bg_img,text="Train model",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=550,width=220,height=20)

        #  Help face button
        img9=Image.open(r"image\img9.jpg")
        img9=img9.resize((300,100),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        # f_lbl=Label(self.root,image=self.photoimg5)
        # f_lbl.place(x=1000,y=0,width=500,height=200)
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=600,y=350,width=220,height=200)

        b1_1=Button(bg_img,text="Upload Photo ",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=600,y=550,width=220,height=20)

        # Exit button
        img10=Image.open(r"image\img10.jpg")
        img10=img10.resize((200,100),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        # f_lbl=Label(self.root,image=self.photoimg5)
        # f_lbl.place(x=1000,y=0,width=500,height=200)
        b1=Button(bg_img,image=self.photoimg10,command=self.exit_button,cursor="hand2")
        b1.place(x=1000,y=350,width=220,height=200)

        b1_1=Button(bg_img,text="Exit",command=self.exit_button,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=550,width=220,height=20)

    def open_img(self):
        os.startfile("data")

    def exit_button(self):
        self.exit_button=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project",parent=self.root)
        if self.exit_button>0:
            self.root.destroy()
        else:
            return

        # messagebox.showwarning("warning","Do you want to exit")

    ##################function button###############

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_date(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def attendance_date(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()