data =[11,22,34,56,78,87,335,67,8]
evenList = [i for i in data if i %2 ==0 ]
print(evenList)
# for i in data:
#     if i %2 ==0:
#         evenList.append(i)

print(evenList)        

users = ["amit","raj","simran","gabbar","kattapa","shaktiman"]
filusers =[i for i in users if len(i)>5 and i.startswith("s")]

# for i in users:
#     if len(i)>5:
#         filusers.append(i)

print(filusers)        
        
        
#users =["naman","madam","jay","raj","radar","malayalam","amit","nitin"]        