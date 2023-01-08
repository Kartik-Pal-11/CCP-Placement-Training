# a = int(input("Enter no: "))
# b = int(input("Enter no: "))
# # print(a/b)
#             |     |
#             |     |
#             \    /
#              \  /
#               \/

# a = int(input("Enter no: "))
# b = int(input("Enter no: "))
# try:
#         print(a/b)
# except:
#     print("Can't divide by xero")

# try:
#         print(2/0)
# except ZeroDivisionError as message:
#         print("The description of exception:",message)

# #Multiple accept block
# try:
#         a = int(input("Enter no: "))
#         b = int(input("Enter no: "))
#         print(a/b)
# except ZeroDivisionError as message:
#         print("plz ensure that you can't divide any no by zero: ",message)
# except ValueError as message:
#         print("Enter only integer no=>", message)

# # Muktile accept block
# try:
#         a = int(input("Enter no: "))
#         b = int(input("Enter no: "))
#         print(a/b)
# except (ValueError,ZeroDivisionError) as message:
#         print(message)

# # # Multiple access block with default
# try:
#         a = int(input("Enter no: "))
#         b = int(input("Enter no: "))
#         print(a/b)
# except (ValueError,ZeroDivisionError) as message:
#         print(message)
# except:
#         print("This is default part of except block")

# try:
#         a = int(input("Enter no: "))
#         b = int(input("Enter no: "))
#         print(a/b)
# except:
#         print("This is default part of except block")

# except (ValueError,ZeroDivisionError) as message:
#         print("Enter correct number: "message)

# # Multiple accept with else
# try:
#         a = int(input("Enter no: "))
#         b = int(input("Enter no: "))
#         print(a/b)
# except (ValueError,ZeroDivisionError) as message:
#         print("Enter correct number: ",message)
# else:
#         print("Everything is ok")

# # #  Finally block in multiple except
# try:
#         a = int(input("Enter no: "))
#         b = int(input("Enter no: "))
#         print(a/b)
# except (ValueError,ZeroDivisionError) as message:
#         print("Enter correct number: ",message)
# finally:
#         print("I will always executed")

# # # # NESTED TRY BLOCK
# try:
#         a = int(input("Enter no: "))
#         b = int(input("Enter no: "))

#         try:
#                 print(a/b)
#         except ZeroDivisionError as msg:
#                 print(msg)
# except ValueError as msg:
#         print(msg)

# try:
#         a=int(input("Enter first integer no"))
#         b=int(input("Enter first integer no"))
#         print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#         print(message)
# else:
#         print("there are no error in try block")
# finally:
#         print("i am finally block i always excuted wheather error is raise or not")

# USER DEFINED EXCEPTION
# bank_bal=2000
# if bank_bal>1000:
#         raise Exception("UR account balance is below a accessing limit")
# else:
#         print("Your amount has withdrawal")