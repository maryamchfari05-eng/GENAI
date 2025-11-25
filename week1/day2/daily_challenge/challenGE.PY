#Challenge 1: Multiples of a Number
NUMBER = int(input("Enter a number?"))
length = int(input("enter the lengths"))
multipls =[]
for i in range(1, length +1):
    multipls.append(NUMBER *i )
print(multipls)
#Challenge 2: Remove Consecutive Duplicate Letters
TEXT = input("please enter a string")
result = ""
for char in TEXT :
    if result=="" or char  != result[-1]:
        result+= char
print("modifier string", result)
   