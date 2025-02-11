# def greet(name):
#     print(f"happy bday {name}")
# greet("Sai")
# greet("Madan")
# greet("Mohan")

# def createname(fname,lname):
#     fname= fname.capitalize()
#     lname = lname.capitalize()
#     return fname + " " + lname
# print(createname("sai","madan"))

# def add(x,y=2):
#     print(x+y)
# print(add(4))
# print(add(3,5))
# print(add(3,2))

# print(add(2,2))
# print(add(4,2))

# class character:
#     def __init__(self,health,damage,speed):
#         self.health = health
#         self.damage = damage
#         self.speed = speed
#     def warriorinfo(self):
#         return f"character has {self.health} health and have {self.speed} speed and he can damage {self.damage} "
# warrior = character(400,300,250)
# ninja = character(400,500,250)
# print(warrior.warriorinfo())
# print(ninja.warriorinfo())


#class methods

class student:
    count = 0
    totalgpa = 0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        student.count += 1
        student.totalgpa +=1

    def getinfo(self):
        return f" {self.name} {self.gpa} "
    @classmethod
    def getcount(cls):
        return f"total # students  :  {cls.count}"
    
    @classmethod
    def countgpa(cls):
        return f"Total GPA : {cls.totalgpa}"
s1 = student("Sai",3.2)
s2 = student("Madan",3.8)
s3 = student("Mohan",4.8)

print(student.getcount())
print(student.countgpa())
