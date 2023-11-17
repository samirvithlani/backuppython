data = "hello this is a string"
cnt =0


for i in data:
    if i == " ":
        cnt = cnt + 1

print("total word...",cnt+1)        
