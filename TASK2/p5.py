from p4 import dic1

dict1 = dic1

with open("filtered.txt", 'w') as f:
    for i in dict1:
        name = dict1[i]['name']
        birthyear = dict1[i]['birthyear']
        f.write(f'{i} {name} - {birthyear} \n')