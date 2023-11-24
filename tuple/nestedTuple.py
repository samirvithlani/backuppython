users = (("jay",23),("raj",24),("simran",25))
print(users[0])
print(users[0][1])

# for i in range(0,len(users)):
#     for j in range(0,len(users[i])):
#         print(users[i][j],end=" ")


for i in users:
    for j in i:
        print(j,end=" ")