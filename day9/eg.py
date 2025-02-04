# def sum(a=8,b=5):
#     return a+b

# print(sum(12,56))
# sum(1,2)
# sum(2,5)
# sum(2,6)
# sum(4,7)
# sum(1,2)


def person(fname,lname,surname = "chalamalasetti"):
   name= f"my name is {fname} {lname} {surname}"
   return name

print(person("sai","madan"))

def print_upto_five():
   for i in range(5):
        print(i)

print_upto_five()
