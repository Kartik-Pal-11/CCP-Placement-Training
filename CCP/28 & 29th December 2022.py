### Object oriented programming
#             |     |
#             |     |
#             \    /
#              \  /
#               \/
# # 1.CLASS
# class New: #New ka N bada hona jaruri hai
#     x=10 # data member inside of class
#     def display(self): # data member function of class |||||||idhar self by default hota hai
#         print('hello python')   
# obj = New()
# obj.display()
# print(obj.x)
#print(obj.a)

# # 2.CONSTRUCTOR
# Constructor is called automatically when object is formed
# class NewClass:
#     def _init_(self):  #constructor
#         print("my name is constructor and i allways execute first")

#     def show(self): #member function inside of class
#         print('Welcome to class level programming')
# obj = NewClass()
# obj.show()
# obj2 = NewClass()

# class Hod:
#     def _init_(self):
#         self.name='aditya' #data member
#         self.age=21
#         self.empid=1001

#     def info(self):
#             print("My name is :",self.name)
#             print("My Age is:",self.age)
#             print("My emp id",self.empid)

# obj = Hod() #object create
# obj.info()


# # declaring instance variable inside a constructor by using self variable.

# class Student():
#     def __init__(self):
#         self.sname = "aditya"
#         self.lname = "rai" #instance variable
#         self.srollno = 101
#         self.sbranch = 'CS'
#         self.smb = 0000000000

# obj = Student()
# print(obj.__dict__)

# self variable
# class Student:
#     def __init__(self):
#         self.sname = "aditya"
#         # self.lname = "rai" #instance variable
#         self.srollno = 101
#         self.sbranch = 'CS'
#         # self.smb = 0000000000
#     def getdata(self):
#         self.smb    = 28282828282

# obj = Student()
# #obj.getdata()
# print(obj.__dict__)

#declaring instance variable outside a class by using object
# class Student:
#     def __init__(self) -> None:
#         self.sname = 'rishabh'
#         self.srollno = 101

#     def getdata(self):
#         self.smb = 28282828282

# obj = Student()
# obj.getdata()
# obj.sbranch = 'cs'
# print(obj.__dict__)

#accessing and deleting instance variable from the class
# class Student:
#     def __init__(self) -> None:
#         self.sname=input("Enter name")
#         self.srollno = 101

#     def getdata(self):
#         self.smb = 282828282

# obj = Student()
# obj.getdata()
# obj.sbranch="cs"    #adding instance variable by using object
# del obj.srollno     #dele
# print(obj.sname)
# print(obj.__dict__)


# print(obj.__dict__)

# 29th December 2022
# # #STATIC Variable
# class College:
#     collegename= "Modern College" #static variable (1 memory)

#     def __init__(self):
#         self.studentname= "prashant" #instance variable (3 seperate memory)

# principle = College() #object creation
# teacher = College()
# accountant = College()
# print("principle =",principle.collegename,"....",principle.studentname)
# print("teacher=",teacher.collegename,"....",teacher.studentname)
# print("accountant=", accountant.collegename,"...",accountant.studentname)

# College.collegename="HBD" #second way to add static variablr
# principle.studentname="kartik pal"

# print("principle=",principle.collegename,"|",principle.studentname)
# print("teacher=",teacher.collegename,"|",teacher.studentname)
# print("accountant=", accountant.collegename,"|",accountant.studentname)


# # # INSTANCE METHOD

# class Student:
#     def __init__(self, name, rollno,mob):
#         self.name=name #instance variable
#         silf.rollno=rollnoself.mob = mob
#     def dispaly(self): #instance method
#         print(self.name," ",self.rollno," ",self.mob)

# stud = Student("kartik", 1001,6464646464)
# stud.display()

# # #  STSTIC METHOD
# class Student:
#     #by using class name we can access static method
#     @staticmethod #decorator
#     def get_personal_detail(fname,lname):
#         print("your personal detail=", fname,lname)

#     @staticmethod
#     def contact_detail(mobil_no, rollno):
#         print("your contact detail=",mobil_no,rollno)

# Student.get_personal_detail("prashant","jha")
# Student.contact_detail(5456454646,1001)

# # # # #INHERITANCE

#N # # # SINGLE LEVEL
# class college: #parent class
#     def college_name(self):
#         print("Modern College")

# class Student(college): #child class
#     def student_info(Self):
#         print("Name: Kartik Pal")
#         print("Branch: AIML")

# obj = Student()
# obj.college_name()
# obj.student_info()

# # # # # MULTI LEVEL INHERTIANCE
# class college: #first class  first level
#     def college_name(self):
#         print("Modern College")

# class Student(college): #Second class second level
#     def student_info(Self):
#         print("Name: Kartik Pal")
#         print("Branch: AIML")

#     class Exam(Student): #child class
#         def subject(self):
#             print("Subject1: Designe engineering")
#             print("Subject1: Designe engineering")
#             print("Subject: C-Language")
# obj = Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()

# # # # # MULTIPLE INHERTIENCE

# class SubjMarks: # class-1
#     math = int (input("Enter paper marks of math"))
#     DE = int (input("Enter paper marks of designe engineering"))
#     C= int.input("Enter paper marks of C language")
#     english = int(input("Enter paaper marks of english"))
# #=====-===---===================== parent class -1
# class PractMarks: # class-2
#     cpract = int(input("Enter practicals marks of c language"))
# # H==2
# # parent class -2
# class Result(SubjMarks,PractMarks): # child class
#     #print("if student pass in both = subject and practical paper then pass")
#     def total(self):
#         if self.math>=40 and self.DE>=40 and self.c>=40 and self.english>=40 and aelf.english>=40 and self.english>=40:

# self.cpract>-20
# print("pask")
# else:
#     print("fail")
# obj = Result()
# obj.total()

# # GIVEN QUESTION CLASSES HOSPITAL,PATIEBT<HOSPITALSTAFF<PHARMACY
# class Hospital: #class-1
#     hname=input("Enter Hospittal Name: ")
#     doctor_name=input("Doctors name")
#     Feild=("Enter Hospital Spllization")
#     data=input("Enter data of joining")
# class HospitalStaff:
#     sname=input("Enter staff name: ")
#     vname=input("Enter visitor name: ")
# class Pharmacy:
#     pname=input("Enter pharmacy name: ")
#     dawa=input("Enter medicine name: ")
# class Patient(Hospital,HospitalStaff,Pharmacy):
#     def mariz(self):
#         patientname=input("Enter patient name: ")
#         urname=input("Enter your name: ")
#         print("Hello {urname}. Below are the details required: ")
#         print("Hospital Name: ",self.hname)
#         print("Doctor name= ",self.doctor_name)
#         print("Specialization: ",self.Feild)
#         print("Patient Date of joining: ",self.data)
#         print("Vistor name: ",self.sname)
#         print("Pharmacy name: ",self.pname)
#         print("Mediceine name: ",self.dawa)

# obj = Patient()
# obj.mariz()





# # # # # # # # # POLYMORPHISM

# class Principal:
#     def role(self):
#         print("I am managing all activity of college")
    
# class Dean:
#     def role(self):
#         print("I am decision taking person")

# class HOD:
#     def role(self):
#         print("I have responsibility if Teachers and students")

# class Faculty:
#     def responsibility(self):
#         print("I have to complete syllabus")

# # ======================== class declaration complete ===================          { RESPONSIBILITY WALLA REMINING}
# def func(obj): # called func obj = 1:Dean
#     obj.role()  #calling func
#     obj.responsibility()

# campus=[Principal(),Dean(),HOD()]
# for obj in campus: #obj=[0:Principal,1:Dean,2:HOD,3:Faculty]
#     func(obj) #calling fun

# camp1=[Faculty()]
# for obj in camp1:
#     func(obj)

# # # # # #OPERATOR OVERLOADING

# class Deposit:
#     def __init__(self,cash):
#         self.cash = cash

# d1=Deposit(1000)
# d2=Deposit(2000)
# print(d1+d2)   # d1 & d2 operand

        #     /\
        #    /  \    error ayega 
        #   /____\      To be solved using #magic method


#magic operator is available for every operator. To overload any operator we have to override that Method in our class.
# the __add__ method is a magic method which gets called when we two numbers using the+ operator.

# class Deposit:
#     def __init__(self,cash):
#         self.cash = cash

#     def __add__(self,other):
#         return self.cash + other.cash

# d1=Deposit(1000)
# d2=Deposit(2000)
# print("Total cash deposit amount=",d1+d2)

## implemented using magic method

# # # ##OTHER MAGIC METHODS
# detepad
# object._ add_ (self,other)
# ==>
# object.sub (self,other)
# ==>
# ==> o bject._ mul_(self,other)
# object.__ div_ (self,other)
# ==>
# //==> o bject. _ floordiv_(self,other)
# object. mod_ (self,other)
# % ==>
# object.pow(self,other)
# "*==>
# += ==> object. _ iadd_(self,other)
# = ==> object._ isub_ (self,other)
# *= ==> object.__ imul_ (self,other)
# /= ==> object._ idiv_ (self,other)
# //= => object.__ ifloordiv_ (self,other)
# %= => object._imod (self,other)
# *= => object.__ ipow_ (self,other)
# object.lt(self,other)
# <= ==> object._ le_ (self,other)
# ==> object. gt (self,other)
# >= ==> object.ge (self,other)

# # # PYTHON DO NOT SUPPORT FUNCION OVERLOADING/METHOD OVERLOADING

##In if we try to declare multiple methods with sa,e name and different numbers of argumetns then pythin wil always consider only last method.

# class Arithmatic:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
    
# obj = Arithmatic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,3)          ##Ye run nhi karega = ERROR dega


# # #CONSTRUCTOR OVERLOADING


# # # # # ## # # #CONSTRUCTOR OVERLOADING IS NOT POSSIBLE IN PYTHON>
#In if we try to declare multiple constructors then the last constructor will be considered.

# class Arithmatic:
#     def __init__(self) -> None:
#         print("There is no argument")
#     def __init__(self) -> None:
#         print("passing one argument")
#     def __init__(self) -> None:
#         print("passing two arguments")

# obj = Arithmatic()
# obj = Arithmatic(10)
# obj = Arithmatic(2,2)

#  # # # METHOD OVERRIDING


# # # idhar hari om aur uske papa ka example diya tha
# class Father:  #parent class
#     def bike(self):
#         print("Harley Devidson")

#     def laptop(self):
#         print("Laptop with 2GB RAM and 500GB HDD I3 processor")

# class Aman(Father):
#     def laptop(self):
#         print("As per my programming software this is not cool for me")
#         print("Laptop with 8GB Ram and 1TB HDD I7")
    
# obj = Aman()
# obj.bike()
# obj.laptop()


# # # how to make laptop accepted using super()
# class Father:  #parent class
#     def bike(self):
#         print("Harley Devidson")

#     def laptop(self):
#         print("Laptop with 2GB RAM and 500GB HDD I3 processor")

# class Aman(Father):
#     def laptop(self):
#         print("As per my programming software this is not cool for me")
#         print("Laptop with 8GB Ram and 1TB HDD I7")
    
#         super().laptop()
# obj = Aman()
# obj.bike()
# obj.laptop()

####################################################################################################

# class Father:
#     def __init__(self) -> None:
#         print("Father:= o am on time at breakfast table")

# class Child(Father):
#     def __init__(self):
#         #using super() method we can call parent classs constructor
#         print("Child:=i will be late for breakfast")
#         super().__init__()

# obj = Child()





# +++++++++++++++++++++++ SIR KA DIYA EK BADA PROGRM+++++++++++++++++++++++++==========
choice =0 # global variable
class Exam(object):
    def __init__(self):
        self.sname=None
        self.collegename=0
        self.classname=0
        self.rollno=0
        self.login() # calling function
    def login(self): # constructor part (called function)
        print("======================================")

        username=input("Enter username")
        password=input("Enter password")

        print("=======================================")
        print()
            #Login Section
        if username == password:
            print("Login successfully")
            self.getdata() # calling function
        else:
            print("Login fail try again")

#=======================================================================================================

        print()
    #Enter Your Profile Detail
    def getdata(self):
        self.sname  = input("Enter Your Name")
        self.collegename = input("Enter your college name")
        self.classname = input("Enter ypur class name")
        self.rollno = input ("Enter Your Roll number")
        print()
        #===================================End of Profile
# Section===========================================
    # static subject declaratin
        print("choose any branch for giving exam")
        print("1. Mechanical Engineering")
        print("2. Information Technology")
        print("3.Computer Science")
        print("4.Civil Engineering")
        print()

        choice = int(input("Enter your choice")) # subject selection logic part
        if choice==1:
            self.mechanical() #calling function
        elif choice == 2:
            pass 
        elif choice==3:
            pass
        elif choice==4:
            pass
        else:
            print("you have entered wrong choice")

    # called function part
def mechanical(self):
    print("1. First Semester")
    print("2.Second Semester")
    print("Enter your Sem number ")
    # logical part
    choice = int(input("Enter your choice"))
    if choice == 1:
        #first_subj() #calling function
        print("Math")
    elif choice == 2:
        pass #second_subj()

def information(self):
    print("1. First semester")
    print("2. Second Semester")
    choice = int(input("Enter your choice"))
    if choice == 1:
        pass
    elif choice ==2:
        pass

def computer(self):
    print("1. First Semester")
    print("2. Second Semester")
    choice =input("Enter your choice")
    if choice == 1:
        pass
    elif choice== 2:
        pass

def civil(self):
    print("1. First Semister")
    print("2. Second Semister")
    choice =input("Enter your choice")
    if choice == 1:
        pass
    elif choice== 2:
        pass
#object creation of class
#obj =Exam()
#obj.login()
#===============================================================================end=======================================================================
# Examination Calculation part
class Calculation(object):
    def __init__(self):
        self.stat-0
        self.dmgt=0
        self.cg =0
        self.toc =0
        self.math=0
        self.total=0
        self.percentage=0
        self.ps=0
        print()
        print("Do You Want To Put Examination Marks Enter yes/No")
        print()
        Yes = input("Enter yes/no")
        if Yes == "yes":
            self.calculatemarks() # calling function
        else:
            print("Thank You For Visiting Here")
        print()
# taking a marks for subject
    def calculatemarks(self):
        self.stat = int(input("Enter Marks Of Statistics:"))
        self.dmgt = int(input("Enter Marks Of DMGT:"))
        self.cg - int (input("Enter Marks Of CG):"))
        self.toc = int(input("Enter Marks Of TOC):"))
        self.math = int(input("Enter Marks Of Mathl:"))
        print()
        if self.stat >=40 and self.dmgt>=40 and self.cg>=40 and self.toc>=40 and self.math>=40:
            self.ps-"pass"
            print("You are pass")
        else:
            self.ps="Fail"
            print("You are fail")

        self.total = self.stat+self.dmgt+self.cg+self.toc+self.math
        self.percentage = self.total/5.0

#obj1 = Calculation()
#==================================================================================================================================================

#Assesment class

class Assesment(Exam, Calculation): #multiple inhertance
    def __init__(self): #child class constructor
        Exam.__init__(self)  #calling parent class constructor
        Calculation.__init__(self)

    def result(self):

        print("================================================================================================")
        print("                                                                                                ")
        print("                             College Name: ",self.collegename ,"                                ")
        print("                                                                                                ")
        print("================================================================================================")

        print("|                            Student Name: ", self.sname, "                                    |")
        print("|                            Class Name: ", self.classname, "                                  |")
        print("|                            Roll Name: ", self.rollno, "                                      |")
        print("================================================================================================")
        print("                                                                                                ")
        print("                   Subject Name   :   Total Marks     :Obtained Marks  :                        ")

        print("                                                                                                ")
        print("                     Statistics     :",  "  100  "   "  :",  self.stat,                       ":")
        print("                     DMGT           :",  "  100  "   "  :",  self.dmgt,                       ":")
        print("                     CG             :",  "  100  "   "  :",  self.cg,                         ":")
        print("                     TOC            :",  "  100  "   "  :",  self.toc,                        ":")
        print("                     Math           :",  "  100  "   "  :",  self.math,                       ":")
        print("================================================================================================")
        print("                                                                                                ")
        print("                     Result Status  :",                                              self.ps,"  ")
        print("                     Total Marks    :",   "500",                                             "  ")
        print("                     Obtained Marks :",                                           self.total,"  ")
        print("                     Percentage     :",    self.percentage,                                  "  ")
        print("================================================================================================")

obj2 = Assesment()
obj2.result()