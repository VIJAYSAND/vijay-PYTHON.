l=list(map(int,input("enter:").split()))
print(l)
x=1
y=0
for i in l:
    x=x*i
    y=y+i
if x<=750:
    print("proad",x)
else:
    print("sum",y)
