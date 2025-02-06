# student = {"name": "Alice", "age": 20}
# print(student["name"])  # Alice
# student["age"] = 21 
# print(student)

#class  functions

# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print(f"Hi iam {self.name} and my age is {self.age}")
# p1 = person("sai",25)
# p1.introduce()
# p2 = person("Madan",26)
# p2.introduce()

# list1  = [1,2,3,4,5]
# list1[1] = 10
# print(list1)


#for loop

# list1 = [1,2,3,4,5]

# # for i in list1:
# #     print(i*5)
# # print("BYE")

# list2 =[]
# for i in list1:
#     list2.append(i*5)
# print(list2)

# for i in range(1,100):
#     if i%7 ==0 :
#         continue
#     print(i)

# num = int(input("Enter the number :"))
# for i in range(1,11):
#     print(num, "x" ,i , "="  ,num*i)


# str1 = input("Enter the str : ")
# v=[]
# c=[]

# for i in str1:
#     if i in 'AEIOUaeiou':
#         v.append(i)
#     else:
#         c.append(i)
# print(v,len(v))
# print(c,len(c))


# str1 = input("Enter the str  : ")
# a=[]
# d=[]
# g=[]
# for i in str1:
#     if i.isalpha():
#         a.append(i)
#     elif i.isdigit:
#         d.append(i)
#     else:
#         g.append(i)
# print(a)
# print(d)
# print(g)

# str1 = input("Enter the str  : ")
# u = []
# l = []
# for i in str1:
#     if i.isupper():
#         u.append(i)
#     else:        
#         l.append(i)
# print(u,len(u))
# print(l,len(l))

#while loop

# i = 0
# while i<10:
#     i=i+1
#     print(i)


# while True:
#     print("1 . Add")
#     print("2 . Subtract")
#     print("3 . multiply")
#     print("4 . exit")
#     ch = int(input("enter your option  : "))
#     if ch ==1:
#         n1 = int(input("Enter the num1  : "))
#         n2 = int(input("Enter the num2  : "))
#         print("Add of two number is  : ", n1+n2)
#     elif ch == 2:
#         n1 = int(input("Enter the num1  : "))
#         n2 = int(input("Enter the num2  : "))
#         print("Subtract of two number is  : ", n1-n2)
#     elif ch == 3:
#         n1 = int(input("Enter the num1  : "))
#         n2 = int(input("Enter the num2  : "))
#         print("Multipy of two number is  : ", n1*n2)
#     elif ch ==4:
#         print("thank you")
#         break
#     else:
#         print("invalid")

# def add(x,y):
#     return x+y
# result = add(4,5)
# print(result)

# result = add(10,1)
# print(result)


#class and object

# class character:
#     def __init__(self,health=50,damage=50,speed=100):
#         self.health = health
#         self.damage = damage
#         self.speed = speed
     

# warrior = character(100,500 ,350)
# ninja = character()
# print(f"warrior have {warrior.health}")
# print(f"ninja have {ninja.health}")


# class student():


#     def __init__(self,name,gpa):
#         self.name = name
#         self.gpa = gpa

#     def getinfo(self):
#         return f"My name is {self.name} and gpa is {self.gpa}"

# s1 = student("sai",8.9)
# print(s1.getinfo())

# class cars():
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def drive(self):
#         return f"{self.brand} is driving"
# volvo = cars("volvo",2020)
# print(volvo.drive())



# while True:
#     print("1. Show Balance")
#     print("2. Deposit")
#     print("3.withdraw")
#     print("4. Exit")
#     ch = int(input("Enter your choice : "))
#     if ch==1:
#         name = input("enter your name  : ")
#         print(f"Hi {name} this is your balance in your saving account")
#         print("-"*30)
#     elif ch==2:
#         name = input("enter your name  : ")
#         amount = int(input("Enter how much amount you want to deposit  : "))
#         print(f"Amount {amount} was sucessfully deposited")
#         print("-"*30)
#     elif ch ==3:
#         name = input("enter your name  : ")
#         amount = int(input("Enter how much amount you want to withdraw  : "))
#         print(f"Please collect your amount {amount}")
#         print("-"*30)
#     elif ch==4:
#         print("Thank you ") 
#         print("-"*30)
#         break
#     else:
#         print("Inavild") 
#         print("-"*30)
# print("Thanks for visiting")                  


def wish(name):
    print( f" happy birthday {name}")
wish("sai")
