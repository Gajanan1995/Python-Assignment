# Data Types in Python 
print("----------------------------")
print("--- Data Types is Python ---")
print("----------------------------")

#Numeric
print("--- Numeric Data Types ---")
No = 11                                     #int
Marks = 91.5                                #float
Value = 4+5j                                #complex

print("Value of No is : ",No)
print("Id of No is : ",id(No))
print("Type of No is : ",type(No))

print("")


print("Value of Marks is : ",Marks)
print("Id of Marks is : ",id(Marks))
print("Type of Marks is : ",type(Marks))

print("")

print("Value of Value is : ",Value)
print("Id of Value is : ",id(Value))
print("Type of Value is : ",type(Value))

#Text
print("")
print("--- Text Data type --- ")
State = "Maharashtra"                      # Str 

print("Value of State is : ",State)
print("Id of State is: ",id(State))
print("Type of State is :",type(State))

#Sequence
print("")
print("--- Secquence Data Type ---")
data1 = [10, 20, 30, 40]                    # List 
data2 = (10, 20, 30, 40)                    # Tuple
data3 = {10, 20, 30, 40}                    # Set
data4 = {"A":10, "B":20, "C":30, "D":40}    # Dict
data5 = "Maharashtra"                       # Str

print("Value of data1 is : ",data1)
print("Type of data1 is : ",type(data1))
print("Id of data1 is : ",id(data1))

print("")

print("Value of data2 is : ",data2)
print("Type of data2 is : ",type(data2))
print("Id of data2 is : ",id(data2))

print("")

print("Value of data3 is : ",data3)
print("Type of data3 is : ",type(data3))
print("Id of data3 is : ",id(data3))

print("")

print("--- Mapping Data Type ---")
print("Value of data4 is : ",data4)
print("Type of data4 is : ",type(data4))
print("Id of data4 is : ",id(data4))

print("")

print("Value of data5 is : ",data5)
print("Type of data5 is : ",type(data5))
print("Id of data5 is : ",id(data5))

print("")

# Boolean
print("--- Boolean Data Type ---")
gender = True                               # bool
print("Value of Gender is",gender)
print("Type of gender is : ",type(gender))
print("ID of gender is : ",id(gender))

# None
print("")
print("--- None Data Type ---")
demo = None                                 #None
print("Value of demo is :",demo)
print("Type of demo is :",type(demo))
print("Id of demo is : ",id(demo))