#type of functions
'''
def person (name,age):
    print(name)
    print(age)
person("madan","25")
person("sai","23")
'''
# to take default value
'''
def person(name,age=18):
    print(name)
    print(age)
person("madan")
   '''
# variable length
'''
def sum(a,*b):
    c = a
    for i in b:
        c= c+i
    print(c)
sum(2,3,5,6)
'''
#keyword variable length
'''
def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)
person("madan",age=25,city="mumbai")
'''

#global and local variable
'''
a = 10
def something():
    global a
    a= 5
    print("inside fun : ",a)
something()
print("outside fun : ",a)
'''
#count no of even and odd num present in list  
''' 
def count(lst):
    even =0
    odd = 0
    for i in  lst:
        if i%2 ==0:
         even = even+1
        else:
          odd= odd+1
    return even,odd
lst = list(map(int,input("Enter numbers separated by spaces: ").split()))

even, odd = count(lst)
print(even,odd)
'''
#fibanocci series
'''

def fib(n):
      a =0
      b=1
      print(a)
      print(b)
      for i in range(2,n):
            c = a+b
            a = b
            b = c
            print(c)
fib(10)
print("Enter the number of terms: ")
'''
#fatcorial of a number
'''
def fact(n):
    fact = 1
    for i in range(1,n+1):
        
        
        fact = fact*i
        print(fact)
fact(5)

'''
'''
def fact(num):
    fact = 1
    n = 1
    while fact<num:
        fact = fact*num
        n = n+1
        return fact == num
num = int(input("Enter the number: "))
if fact(num):
    print("yes")
else:
    print("no")
    '''
'''
f = lambda a : a*a
result = f(5)
print(result)
'''

#filter map and reduce
import class7
 
print("hi")
        

   
