size=int(input("size="))
L=[]
for i in range(size):
    ele=int(input("element:"))
    L.append(ele)
print(L)
for j in L:
    if(j%2==0):
        print(j)
        
