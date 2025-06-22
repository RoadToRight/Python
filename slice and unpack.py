# slice means [0:2] youcan slice string and also list

# [::2] means cut one and then skip and then cut one and skip

names = ["sameer", "shah", 12, 18, 19]

first, second, third = names
# you must use 3 variables not 2 or 4 exact number
print(first)
print(second)
print(third)
# but if you need so use list slicing
first, second, third = names[0:2]
print(first)
print(second)
# in this situation if you need to take numbers in a list so
names2 = ["sameer", "shah", 12, 18, 19,"pk"]
first, second, *third ,pk= names
print(first)
print(second)
print(third)
