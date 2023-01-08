## Tuples()
# mytuple = ("Kartik", "Rishabh", "Aditya","Jayesh","Mehul","Roshan","Arpit")
# print(mytuple)
# print(type(mytuple))
# # mytuple[2]="sunil"
# print(mytuple)

# # Set Datatype {}
# myset = {1,2,"Kartik",5.66,"Rishabh","aditya","jayesh"}
# print(myset)
# #we can add a data with
# myset.add(60)
# print(myset)
# # to add more thaaan one data we will use
# # myset.update(range(1,10,12))
# # To remove when not sure of values presence
# myset.discard(3)
# print(myset)
# #Use remove when we know that value is present
# # myset.remove(3)

#union
# myset = {10,20,30,40}
# yourset={"Kartik","Pal"}
# newset = myset.union(yourset)
# print(newset)

#intersection
# myset = {10,20,30,40}
# yourset = {10,50,60,30}
# print(myset.intersection(yourset))

#difference
myset = {10,20,30,40}
yourset = {10,50,60,30}
print(myset.difference(yourset))

#4 frozenet datatypes
myset={1,2,"Kartik",5.66,"rahul","rishabh","aditya"}
fs=frozenset(myset)
print(type(fs))
print(fs)