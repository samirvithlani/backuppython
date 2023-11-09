havingTicket = True
securityCheck = True
age = 17



if securityCheck ==True:
    print("security check passed")
    
    if havingTicket == True:
        print("you are allowed to enter")
        
        if age>=18:
            print("you are allowed to watch the movie")
        else:
            print("you are not allowed to watch the movie")        
            
    
    else:
        print("you are not allowed to enter in the theatre")    
    

else:
    print("security check failed")    



