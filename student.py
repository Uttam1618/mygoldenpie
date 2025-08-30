from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

#create the class and call the constructor
class Students:
    def __init__(self,root):
        self.root = root
        self.root.attributes("-fullscreen", True)
        self.root.geometry("1440x900+0+0")
        self.root.title("Face Recognition System")

        #title
        title = Label(self.root, text="Student Management System", font=("Arial", 30, "bold"), fg="black")
        title.place(x=0, y=20, width="1440", height="40")

        #main frame
        main_frame = Frame(self.root, bd=2, relief=RAISED, bg="black")
        main_frame.place(x=10, y= 70, width=1420, height=820)

        #left label frame
        lelf_frame = LabelFrame(main_frame, bd=2, relief=RAISED, text="Student Details",font=("Arial", 18, "bold"))
        lelf_frame.place(x=10, y=73, width=690, height=690)

        #course information 
        course_info = LabelFrame(lelf_frame, bd=2,text="Course information", relief=RIDGE, font=("times new roman", 18, "bold"))
        course_info.place(x=10, y=20, width= 670, height=160)

        ##department
        dep_label = Label(course_info, text= "Department", font=("times new roman", 18, "bold"))
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(course_info, font=("times new roman",16,"bold"), state="readonly")
        dep_combo["values"]=("Select Department", "Faculty of arts and society", "Faculty of science and technology", "Faculty of health", "CDU TAFE (Vocational Education & Training)")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=0, pady=15, sticky=W)

        ##course
        course_label = Label(course_info, text= "Course", font=("times new roman", 18, "bold"))
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(course_info, font=("times new roman",16,"bold"), state="readonly")
        course_combo["values"]=("Select Course", "Arts", "Accounting", "Business", "Art and Society", "Information Technology and Network Engineering", "Engineering (Civil, Electrical/Electronics, Mechanical)", "Community Services and Social Work","Humanities and Social Sciences")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=0, pady=15, sticky=W)

        ##year
        year_label = Label(course_info, text= "Year", font=("times new roman", 18, "bold"))
        year_label.grid(row=2, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(course_info, font=("times new roman",16,"bold"), state="readonly")
        year_combo["values"]=("Select Year", "IT", "Accounting", "Nursing", "Art and Society", "Health")
        year_combo.current(0)
        year_combo.grid(row=2, column=1, padx=0, pady=15, sticky=W)

        ##Semester
        semester_label = Label(course_info, text= "Semester", font=("times new roman", 18, "bold"))
        semester_label.grid(row=2, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(course_info, font=("times new roman",16,"bold"), state="readonly")
        semester_combo["values"]=("Select Semester", "IT", "Accounting", "Nursing", "Art and Society", "Health")
        semester_combo.current(0)
        semester_combo.grid(row=2, column=3, padx=0, pady=15, sticky=W)

        #class student information frame
        students_info = LabelFrame(lelf_frame, bd=2,text="Student Information", relief=RIDGE, font=("times new roman", 18, "bold"))
        students_info.place(x=10, y=190, width= 670, height=450)

        #student ID
        studentid_label = Label(students_info, text= "Student ID:", font=("times new roman", 18, "bold"))
        studentid_label.grid(row=0, column=0, padx=10, sticky=W)

        studentid_entry = ttk.Entry(students_info, width = 16, font=("times new roman", 18, "bold"))
        studentid_entry.grid(row=0, column=1, padx=10, sticky=W)

        #student name
        studentname_label = Label(students_info, text= "Student Name:", font=("times new roman", 18, "bold"))
        studentname_label.grid(row=0, column=2, padx=0, sticky=W)

        studentname_entry = ttk.Entry(students_info, width = 16, font=("times new roman", 18, "bold"))
        studentname_entry.grid(row=0, column=3, padx=10, sticky=W)

         #Class division
        classdivison_label = Label(students_info, text= "Class Division:", font=("times new roman", 18, "bold"))
        classdivison_label.grid(row=2, column=0, padx=10, sticky=W)

        classdivision_entry = ttk.Entry(students_info, width = 16, font=("times new roman", 18, "bold"))
        classdivision_entry.grid(row=2, column=1, padx=10, sticky=W)

        #gender
        gender_label = Label(students_info, text= "Gender:", font=("times new roman", 18, "bold"))
        gender_label.grid(row=2, column=2, padx=0, sticky=W)

        gender_entry = ttk.Entry(students_info, width = 16, font=("times new roman", 18, "bold"))
        gender_entry.grid(row=2, column=3, padx=10, sticky=W)

        #dob
        dob_label = Label(students_info, text= "DOB:", font=("times new roman", 18, "bold"))
        dob_label.grid(row=3, column=0, padx=10, sticky=W)

        dob_entry = ttk.Entry(students_info, width = 16, font=("times new roman", 18, "bold"))
        dob_entry.grid(row=3, column=1, padx=10, sticky=W)

        #email
        email_label = Label(students_info, text= "Email:", font=("times new roman", 18, "bold"))
        email_label.grid(row=3, column=2, padx=0, sticky=W)

        email_entry = ttk.Entry(students_info, width = 16, font=("times new roman", 18, "bold"))
        email_entry.grid(row=3, column=3, padx=10, sticky=W)

        #phone
        phone_label = Label(students_info, text= "Phone:", font=("times new roman", 18, "bold"))
        phone_label.grid(row=4, column=0, padx=10, sticky=W)

        phone_entry = ttk.Entry(students_info, width = 16, font=("times new roman", 18, "bold"))
        phone_entry.grid(row=4, column=1, padx=10, sticky=W)

        #Address
        address_label = Label(students_info, text= "Address:", font=("times new roman", 18, "bold"))
        address_label.grid(row=4, column=2, padx=0, sticky=W)

        address_entry = ttk.Entry(students_info, width = 16, font=("times new roman", 18, "bold"))
        address_entry.grid(row=4, column=3, padx=8, sticky=W)

        #tutor
        tutor_label = Label(students_info, text= "Tutor:", font=("times new roman", 18, "bold"))
        tutor_label.grid(row=5, column=0, padx=10, sticky=W)

        tutor_entry = ttk.Entry(students_info, width = 16, font=("times new roman", 18, "bold"))
        tutor_entry.grid(row=5, column=1, padx=10, sticky=W)

        # radio buttons
        radionbtn1 = ttk.Radiobutton(students_info, text = "take a photo sample", value="Yes")
        radionbtn1.grid(row=6, column=0, padx=10, pady=10)







        #right label frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RAISED, text="Student Details",font=("Arial", 18, "bold"))
        right_frame.place(x=710, y=73, width=700, height=690)



      


#calling the main 
if __name__ == "__main__":
    root = Tk()
    obj = Students(root)
    root.mainloop()