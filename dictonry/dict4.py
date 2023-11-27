data = {"name":"raj","age":20,"email":"raj@gmail.com","salary":10000}

print(len(data))

while len(data)>0:
    rem = data.popitem()
    print(len(data))
    print("removed key:value pair...",rem)

print(data)    