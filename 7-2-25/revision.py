# carage = 30
# # carinfo = f"the car is {carage} years old"
# print(carinfo)


# cars = ["Hundai","Audi","BMW"]
# # cars[1] = "tata"
# cars.insert(1,"tata")
# print(cars)

# def cars(name):
#     return f"the {name} is driving so fast"
# print(cars("Hunda"))

# fuel = 5
# while fuel>0:
#        fuel = fuel-1
#        print("its working")

# class car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def displayinfo(self):
#         return f"I am having {self.brand} and the model is {self.model}"
# cars=car("Tata",2023)   
# print(cars.displayinfo())

# class student():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def studentinfo(self):
#         return f"the student name is {self.name} and his age is {self.age}"
# s1 = student("sai",24)
# s2 = student("madan",25)
# print(s1.studentinfo())
# print(s2.studentinfo())


# class student():
#     def __init__(self,name,age=24):
#         self.name=name
#         self.age=age
#     def studentinfo(self):
#         return f"the student name is {self.name} and his age is {self.age}"
# s1 = student("sai",24)
# s2 = student("madan",)
# print(s1.studentinfo())
# print(s2.studentinfo())


# class ATM():
#     def __init__(self,balance=10000):
#         self.balance = balance
#     def withdraw(self,amount):
#         if amount>self.balance:
#             return "insufficient funds"
#         self.balance=self.balance-amount
#         return f"withdrawn {amount} and remaining balance is {self.balance}"
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         return f"Deposited {amount} and balance is {self.balance}"
# atm =ATM()
# print(atm.withdraw(500))
# print(atm.deposit(100))


# num=[2,3,4,5,6,7,8,9,10,11]
# even=[]
# odd=[]
# for i in num:
#     if i%2==0:
#        even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)


for i in range(5,0,-1):
    print("#"*i)
    