data = {"MON":[90,30,70],"TUE":[40,50,60],"WED":[70,80,90]}

data.update({"THU":[60,30,45]})
print(data)

data["WED"]=[80,20,70]
print(data)

#totalData = {"MON":190,"TUE":150,"WED":240,"THU":135}
totalData = {}
add =0

for k,v in data.items():
    add =0
    for j in v:
        add = add+j
        
    totalData.update({k:add})   
        

print(totalData)        
    
    
    