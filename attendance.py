from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
# import mysql.connector
# from time import strftime
# from datetime import datetime
# from turtle import hideturtle
# import cv2
# import numpy as np
import os
import csv
from tkinter import filedialog

# from sqlalchemy import false

my_data=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        # self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_status=StringVar()      

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
        title_lbl=Label(bg_img,text="ATTEDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="blue",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1500,height=600)

        #Left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),fg="black")
        Left_frame.place(x=10,y=10,width=730,height=520)

        # table_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,bg="white")
        # table_frame.place(x=5,y=130,width=720,height=200)
        
        img_left=Image.open(r"image\img11.png")
        img_left=img_left.resize((250,125),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=150,y=10,width=250,height=125)

         #Class studentinfo course
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"),fg="black")
        class_student_frame.place(x=5,y=150,width=720,height=250)

        #attendance id
        # attenId_label=Label(class_student_frame,text="Attendance id:",font=("times new roman",12,"bold"))
        # attenId_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)
        # attenId_entry=ttk.Entry(class_student_frame,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        # attenId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student Id
        stdroll_label=Label(class_student_frame,text="Student Roll no:",font=("times new roman",12,"bold"))
        stdroll_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)
        stdroll_entry=ttk.Entry(class_student_frame,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        stdroll_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #Student name
        stdname_label=Label(class_student_frame,text="Student name:",font=("times new roman",12,"bold"))
        stdname_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)
        stdname_entry=ttk.Entry(class_student_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",12,"bold"))
        stdname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #date time
        time_label=Label(class_student_frame,text="Entry Time:",font=("times new roman",12,"bold"))
        time_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)
        time_entry=ttk.Entry(class_student_frame,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        time_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        date_label=Label(class_student_frame,text="Entry Date:",font=("times new roman",12,"bold"))
        date_label.grid(row=1,column=2,padx=2,pady=10,sticky=W)
        date_entry=ttk.Entry(class_student_frame,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        date_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #department

        dep_label=Label(class_student_frame,text="Department:",font=("times new roman",12,"bold"))
        dep_label.grid(row=2,column=0)
        dep_combo=ttk.Combobox(class_student_frame,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"),state="readonly",width=17)
        dep_combo["values"]=("--Select department--","CSE","ECE","IT","MEC","CIV")
        dep_combo.current(0)
        dep_combo.grid(row=2,column=1,padx=0,pady=0,sticky=W)
       
        atten_status_label=Label(class_student_frame,text="Attendance Status:",font=("times new roman",12,"bold"))
        atten_status_label.grid(row=2,column=2)

        atten_status_combo=ttk.Combobox(class_student_frame,textvariable=self.var_atten_status,font=("times new roman",12,"bold"),state="readonly",width=17)
        atten_status_combo["values"]=("--status--","Present","Absent")
        atten_status_combo.current(0)
        atten_status_combo.grid(row=2,column=3,padx=0,pady=10,sticky=W)

        

        btn_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"),fg="black")
        btn_frame.place(x=15,y=435,width=720,height=40)

        imcsv_btn=Button(btn_frame,text="Import CSV",command=self.importCSV ,width="23",font=("times new roman",13,"bold"),bg="lightblue",fg="black")
        imcsv_btn.grid(row=0,column=0)

        excsv_btn=Button(btn_frame,text="Export CSV",command=self.exportCSV,width="23",font=("times new roman",13,"bold"),bg="lightblue",fg="black")
        excsv_btn.grid(row=0,column=1)

        # update_btn=Button(btn_frame,text="Update",width="17",font=("times new roman",13,"bold"),bg="lightblue",fg="black")
        # update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width="23",font=("times new roman",13,"bold"),bg="lightblue",fg="black")
        reset_btn.grid(row=0,column=2)


        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),fg="black")
        right_frame.place(x=750,y=10,width=730,height=520)

        #table frame
        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=10,width=715,height=400)        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("roll","name","dep","time","date","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("status",text="Attendance Status")
        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        # self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=150)
        self.AttendanceReportTable.column("dep",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("status",width=150)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    def importCSV(self):
        global my_data
        my_data.clear()
        # if len(my_data)<1:
        #     messagebox.showerror("No Data","No Data found to import",parent=self.root)
        #     return false
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=[("CSV File","*.csv")],parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                my_data.append(i)
            self.fetchData(my_data)
    def exportCSV(self):
        try:
            if len(my_data)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=[("CSV File","*.csv")],parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in my_data:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully",parent=self.root)
        except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        row=content['values']
        # self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[0])
        self.var_atten_name.set(row[1])
        self.var_atten_dep.set(row[2])
        self.var_atten_time.set(row[3])
        self.var_atten_date.set(row[4])
        self.var_atten_status.set(row[5])
        
    def reset_data(self):
        # self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("--select department--")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_status.set("--status--")


   


if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()