#i=1,2,3,4,5
for i in range(1,5):
    # 6,5,4,3,2,
    # 6,5,4,3
    for k in range(6,i,-1):
        print(" ",end="")
    
    for j in range(1,i+1):
        print("*",end=" ")
    
    
    print()        
    
        