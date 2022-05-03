#Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.


from time import sleep
def f():
    return ("Hi! good morning")
def jobscheduler(f,n):
    sleep(n/1000)
    print(f())
n=int(input())
jobscheduler(f,n)