### ABSTRATION

# from abc import ABC, abstractmethod
# class Programming(ABC): #abstract class
#     @abstractmethod
#     def training(self): #abstract method
#         pass

#     @abstractmethod #absent method
#     def placement(self):
#         pass

# class Ashish(Programming):
#     def training(self):
#         print('C,C++,Java')
#     def placement(self):
#         print("Java placement")

# class Ankush(Programming):
#     def training(self):
#         print("Python | Django")
#     def placement(self):
#         print("Python Placement")

# class Rishabh(Programming):
#     def training(self):
#         print("Machine Learning")
#     def placement(self):
#         print("Data Science Placement")

# obj1= Ashish()
# obj1.training()
# obj1.placement()
# obj2=Ankush()
# obj2.training()
# obj2.placement()
# obj3=Rishabh()
# obj3.training()
# obj3.placement()


# # # #ABSTRACT IRTC EXAMPLE

# from abc import ABC, abstractmethod
# class Irctc(ABC): #abstract class
#     @abstractmethod
#     def TicketbookingTi(self): #abstract method
#         pass
#     @abstractmethod
#     def display(self,source,destination,date):
#         pass

# class MMT(Irctc):

#     def TicketbookingTi(self):
#         print("========Welcome to MTM========")
#         source =input("Enter a source destination ")
#         destination =input("Enter a destination")
#         date = input("Enter date ")
    
#     def display(self, source, destination, date):
#         print("Source= ",source)
#         print("Destination= ",destination)
#         print("Date= ",date)

# class GoIbibo(Irctc):

#     def TicketbookingTi(self):
#         print("        Welcome to GoIbibo             ")
#         source =input("Enter a source destination ")
#         destination =input("Enter a destination")
#         date = input("Enter date ")

#     def display(self, source, destination, date):
#         print("Source= ",source)
#         print("Destination= ",destination)
#         print("Date= ",date)

# class Yatra(Irctc):

#     def TicketbookingTi(self):
#         print("======Welcome to Yatra==========")
#         source =input("Enter a source destination ")
#         destination =input("Enter a destination")
#         date = input("Enter date ")

#     def display(self, source, destination, date):
#         print("Source= ",source)
#         print("Destination= ",destination)
#         print("Date= ",date)

# m=MMT()
# m.TicketbookingTi()
# m.display()

# g=GoIbibo()
# g.TicketbookingTi()
# g.display()

# y=Yatra()
# y.TicketbookingTi()
# y.display()


# # # # # #ENCAPSULATIONS - LAST OOPS
# class Base: #abstract class
#     def __init__(self) -> None:
#         print("Parent class constructor called ")
#         self.a = "YCCE" #public data menber
#         self._c = "IIM" #private member

# # Creating a derived class/ child class
# class Derived(Base): #child class
#     def __init__(self) -> None:
        
#         #calling constructor of
#         # Base class
#         Base.__init__(self)
#         print("Calling private member of base classs: ")
#         # print(self.__c)
# #driver code
# obj1 = Derived()
# # print(obj1.a)
# # print(obj1.c)
# obj2 = Base()
# # print(obj2.c)

# class Base:
#     def __init__(self) -> None:
#         print("parent classs constructor called")
#         self._a = 2 #Protected menber
# #creating a derived class
# class Derived(Base): #child class
#     def __init__(self) -> None:
#         #Calling constructor of
#         #Base class
#         Base.__init__(self)
#         print("Calling protected member of base class: ")
#         print(self._a)

# obj1 = Derived()


# # # ## # ALGORITHM
# num = 123
# a = num%10
# print(a)

# Question given by sir
# paisa=[2000,1000,500,200,100,50,20,10,5,2,1]
# value = int(input("Enter Amount: "))
# for i in paisa:
#     j=i
#     count=0
#     while value>=j:
#         count+=1
#         value = value - j
#     print(i,"=",count)

value = int(input("Enter number: "))

nums = [2,5,5,5,6,6,8,9,9,9]
