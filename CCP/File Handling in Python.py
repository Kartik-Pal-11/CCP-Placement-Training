# for i in range(1,10):
#     if i==5:
#         break
#     print(i)

# # To know how much index number is present in given name
# name=input("Enter name: ")
# #prashant
# #01234567
# i =0
# for x in name : #x
#     if x== 'n':
#         print("The character present at index no",i,"value=:",x)
#         break
#     i = i+1
# # Skip looping
# for i in range(1,10):
#     if i==5:
#         continue
#     print(i)

# mycart = [10,20,200,300,800,60,700]

# for i in mycart:
#     if i>400:
#         print("THis my purchased card item")
#         continue
#     print(i)

# # Using zip function for multi range
# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i == 3 and j==3:
#         continue
#     print(i," ",j)
    
    # # # #
    # # # # WHILE LOOP
# i=0
# while i<6:
#     i=i+1
#     if i ==3:
#         continue
#     print(i)

# i=0
# while i<6:
#     i=i+1
#     if i ==3:
#         break
#     print(i)

# name=""
# while name!="prashant":
#     name=input("Enter name:")

# print("Entered Valid name")


# #E # # # ## # IMPORTANT QUESTION
# continue1 = "y"
# while continue1 == "y":
#     print("1. add")
#     print("2. mul")
#     print("3. div")
#     print("4. sub")
#     choose = int(input("Enter your choice: "))
#     num1 = int(input("Enter value for 1st number"))
#     num2 = int(input("Enter 2nd value"))

#     if choose==1:
#         add=num1+num2
#         print(add)
#     elif choose==2:
#         mul=num1*num2
#         print(mul)
#     elif choose==3:
#         div=num1/num2
#         print(div)
#     elif choose==4:
#         sub=num1-num2
#         print(sub)
#     else:
#         print("Invalid")
#     continue1 = input("Do U Wish to continue(Y/N)")

# mylist=[2,3,4,4,2,5,2,1,5,5,4,4] #Remaining

# # # # # FUNCTIONS
# def add():
#     print(2+2)
# add()
# add()

# # # Login logoc with using function
# def login():
#     while True:
#         username = input("Enter username")
#         password = input("Enter password")
#         if username == password:
#             print("Login Successful")
#             break # idhar break daalne se login ke baad dubara turant login nhi ayega
#         else:
#             print("Wrong credentials")
# login()

# def info(firstname,lastname):
#     print('First name=', firstname)
#     print('Last name=',lastname)
# info("Kartik","Pal")

# def add(num1,num2):
#     return num1+num2

# print(add(2,3))

# def add (num1,num2):
#     return num1+num2

# result = add(2,3)
# print(result)

###MULTIPLE RETURN FINCTION
# # Positional argument
# def arithmatic(a,b):
#     r = a+b
#     n = a*b
#     m = a-b 
#     return r,n,m
# result = arithmatic(10,5)
# print("Result= ",result)

# # KEYWORD ARGUMNET
# with added/given input
# def func(fname.lname):
#     print("Hi",fname)
#     print("Hi",lname)

# func(fname="kartik",lname="pal")

# # with input to be taken
# def func(fname.lname):
#     print("Hi",fname)
#     print("Hi",lname)
# fname = input("Enter first name")
# lname = input("Enter last number")
# func(fname, lname)

##DEFAULT ARGUMENT
# def func(city = "Nagpur"):
#     print("I am from ", city)

# func("Delhi")
# func("LA")
# func()

# # # # VARIABLE LENGTH ARGUMENT
# def name(*name):
#     print(name)

# name("Kartik","rishabh","Akshay",2002)

# # # LOCAL AND GLOBAL VARIABLE
# x = 0
# def info_one():
#     #Global x
#     x=17
#     print("X=",x)
# def info_two():
#     print("X=",x)

# info_one()
# info_two()

# fname = ""
# lname = ""

# def getpersonaldetail(fname,lname):
#     fname = input("Enter your first name: ")
#     lname = input("Enter your last name: ")
# getpersonaldetail(fname.lname)

# global college_name,Year,branch,Roll_no

# def getcollegedetail(college_name,Year,branch,Roll_no):
#     college_name = input("Enter your college name: ")
#     Year = input("Year you study")
#     branch = input


# # # FILE HANDLING IN PYTHON
# f = open("myfile.txt","w")
# print("name of file",f.name)
# print("file mode",f.mode)
# print(" readeble ",f.readable())
# print(" writeable ",f.writable())
# print(" file has closed",f.closed)
# f.close()
# print(" file has closed",f.closed)

# f =open("covid.txt","w")
# f.write("\n Bhayander is fully vaccinated")
# f.close()
# print("Job done")

# INPUT AND DEVELOP A CSV FILE
# import csv
# f = open("student.csv","a", newline="")
# a = csv.writer(f)
# # a.writerow(["studentID","rollno","name","mobileno"])
# studentid=int(input(""))
# rollno =int(input(""))
# name =input("")
# mobileno =int(input("")) 

# a.writerow([studentid,rollno,name,mobileno])
# print("student record has save")



# # # # # # # #NEW PROGRAM
# NO OFF RECORD
# import csv

# f = open("student.csv","a",newline = "")
# a = csv.writer(f)
# # a.writerow(["studentId","name","roll no", "email id", "address", "mobileno", "p1", "p2", "p3", "p4", "p5", "total", "percentage", "Result"])
# studentId = int(input("Enter your student id: "))
# name = input("Enter name: ")
# rollno = int(input("Enter rollno: "))
# email = input("Enter email: ")
# address = input("Enter address: ")
# mobileno = input("Enter mobile no: ")
# p1 = int(input("Enter marks in p1:     "))
# p2 = int(input("Enter marks in p2:     "))
# p3 = int(input("Enter marks in p3:     "))
# p4 = int(input("Enter marks in p4:     "))
# p5 = int(input("Enter marks in p5:     "))
# total = p1+p2+p3+p4+p5
# percentage = total/5.0

import csv

def invalidTnput():
    print("Please Enter Valid Input")
def create():
    f = open("student.csv","a",newline = "")
    a = csv.writer(f)
    # a.writerow(["studentId","name","roll no", "email id", "address", "mobileno", "p1", "p2", "p3", "p4", "p5", "total", "percentage", "Result"])
    records = int(input("Enter no of records"))
    while records>0:
        try:
            studentId = int(input("Enter your student id: "))
            name = input("Enter name: ")
            rollno = int(input("Enter rollno: "))
            email = input("Enter email: ")
            address = input("Enter address: ")
            mobileno = input("Enter mobile no: ")
            p1 = int(input("Enter marks in p1:     "))
            p2 = int(input("Enter marks in p2:     "))
            p3 = int(input("Enter marks in p3:     "))
            p4 = int(input("Enter marks in p4:     "))
            p5 = int(input("Enter marks in p5:     "))
        except:
            total = p1+p2+p3+p4+p5
            percentage = total/5.0
            if p1<40 or p2<40 or p3<40 or p4<40 or p5<40:
                result = "fail"
            else:
                result = "pass"
        a.writerow([studentId,name,rollno,email,address,mobileno,p1,p2,p3,p4,p5,total,percentage,result])
        if name == "Aditya":
            print()
        records-=1


    print("student data has saved")

def readRecord():
    # f = open("student.csv","r")
    with open("student.csv") as f:
        a = csv.reader(f)
        id = input("Enter id to display: ")
        for i in a:
            if i[0]==id:
                print(i)
try:
    choice = int(input("Enter your choice: 1. Enter student data, 2. Read Student record"))
    if choice!=1 or choice!=2:
        invalidInput()
except:
    if choice == 1:
        create()
    if choice == 2:
        readRecord()

# f = open("dhoni.jpg","rb")
# w = open("def.png","wb")
# data = f.read()
# w.write(data)