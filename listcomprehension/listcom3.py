users =["naman","madam","jay","raj","radar","malayalam","amit","nitin"]


filusers = [i for i in users if i == i[::-1]]
print(filusers)