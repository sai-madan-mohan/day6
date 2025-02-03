'''
x = 10

if x < 10:
  for i in range(1,5):
   print(x*i)
elif x>10:
  j =1
  while j<5:
       print(x*j)
       j=j+1
else:
  print(x**10)
'''
#eg Exceptional handling in python
'''
try:
    n1 = int(input("enter num1 :    "))
    n2 = int(input("Enter num2 :    "))
    result =n1/n2
except ZeroDivisionError:
    print("you can not divide a num with Zero")
except ValueError:
    print("Invalid Input")
    '''
''''
f = open("source.txt","w")
f.write("HI DA")
f.close()
'''
'''
#eg CSV files
import csv
f = open("dagta.csv","w",newline ="")
obj = csv.writer(f)
obj.writerow(["sai","delhi"])
obj.writerow(["madan","Vijayawada"])
f.close()
'''
'''
# eg to read the csv files
import csv
f = open("dagta.csv","r")
obj = csv.reader(f)
data = list(obj)
print(data)
f.close
'''
#eg csv project
'''
import csv

def addData():
    print("___ Add a student Details____")
    f = open("project.csv","w")
    obj = csv.writer(f)
    list1 = []
    roll = input("Enter the roll number  :  ")
    list1.append(roll)
    n = input("enter the student name  :  ")
    list1.append(n)
    m = input("enter the marks in Maths")
    list1.append(m)
    s = input("enter the marks in Science")
    list1.append(s)
    obj.writer(list1)
    f.close
    print("__Added succefully__")
def printData():
    print("___Data___")
    f = open("project.csv","r")
    obj=csv.reader(f)
    data = list(obj)
    for i in data:
        print(i)
    print("________")
    f.close()
def checkpercentage():
    print("__Check your result___")
while True:
    print("1. Add Data")
    print("2.Show Data")
    print("3.Check your percentage")
    print("4.exit")
    ch = int(input("Enter your choice :"))
    if ch == 1:
        addData()
    elif ch ==2:
        printData()
    elif ch==3:
        checkpercentage()
    else:
        print("invalid")
'''

