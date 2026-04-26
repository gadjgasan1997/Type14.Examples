# 4Cx4^15 + x62A^13
f=[]
for x in '0123456789ABC':
    t=int("4C"+x+"4",15) + int(x+'62A',13)
    if t%121==0:
        f.append(t)
if f:
    print(min(f)//121)