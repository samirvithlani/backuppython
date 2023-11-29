userData = {"user1":[10,20,30],"user2":[40,50,60],"user3":[70,80,90]}

print(userData)
print(userData.get("user1"))


for k,v in userData.items():
    print(k)
    #print("value ",v,end=" ")
    
    for j in v:
        print(j,end=" ")
    print()    


# for i in userData.get("user1"):
#     print(i)

# for i in userData.get("user2"):
#     print(i)

# for i in userData.get("user3"):
#     print(i)    
        