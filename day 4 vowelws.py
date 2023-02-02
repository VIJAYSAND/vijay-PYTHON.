l=['a','e','i','o','u','A','E','I','O','U']
str=input("enter a string:")
count=0
for i in str:
    if i in l:
        count=count+1
print(count)
