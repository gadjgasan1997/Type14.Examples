res=[]
for x in "012345678":
    for y in "012345678":
        t = int('88' + x + '4' + y, 9) + int('7' + x + '44' + y, 11)
        if t%61==0:
            res.append(t)
if res:
    print(min(res)//61)