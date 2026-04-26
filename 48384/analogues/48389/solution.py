# x341y^11 + 56x1y^19
f=[]
for x in "0123456":
    for y in "0123456":
        t=int(y+x+"320",7)+int('1'+x+'3'+y+'3',9)
        if t%181==0:
           f.append(t)
print(min(f)//181)
