data = (["raj",23],["jay",24],["simran",25])

data[0][1]=24

print(data)

print(data[2][1])

data[2].pop()

print(data)

data[1].insert(1,"ok")
print(data)