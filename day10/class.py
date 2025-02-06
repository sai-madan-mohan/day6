# def multiply(a,b,c):
#      return a*b*c

# print("Product: " ,multiply(2,3,4))


# def addall(*numbers):
#     return sum(numbers)
# print("The sum of all numbers : ",addall(1,2,3))



#class and object

# class car:
#     brand = "Hundai"
#     model = 2020

#     def start(self):
#         print("the car is starting...")
        
# my_car = car()
# print(my_car.brand)
# print(my_car.model)
# my_car.start()

# def count_v(string):
#     vowels = "AEIOUaeiou"
#     count = 0
#     for char in string:
#         if char in vowels:
#             count = count+1
#     return count
# text ="hello"
# print(count_v(text))


# class car:
#     def __init__(self,brand,horsepower):
#         self.brand = brand
#         self.horsepower = horsepower
#     def drive(self):
#         print(f"{self.brand} is driving....")
#     def getinfo(self):
#         print(f"{self.brand} with {self.horsepower} horsepower")
# volvo: car = car('volvo',120)
# volvo.drive()
# volvo.getinfo()
# BMW: car= car("BMW",240)
# BMW.drive()
# BMW.getinfo()

# str1 ="python"
# print(str1[4:1:-1])

# str1 = 'PytHon'
# str1.swapcase()
# print(str1)

# str1 = "PytHon"
# str2=str1.islower()
# print(str2)

# str1 = " i want to play cricket"
# str2=str1.count("i")
# print(str2

# marks = int(input("Enter your marks"))
# if marks<35:
#     print("fail")
# else: 
#     print("pass")

# marks = int(input("enter your marks : "))
# if marks<35:
#     print("Fail")
# elif marks>=35 and marks<60:
#     print("grade c")
# elif marks>=60 and marks <90:
#     print("grade B")
# else:
#     print("grade A")

# num1 = int(input("enter value for num1  :"))
# num2 = int(input("enter value for num2  :"))

# if num1>num2:
#     print("num1 is big")
# elif num2>num1:
#     print("num2 is big")
# else:
#     print("both are equal")


# phn = input("enter the number : ")
# if phn.isdigit() and len(phn)==10:
#     print("valid")
# else:
#     print("invalid")

# num = int(input("enter the num  : "))
# if num%2==0:
#     print("num is even")
# else :
#     print("num is odd")

# ch = input("enter the char  :  ")
# if ch in "aeiouAEIOU":
#     print("Vowels")
# else:
#     print("cons")
