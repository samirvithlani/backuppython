#and , or 

'''
    cond 1 and cond 2
    T    T    T
    F    -    F
    T    F    F
'''

'''
    cond 1 or  cond 2
    
    T  -    T
    F   T   T
    F   F   F
'''

isAlive = False
age  = 50


if isAlive or age > 60:
    print("enjoying your life")

else:
    print("You are dead")    











