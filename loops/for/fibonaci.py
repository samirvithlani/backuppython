#0 1 1 2 3 5

no1 = 0
no2 = 1
sum = 0
print(no1,no2,end=" ") #0,1

for i in range(10):
    sum = no1 + no2
    #sum = 0 + 1 = 1
    #sum = 1 + 1 = 2
    #sum = 1 + 2 = 3
    print(sum,end=" ")
    #no1 = 1
    #no1 = 1
    no1 = no2
    #no2 = 1
    #no2 = 2
    no2 = sum

