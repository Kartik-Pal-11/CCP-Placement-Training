# # First way to imprt any function, variable or class from one module to another modele through import
# import module1
# module1.square(5)
# module1.login("kartik", "pal")
# print(module1.pi)

# # Second way to imprt any function, variable or class from one module to another modele through import
# import module1 as mod
# mod.square(8)
# mod.login("rishabh","aditya")
# print(mod.pi)

# # Third way when we have to import a specific function from diffferent modules 
# from module1 import square,pi
# square(7)
# print(pi)

# # FOURTH WAY When we want to access all the function in the module(so we use *)
from module1 import*
print(pi)
square(6)
welcome("Jayesh","Pandey")
login("kkk","xxx")