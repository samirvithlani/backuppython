'''
    list: list is group of elements
    1) list is mutable
    2) list is ordered [0,n-1]
    3) list is iterable [1,2,3,4]
    4) list is heterogeneous [1,2.3,"hello"]
    5) list is dynamic
    6) list is growable
    7) list is indexable
    8) list is sliceable
    
    [] -> empty list
    list -> data type list
'''

data = [10,20,30,40,50,60,70,80,90,100]
print(data)
print(type(data))

x = data[0]
print(x)

#range...(0,end)

l = len(data)
print("len..",l)

#for i in range(0,l):
for i in range(0,len(data)):
    print(data[i])
