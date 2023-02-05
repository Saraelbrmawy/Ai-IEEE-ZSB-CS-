dict1={
    "A":[20,30,100,49],
     "B":[00,199,201,29],
    "C":[40,90,69,18]
}

maxres = max([max(vals) - min(vals) for sub, vals in dict1.items()])
res = [sub for sub in dict1 if max(dict1[sub]) - min(dict1[sub]) == maxres][0]

print("The maximum element key : " + str(res))