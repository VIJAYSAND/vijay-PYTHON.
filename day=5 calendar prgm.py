'''#DISPLAY HOLE YEAR CALENDaR
import calendar
print("full calendar")
print(calendar.calendar(2033))


print("particular month")
print(calendar.month(2022,2))

print("set first day of the week")
calendar.setfirstweekday(calendar.FRIDAY)
print(calendar.month(2022,12))'''


#display date times:>
import datetime
a=datetime.datetime.now()
print(a)

sv=a.strftime("%y") #lower case
fv=a.strftime("%Y") #upper case

print("yesr short version",sv)
print("year full version",fv)
