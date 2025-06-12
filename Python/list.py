data = "vishwajeet"
names = ["sameer", "shah", 12, 18, 19]
marks = [[90, 54, 54], [32, 54, 67], [98, 87, 68], "sameer", 1]
print(type(marks))

list1 = names + marks

print(list1)
numbers = list(range(20))
print(numbers)

textList = list("vishwajeet")
print(textList)
print(len(textList))

# if you want index of list enumerate return with tuple
for x in enumerate(names):
    print(x[0], x[1])

names.append("Youtube")  # it changes original list
# it does not remove existing element or zero index it makes it 1
names.insert(0, "hello")

names.pop()  # last item remove change original list
names.pop(1)  # takes index t0 remove

# removes with element name it removes only first item that match and found if twwo shah so first deleted
names.remove("shah")


del names[1:4]  # it is use to remove so many elements
names.clear()  # make list empty
# finding the element present in listt?
if "ajit" in names:
    print("yes")
else:
    print("no")

# give index/position of element it return of first element of two present
names.index("shah")
names.count("ajit")  # how many time it present
