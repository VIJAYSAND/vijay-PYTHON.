##try,excepy,finally programs:

'''a=100
b=10
try:
    print(a/b)
except:
    print("please note number cant be divided by 0")
finally:
    print("resource closed")


a=10
try:
    b=int(input("enter the a number:"))
    print("resource opened")
    print(b/a)
except  ZeroDivisionError as e:
    print("please note that the number cant be divided by 0",e)
except ValueError as e:
    print("invalid input",e)
except exception as e:
    print("other error")
finally:
  print("resource closed")

x=10
if x%2!/=0:
    r/*aise Exception("x shud even number")
else:
   print("x is even numbr..correct")

class computer:
    def config(self):
        print("YES")

lenova=computer()
lenova.config()

dell=computer()
dell.config()


class Employee:
    def __init__(self,name,id):
        self.id = id
        self.name = name

def display(self):
           # print("ID: %d \name: %s" % (self.id,#self.name))
           print(self.id,self.name)
emp1= Employee("vijay",101)
emp2= Employee("abhi",102)

emp1.display()
emp2.display() '''












































































































































































class computer():
    a=10
    b=20
    print("class variable inside class",a)

    def config(self):
        c=100
        print("YES")
        print("Instance access",self.b)
 
lenovo=computer()
print(lenovo.a)
print(lenovo.a+lenovo.b)
dell=computer()
print("dell",dell.a)
lenovo.config()

















