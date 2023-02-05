l=input( ).split(",")
dict1={}
for i in l:
    name,age=i.split(",")
    dict1[name]=age
print(dict1)