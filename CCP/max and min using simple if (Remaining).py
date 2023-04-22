# #DIctonary 
# # {key:Value}
# mydic = {101:"Kartik", 102: "Rishabh",103:"102", 103: "Aditya"}
# print(mydic)
# a = mydic[101]
# print(a)
# mydic[102]="Mehul"
# print(mydic)

# mydic1 = {111:"Arvind"}

# # OPERATORS
#Identity operators
# a=10
# b=10
# print(a is b)
# print(b is not a)

#membership operators
# in
#not in

#conditional operators
# using simple if
# max and min using simple if

# a =int(input("Enter value: "))
# if a>0:
#     print("Given number is +ve")
# if a<0:
#     print("Given number is -ve")
# if a == 0:
#     print("Number is zero")
# a = int(input("Enter value: "))
# b = int(input("Enter value: "))
# c = int(input("Enter value: "))
# d = int(input("Enter value: "))
# e = int(input("Enter value: "))

# if a>b and a>c and  a>d and a>e:
#     print("A has the maximum value")
# if b>a and b>c and b>d and b>e:
#     print("B is the greatest")
# if c>a and c>b and c>d and c>e:
#     print("C is max")
# if d>a and d>b and d>c and d>e:
#     print("D is max")
# if e>a and e>b and e>c and e>d:
#     print("E is greatest")

# #min
# p = int(input("Enter the value: "))
# q = int(input("Enter the value: "))
# r = int(input("Enter the value: "))
# s = int(input("Enter the value: "))
# t = int(input("Enter the value: "))
# if p<q and p<r and p<s and p<t:
#     print("P is Min")
# if q<p and q<r and q<s and q<t:
#     print("Q is Min")
# if r<p and r<q and r<s and r<t:
#     print("R is Min")
# if s<p and s<q and s<r and s<t:
#     print("S is Min")
# if t<p and t<q and t<r and t<s:
#     print("T is Min")

# x = int(input("Enter the value: "))
# y = int(input("Enter the value: "))
# if x>y:
#     print("X is big")
# else:
#     print("Y is greater")

# if elif else

# a = int(input("Enter value: "))
# b = int(input("Enter value: "))
# if a>b:
#     print("A is Greater")
# elif b>a:
#     print("B is Greater")
# else:
#     print("Both are Equal")

# # Logical operators
#AND
# p1 = int(input("enter value: "))
# p2= int(input("enter value: "))
# p3 = int(input("enter value: "))
# p4 = int(input("enter value: "))
# p5 = int(input("enter value: "))
# p6 = int(input("enter value: "))
# p7 = int(input("enter value: "))
# if p1>=40 and p2>=40 and p3>=40 and p4>=40 and p5>=40 and p6>=10 and p7>=10:
#     print("Pass")
# else:
#     print("Fail")
# total = p1+p2+p3+p4+p5
# percentage = total/5
# print("total marks: ", total)
# print("Percentage acquired: ", percentage)

#OR
# ch = str(input("Enter any character: "))
# if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
#     print("Vowel")
# else:
#     print("Consonent")

# QUESTION
# ch = str(input("Enter any character: "))
# if ch>='a' and ch<='z':
#     print("Character is lowercase")
# elif ch>="A" and ch<="Z":
#     print("Character is uppercase")
# elif ch>="0" and ch<="9":
#     print("Chacter is Numeric")
# else:
#     print("Given character is Special Symbol")
# # QUESTION
# p1=int(input("Enter Percentage")) #65

# if p1>=40 and p1<=60:
#     print("Grade is C")
# elif p1>=60 and p1<=80:
#     print("Grade is B")
# elif p1>=80 and p1<=90:
#     print("Grade is A")
# else:
#     print("Grade is Excellent")