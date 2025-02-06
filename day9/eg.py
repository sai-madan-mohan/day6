# def sum(a=8,b=5):
#     return a+b

# print(sum(12,56))
# sum(1,2)
# sum(2,5)
# sum(2,6)
# sum(4,7)
# sum(1,2)


# def person(fname,lname,surname = "chalamalasetti"):
#    name= f"my name is {fname} {lname} {surname}"
#    return name

# print(person("sai","madan"))

# def print_upto_five():
#    for i in range(5):
#         print(i)

# print_upto_five()

dict1 = {"brand":"hundai",
         "model":"i20",
         "year": "2020"
         }
# print(dict1["model"])
# print(dict1.get("model2"))
# dict1["year"]= "2024"
# print(dict1)

# dict1["place"] = "HYD"
# print(dict1)
# del(dict1["model"])
# print(dict1)

for keys in dict1.keys():
    print(keys)
for values in dict1.values():
    print(values)
for keys,values in dict1.items():
    print(f"{keys}:{values}")
