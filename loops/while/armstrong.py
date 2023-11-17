#153
# 1 + 125 + 27 = 153
no =153
tempno = no
tempno1 = no
rem = 0
sum = 0
cnt =0

while tempno1>0:
    tempno1 = tempno1 // 10 # 163 // 10 = 16 # 16 // 10 = 1 # 1 // 10 = 0
    cnt+=1


print("count ---",cnt)

#15 >0
while no>0:
    rem =no %10 #3 #5 #1
    sum = sum + rem ** cnt#sum = 0 + 3 ** 3 = 27
    # 27 + 5 ** 3 = 27 + 125 = 152
    # 152 + 1 ** 3 = 152 + 1 = 153
    no =no // 10 #15 #1
    

if tempno == sum:
    print("armstrong")

else:
    print("not armstrong")
        