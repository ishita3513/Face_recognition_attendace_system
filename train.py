from tkinter import*
from tkinter import ttk
from turtle import hideturtle
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import cv2
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",35,"bold"),bg="lightblue",fg="white")
        b1_1.place(x=630,y=250,width=300,height=200)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #grey scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Traininig",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #==================== Train the classifier and save =================#

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","training datasets completed!!!",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()