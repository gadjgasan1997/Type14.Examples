f=[]
for x in "0123456789ABCDEF":
    t=int('1'+x+"BAD",16)+ int("2"+"C"+x+"FE",16)
    if t%15==0:
        f.append(t)
print(min(f)//15)