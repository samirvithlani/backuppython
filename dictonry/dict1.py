'''
    list stores data in index...
    tuple stores data in index...
    key:value pair
    
    //image process --> image name,image size,image type,image path
    //["ab.jpg", "10mb", "jpg", "c:/user/desktop/ab.jpg"]
    //{name:"ab.jpg", size:"10mb", type:"jpg", path:"c:/user/desktop/ab.jpg"}
    //aramy --> ranks --> general,major,lieutenant,corporal
    ["jay","raj","rahul","sachin","sourav"]
    {"general":"jay","major":"raj","lieutenant":"rahul","corporal":"sachin"}
    //team --> players --> 
    
    #character of dict
    1) key:value pair
    2) key should be unique
    3) key should be immutable
    4) value can be mutable
    5) value can be duplicate
    6) dictionaries are unordered
    7) dictionaries are mutable
    8) dictionaries are dynamic
    9) dictionaries are iterable
    10) dictionaries are heterogeneous
    
    {} <-- empty dictionary dict

'''
#users = {} # empty dictionary
users = {"name":"raj","age":20,"email":"raj@gmail.com"}
print(users)
print(type(users))

x = users.get("name")
print("value name...",x)

y = users.get("age")
print("value age...",y)


k = users.keys()
print("keys...",k)

v = users.values()
print("values...",v)


kv = users.items()
print("key:value pair...",kv)
#[(),(),()]
# for i in users.items():
#     #print(i)
#     for j in i:
#         print(j)


for k1,v1 in users.items():
    print(k1,v1)