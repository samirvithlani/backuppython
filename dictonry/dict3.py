data = {"name":"raj","age":20,"email":"raj@gmail.com","salary":10000}
print(data)

# rem = data.pop("salary")
# print("removed value...",rem)
print(data)


rem = data.popitem()
print("removed key:value pair...",rem)
print(data)