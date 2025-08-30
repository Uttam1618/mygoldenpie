from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

#create the class and call the constructor
class face_recognition_system:
    def __init__(self,root):
        self.root = root
        self.root.attributes("-fullscreen", True)
        self.root.geometry("1440x900+0+0")
        self.root.title("Face Recognition System")

# add a title label
        title_lbl = Label(self.root, text="Face Recognition System", font=("Arial", 30, "bold"), fg="black")
        title_lbl.place(x=0, y=25, width=1440, height=60)
#add an details button
        attendence_btn = Button(self.root, text="Details", cursor="hand2", font=("arial", 20, "bold"), bg="navy", fg="black")
        attendence_btn.place(x=600, y=100, width=210, height=50)
        #face detector for the week 
        attendence_btn2 = Button(self.root, text="face detector", cursor="hand2", font=("arial", 20, "bold"), bg="navy", fg="black")
        attendence_btn2.place(x=600, y=150, width=210, height=50)
        #Attendence button 
        btn3 = Button(self.root, text="Attendence", cursor="hand2", font=("Arial", 20, "bold"), bg="navy", fg="black")
        btn3.place(x=600, y=200, width=210, height=50)
        #Help button 
        btn3 = Button(self.root, text="Help desk", cursor="hand2", font=("Arial", 20, "bold"), bg="navy", fg="black")
        btn3.place(x=600, y=250, width=210, height=50)
         #trian data button 
        btn3 = Button(self.root, text="Train Data", cursor="hand2", font=("Arial", 20, "bold"), bg="navy", fg="black")
        btn3.place(x=600, y=300, width=210, height=50)
         #photos button 
        btn3 = Button(self.root, text="Photos", cursor="hand2", font=("Arial", 20, "bold"), bg="navy", fg="black")
        btn3.place(x=600, y=350, width=210, height=50)
         #develpor button 
        btn3 = Button(self.root, text="Developer", cursor="hand2", font=("Arial", 20, "bold"), bg="navy", fg="black")
        btn3.place(x=600, y=400, width=210, height=50)
         #exit button 
        btn3 = Button(self.root, text="Exit", cursor="hand2", font=("Arial", 20, "bold"), bg="navy", fg="black")
        btn3.place(x=600, y=450, width=210, height=50)








#calling the main/start the application 
if __name__ == "__main__":
    root = Tk()
    obj = face_recognition_system(root)
    root.mainloop()
