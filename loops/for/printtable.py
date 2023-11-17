no = int(input("Enter a number: "))

# 5 * 1 = 5
# for i in range(1,11):
#     print(no," * ",i," = ",no*i)


#5 *4 * 3 * 2 * 1 = 120    

fact = 1
for i in range(1,no+1):
    fact = fact * i

print("Factorial of ",no," is ",fact)    
    
