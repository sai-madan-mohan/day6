# class bankaccount:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance
    
#     def deposit (self,amount):
#         self.balance= self.balance+ amount
#     def withdraw(self,amount):
#         self.balanace= self.balance-amount
#         return f" wirhdrawn amount is {amount},Remaining balance is {self.balance}"
#     def getbalance(self):
#         return self.balance
    
    
# account = bankaccount("sai",10000)
# print(account.getbalance())

# account.deposit(5000)
# print(account.getbalance())

# print(account.withdraw(10000))


# inheritance class

# class vehicle:
#     def __init__(self,brand,speed):
#         self.brand = brand
#         self.speed = speed
#     def showinfo(self):
#         return f" {self.brand} runs with {self.speed}km/h"
# class car(vehicle):
#     def __init__(self,brand,speed,fueltype):
#         super().__init__(brand,speed)
#         self.fueltype = fueltype
#     def carinfo(self):
#         return f" {self.brand} runs with {self.speed}km/h uses {self.fueltype}"
# c1 = car("Tesla",150,"Electric") 
# print(c1.showinfo())
# print(c1.carinfo())      

