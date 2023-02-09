dic1= {}
oldid = 1
id1 = 1
with open("grades.txt", 'r') as f:
    f.readline()
    for i in f:
        i = i.replace(":", " ")
        i = i.replace("-", " ")
        id= int(i.split()[0])
        name = i.split()[1]
        grade = i.split()[2]
        birthyear = int(i.split()[3])
        gender = i.split()[4]
        if grade == 'N/A':
            continue
        dic1[id] = {'name': name, 'grade': grade,
                      'gender': gender, 'birthyear': birthyear}

        if (dic1[id]['birthyear'] < dic1[oldid]['birthyear']):
            oldid = id
        if (dic1[id]['grade'] < dic1[id1]['grade']):
            id1 = id

print(dic1)

avgrge = 0
val = dic1.values()
for k in val:
    avgrge += int(k['grade'])
avgrge = avgrge / len(val)
print("id-oldest= {}".format(oldid))
print("averge= {}".format(avgrge))
print("gender-highest-score= {}".format(dic1[id1]['gender']))
f.close()