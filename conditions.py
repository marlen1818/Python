#x = 5

# > 2:
  #  print(x,  "is greater than", 6)

    #if x > number:
   #     print(x, "is greater than", number)
  #  else:
 #       print(x, "is less than")

name = input("Please enter your name: ")
age = input("Enter your age: ")

age_limit = 21

if name == "Abdul" and float(age) >= age_limit:
    print("You're welcome to drink", name)

elif name == "Simon":
    print("You are banned", name)
    
else:
    print("You are too young")