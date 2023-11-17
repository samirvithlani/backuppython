#mutablity and immutablity
#mutable: can be changed / modified
#immutable: can not be changed / modified

#string is immutable

y= 'y'
print(y)
print(type(y))

name = "John Doe"
print(name)
print(type(name))


# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])

l = len(name)
print("len...",l)

#for i in range(l):
for i in range(len(name)):
    print(name[i])
    

name[0] = "x" #change....
print(name)    