#insert append

languages = ['Python', 'Java', 'C++', 'French', 'C']
languages.insert(2, 'JavaScript')
print('Updated List:', languages)
languages.append('C#')
print('Updated List:', languages)


newlist = ["PHP","Ruby","Perl"]
print("new list is ",newlist[0])

languages.extend(["php","java","python"])
print('Updated List:', languages)

languages.extend("GO")
print('Updated List:', languages)

languages.extend(100)
print('Updated List:', languages)


