from tkinter import*
from tkinter import ttk
from turtle import hideturtle
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        #################### variables ##########################
        
        self.var_roll=StringVar()
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_sem=StringVar()
        self.var_div=StringVar()
        self.var_std_name=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()


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
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="blue",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1500,height=600)

        # scrollmain_x=ttk.Scrollbar(main_frame,orient=HORIZONTAL)
        # scrollmain_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        # scrollmain_x.pack(side=BOTTOM,fill=X)
        # scrollmain_y.pack(side=RIGHT,fill=Y)
        # self.ma_table.heading("phone",text="Phone")
        # self.student_table["show"]="headings"
        # self.student_table.pack(fill=BOTH,expand=1)

        #Left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),fg="black")
        Left_frame.place(x=10,y=10,width=730,height=520)


        img_left=Image.open(r"image\img11.png")
        img_left=img_left.resize((250,125),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=150,y=10,width=250,height=125)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Details ",font=("times new roman",12,"bold"),fg="black")
        current_course_frame.place(x=5,y=130,width=720,height=120)

        #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=17)
        dep_combo["values"]=("--Select department--","CSE","ECE","IT","MEC","CIV")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=17)
        course_combo["values"]=("--Select course--","TOC","AI","ML","DSA","OS")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        # Year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"))
        # Year_label.grid(row=1,column=0,padx=2,pady=10,sticky=W) 

        # Year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman",12,"bold"),state="readonly",width=17)
        # Year_combo["values"]=("--Select year--","1st","2nd","3rd","4th")
        # Year_combo.current(0)
        # Year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"))
        sem_label.grid(row=1,column=2,padx=2,pady=10,sticky=W) 

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly",width=17)
        sem_combo["values"]=("--Select sem--","1st","2nd","3rd","4th","5th","6th","7th","8th")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Student div
        stddiv_label=Label(current_course_frame,text="Class Division",font=("times new roman",12,"bold"))
        stddiv_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)
       
        stddiv_combo=ttk.Combobox(current_course_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=17)
        stddiv_combo["values"]=("--Select division--","A","B","C")
        stddiv_combo.current(0)
        stddiv_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Class studentinfo course
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"),fg="black")
        class_student_frame.place(x=5,y=250,width=720,height=150)


        #Student Id
        stdroll_label=Label(class_student_frame,text="Student Roll no.",font=("times new roman",12,"bold"))
        stdroll_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)
        stdroll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        stdroll_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #Student name
        stdname_label=Label(class_student_frame,text="Student name",font=("times new roman",12,"bold"))
        stdname_label.grid(row=0,column=2,padx=2,pady=10,sticky=W)
        stdname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        stdname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #student email
        stdemail_label=Label(class_student_frame,text="Student Email",font=("times new roman",12,"bold"))
        stdemail_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)
        stdemail_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        stdemail_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #phone
        phone_label=Label(class_student_frame,text="Student Phone no.",font=("times new roman",12,"bold"))
        phone_label.grid(row=1,column=2,padx=2,pady=10,sticky=W)
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radBtn1=ttk.Radiobutton(class_student_frame,text="Take Photo Sample",variable=self.var_radio1,value="Yes")
        radBtn1.grid(row=2,column=0,padx=2,pady=10,sticky=W)

        #radio button
        radBtn2=ttk.Radiobutton(class_student_frame,text="No Photo Sample",variable=self.var_radio1,value="No")
        radBtn2.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        #button form
        # btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        # btn_frame.place(x=5,y=150,width=720,height=30)

        btn_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"),fg="black")
        btn_frame.place(x=15,y=435,width=720,height=40)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width="18",font=("times new roman",13,"bold"),bg="lightblue",fg="black")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width="17",font=("times new roman",13,"bold"),bg="lightblue",fg="black")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width="17",font=("times new roman",13,"bold"),bg="lightblue",fg="black")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width="18",font=("times new roman",13,"bold"),bg="lightblue",fg="black")
        reset_btn.grid(row=0,column=3)

        #New btn frame
        btn_frame1=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"),fg="black")
        btn_frame1.place(x=15,y=470,width=720,height=40)


        take_sample_btn=Button(btn_frame1,text="Take Sample Photo",command=self.generate_dataset,width="40",font=("times new roman",13,"bold"),bg="lightblue",fg="black")
        take_sample_btn.grid(row=1,column=0)

        update_sample_btn=Button(btn_frame1,text="Update Sample Photo",command=self.update_dataset,width="39",font=("times new roman",13,"bold"),bg="lightblue",fg="black")
        update_sample_btn.grid(row=1,column=1)


        #Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=730,height=520)

        img_right=Image.open(r"image\img5.jpg")
        img_right=img_right.resize((250,125),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=150,y=10,width=250,height=125)

        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search Student ",font=("times new roman",12,"bold"),bg="white")
        search_frame.place(x=5,y=130,width=720,height=60)

        # search_label=Label(search_frame,text="Year",font=("times new roman",12,"bold"))
        # search_label.grid(row=1,column=0,padx=2,pady=10,sticky=W) 

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=17)
        search_combo["values"]=("--Search by--","name","roll","phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        search_btn=Button(search_frame,text="Search",width="27",font=("times new roman",13,"bold"),bg="lightblue",fg="black")
        search_btn.grid(row=0,column=1,padx=1)

        show_all_btn=Button(search_frame,text="Show All",command=self.fetch_data,width="26",font=("times new roman",13,"bold"),bg="lightblue",fg="black")
        show_all_btn.grid(row=0,column=3)

        #table frame
        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=200,width=720,height=280)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("roll","dep","course","sem","div","name","email","phone","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        
        # self.student_table.heading("id",text="Student Id")
        self.student_table.heading("roll",text="Student Roll")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("name",text="name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.column("roll",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("sem",width=100)
        # self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        ######################function###############################

    def add_data(self):
        if self.var_dep.get()=="--Select department--" or self.var_std_name.get()=="" or self.var_roll.get()=="" or self.var_course.get()=="--Select course--" or self.var_div.get()=="--Select division--" or self.var_sem.get()=="--Select sem--":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        if self.var_radio1.get()=="Yes":
            messagebox.showerror("Error","Please click Take Sample Photo button",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("select roll from student_details where roll=%s",(self.var_roll.get(),))
                row=int(len(my_cursor.fetchall()))
                if row>0:
                    messagebox.showerror("Error","Student with same roll already exits",parent=self.root)
                else:
                    messagebox.showinfo("success","You are about to execute",parent=self.root)
                    my_cursor.execute("INSERT INTO student_details (`roll`, `dep`, `course`, `sem`, `std_div`, `std_name`, `email`, `phone`, `photo_sample`)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_sem.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_radio1.get()
                                                                                                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="face_recogniser")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student_details")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        
        self.var_roll.set(data[0])
        self.var_dep.set(data[1])
        self.var_course.set(data[2])
        self.var_sem.set(data[3])
        self.var_div.set(data[4])
        self.var_std_name.set(data[5])
        self.var_email.set(data[6])
        self.var_phone.set(data[7])
        self.var_radio1.set(data[8])
        

    def update_data(self):
        if self.var_dep.get()=="--Select department--" or self.var_std_name.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="face_recogniser")
                    query_cursor=conn.cursor()
                    query=("SELECT roll from student_details where roll=%s")
                    value=(self.var_roll.get(),)
                    query_cursor.execute(query,value)
                    p=query_cursor.fetchall()
                    if len(p)>1:
                        messagebox.showerror("Error","Roll no. cannot be modified.",parent=self.root)
                    else:
                        my_cursor=conn.cursor()
                        my_cursor.execute("UPDATE student_details set dep=%s,course=%s,sem=%s,std_div=%s,std_name=%s,email=%s,phone=%s,photo_sample=%s where roll=%s",(
                                                                                                                                        self.var_dep.get(),
                                                                                                                                        self.var_course.get(),
                                                                                                                                        self.var_sem.get(),
                                                                                                                                        self.var_div.get(),
                                                                                                                                        self.var_std_name.get(),
                                                                                                                                        self.var_email.get(),
                                                                                                                                        self.var_phone.get(),
                                                                                                                                        self.var_radio1.get(),
                                                                                                                                        self.var_roll.get()
                                                                                                                                    ))
                        messagebox.showinfo("Success","Student Details successfully updated",parent=self.root)                                                                                                       
                else:
                    if not update:
                        return 
                
                
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    
    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Student roll no. must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete this student data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="face_recogniser")
                    my_cursor=conn.cursor()
                    sql="DELETE FROM `student_details` WHERE `roll` = %s"
                    val=(self.var_roll.get(),)
                    my_cursor.execute(sql,val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete","Deleted successfully",parent=self.root)
                else:
                    if not delete:
                        return
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
            self.reset_data()
    
    #reset values
    def reset_data(self):
        self.var_roll.set("")
        self.var_dep.set("--Select department--")
        self.var_course.set("--Select course--")
        self.var_sem.set("Select sem")
        self.var_div.set("--Select division--")
        self.var_std_name.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_radio1.set("")


    ######################Generate data set or take photo ############################
    def generate_dataset(self):
        if self.var_dep.get()=="--Select department--" or self.var_std_name.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("select roll from student_details where roll=%s",(self.var_roll.get(),))
                my_result=int(len(my_cursor.fetchall()))
                if my_result>0:
                    messagebox.showerror("Error","Student with same roll already exits",parent=self.root)
                else:
                    id=int(self.var_roll.get())
                    # id=0
                    # for x in my_result:
                    #     id+=1
                    my_cursor.execute("INSERT INTO student_details ( `roll`, `dep`, `course`, `sem`, `std_div`, `std_name`, `email`, `phone`, `photo_sample`)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_sem.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_radio1.get()
                                                                                                    ))
                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    self.reset_data()
                    
                    #################Load predefined data on face frontals from open cv #################
                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                    
                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #scaling factor=1.3
                        #minimum neighbour=5

                        for(x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None: #face_cropped(my_frame) if only my_frame is passed in place of face_cropped(my_frame), then unspecified error(-215) will be shown
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(130,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data set completed!!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    def update_dataset(self):
        if self.var_dep.get()=="--Select department--" or self.var_std_name.get()=="" or self.var_roll.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student_details")
                my_result=my_cursor.fetchall()
                id=int(self.var_roll.get())
                # for x in my_result:
                #     id+=1
                my_cursor.execute("update student_details set roll=%s,dep=%s,course=%s,sem=%s,std_div=%s,std_name=%s,email=%s,phone=%s,photo_sample=%s where roll=%s",(
                                                                                                                                    self.var_roll.get(),
                                                                                                                                    self.var_dep.get(),
                                                                                                                                    self.var_course.get(),
                                                                                                                                    self.var_sem.get(),
                                                                                                                                    self.var_div.get(),
                                                                                                                                    self.var_std_name.get(),
                                                                                                                                    self.var_email.get(),
                                                                                                                                    self.var_phone.get(),
                                                                                                                                    self.var_radio1.get(),
                                                                                                                                    self.var_roll.get()
                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #################Load predefined data on face frontals from open cv #################
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbour=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None: #face_cropped(my_frame) if only my_frame is passed in place of face_cropped(my_frame), then unspecified error(-215) will be shown
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(130,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","data set updated!!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

            

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()