users =[] #empty list

#10 -->

# for i in range(1,6):
#     x = input("Enter the user name:") 
#     users.append(x)

choice = -1
while True:
    
    x = input("Enter the user name:")
    users.append(x)
    choice = int(input("Do you want to continue press 1 else 0:"))
    if choice == 0:
        break
    
    


print("users...",users)    