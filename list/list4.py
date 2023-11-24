sales =[100,20,30,45,67,89,900,20,20,20]
#pop()
#pop(1)
print(sales)
#sales.remove(30)
print(sales)



#count...

x = sales.count(200)
print("repete count...",x)




flag = sales.count(300) #>0
if flag > 0:
    sales.remove(300)
else:
    print("not found")    

print(sales)    



#index ....

ind = sales.index(20)
print("index of 45 is ",ind)


ind = sales.index(20,3,9)
print("index of 20 is ",ind)

