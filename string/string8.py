data = "hi this is a string"

#(" ") is the delimiter
x = data.split("i")
print(x)


data = "hi this is a string"
data = data.replace("x","I",2)
print(data)


#email = "  jay@gmail.com  "
email = "comjay@gmail.com"
print(email)
print("len..",len(email))

email = email.strip("com") #remove spaces from both sides
print(email)
print("len..",len(email))

email = "   raj@gmail.com  "
print(email)
print("len..",len(email))
email = email.lstrip() #remove spaces from left side
print(email)
print("len..",len(email))

email = "   raj@gmail.com  "
print(email)
print("len..",len(email))
email = email.rstrip() #remove spaces from right side
print(email)
print("len..",len(email))

