# 8x78y^13 + 79xy7^18
f=[]
for x in "0123456789ABC":
    for y in "0123456789ABC":
        m=int("8"+x+"78"+y,13) + int("79"+x+y+'7',18)
        if m%9==0:
            f.append(m)
if f:
    print(min(f)//9)
