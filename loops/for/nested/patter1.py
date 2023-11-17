'''
    outer loop
        1 
        2
        3
        inner loop
         1 2 3 false break
         1 2 3 false break
         1 2 3 false break
         
        ****
        ****
        ****
        ****

'''

# for i in range(1,5):
#     for j in range(1,5):
#         print("*",end=" ")
#     print()
    
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")    
    
#     print()    


# for i in range(1,6):
#     #i =1,i=2
#     # 6 5 4 3 2
#     # 6 5 4 3
#     # 6 5 4
#     # 6 5
#     # 6
#     for j in range(6,i,-1):
#         print("*",end=" ")
     
#     print()           


for i in range(6,1,-1):
    #i =6
    for j in range(1,i):
        print("*",end=" ")
    
    print()    