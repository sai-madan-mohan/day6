# def greet(name):
#     return f"Hello how are you {name}"
# print(greet("Sai"))
# print(greet("Madan"))

# eg1

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     return a/b
# print(add(4,5))
# print(sub(4,5))
# print(multiply(4,5))
# print(divide(4,5))

# eg2
# def maximum(a,b,c):
#     return max(a,b,c)
# print(maximum(3,4,5))

#eg3
# def even(num):
#     if num%2==0:
#         return True
#     return False
# print(even(4))
# print(even(9))

#eg4
# def countingvowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0 
#     for char in text:
#         if char in vowels:
#             count= count+1
#     return count
# print(countingvowels("helloworld"))

#eg5

def convertingseconds(seconds):
    hours = seconds//3600
    minutes = (seconds%3600)//60
    remainingseconds = seconds%60
    return f"{hours} hours ,{minutes} minutes , {remainingseconds} seconds"
print(convertingseconds(3661))