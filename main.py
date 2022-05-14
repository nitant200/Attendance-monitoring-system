from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")      
        
         # first imag
        img=Image.open(r"C:\Users\nitan\Desktop\Face_Recognition_System\college_images\coder.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        
        img1=Image.open(r"C:\Users\nitan\Desktop\Face_Recognition_System\college_images\facialrecognition.webp")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        img2=Image.open(r"C:\Users\nitan\Desktop\Face_Recognition_System\college_images\coder.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        # bg img
        img3=Image.open(r"C:\Users\nitan\Desktop\Face_Recognition_System\college_images\coder.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # stude button
        img4=Image.open(r"C:\Users\nitan\Desktop\Face_Recognition_System\college_images\student.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bl=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        bl.place(x=200,y=100,width=220,height=220)

        bl=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bl.place(x=200,y=300,width=220,height=40)

        # detect face
        img5=Image.open(r"C:\Users\nitan\Desktop\Face_Recognition_System\college_images\face detection.png")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        bl=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        bl.place(x=500,y=100,width=220,height=220)

        bl=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bl.place(x=500,y=300,width=220,height=40)

        # Attendance face
        img6=Image.open(r"C:\Users\nitan\Desktop\Face_Recognition_System\college_images\attendance.png")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        bl=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        bl.place(x=800,y=100,width=220,height=220)

        bl=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bl.place(x=800,y=300,width=220,height=40)

        

        # Train face
        img8=Image.open(r"C:\Users\nitan\Desktop\Face_Recognition_System\college_images\train.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        bl=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        bl.place(x=200,y=380,width=220,height=220)

        bl=Button(bg_img,text="Train data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bl.place(x=200,y=580,width=220,height=40)

        # photo face
        img9=Image.open(r"C:\Users\nitan\Desktop\Face_Recognition_System\college_images\detection.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        bl=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        bl.place(x=500,y=380,width=220,height=220)

        bl=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bl.place(x=500,y=580,width=220,height=40)


        # exit face
        img10=Image.open(r"C:\Users\nitan\Desktop\Face_Recognition_System\college_images\exit.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        bl=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.iExit)
        bl.place(x=800,y=380,width=220,height=220)

        bl=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bl.place(x=800,y=580,width=220,height=40)

       
    

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure",parent=self.root)
        if self.iExit >0:
           self.root.destroy()
        else:
            return        

    # =====Function button=====

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

        



    








if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
    
    