import time
def countdown(t):
    while t:
        mins,secs=divmod(t,60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer)
        time.sleep(0)
        t-=1
    print('FINISHED')
t=int(input("enter the same times in seconds"))
countdown(int(t))
