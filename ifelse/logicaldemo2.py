
#min 14 --> 2.0, team exsists, 

teamName = "India"
teamPoints = 14
teamNrr = 2.3
isExists = True #udf variable......
fairPlay = True
isJayShah = False


if (teamPoints>=14 and teamNrr>=2.0 and isExists) or isJayShah:
    print("team is eligible for playoffs")
    
    if fairPlay:
        print("team is eligible for fair play award")
    else:
        print("team is not eligible for fair play award")    

else:
    print("team is not eligible for playoffs")    
    