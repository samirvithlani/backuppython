#123 321

no =123
tempno = no
rem = 0
rev = 0
while no>0:
    rem = no % 10 # 123 % 10 = 3 #12 % 10 = 2  # 1 % 10 = 1
    rev = rev * 10 + rem #  0 = 0 * 10 + 3 = rev = 3 # 3 * 10 + 2 = 32 # 32 * 10 + 1 = 321
    no = no // 10 # 123 // 10 = 12 # 12 // 10 = 1 # 1 // 10 = 0

print(rev)    

if rev == tempno:
    print("palindrome")

else:
    print("not palindrome")    
    
    
# 1 5 3    
# 1 + 125 + 27 = 153,370,371 .... 1634
