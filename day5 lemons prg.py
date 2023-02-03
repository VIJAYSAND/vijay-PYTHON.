####lemon program
'''def lemons():
    x=int(input("enter:"))
    if(x==20):
        print("yes")
    elif(x>20):
        print("excess",20-x)
    else:
        print("need some",x-20)
lemons()'''

#multiplication table
'''n=6
for i in range(1,21):
    print(i,'X',n,"=",i*n)'''

###factorial with function
n=int(input("enter value"))
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            return(i)

res=factors(n)
print(res)
###without fuctions i.e normal
n=int(input("enter?"))
for i in range (1,n+1):
    if n%i==0:
        print(i)

