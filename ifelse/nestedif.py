#true --> depedent -->condition
#false --> depedent -->condition


age = int(input("Enter your age: "))

if age >= 18:
    print("you are eligible to vote")
    
    if age>=60:
        print("you are senior citizen")
    else:
        print("you are not senior citizen")        
        
else:
    print("you are not eligible to vote")
    
    if age>=10:
        print("you are eligible to vote in kids election")
    else:
        print("stay home and play")    
                
    