# Tuples cannot be change list can be change
student1 = ("vishawajeet",7)   #if you use more than one value so if you dont give parenthesis so it considered as tuple , in prev examplein fnc *args also return tuple
student2 = "vishawajeet",7


#if you need to do give one value in tuple so do this
student3 = "vishawajeet",
t1 = (1,2,3)
t2 = (5,6)
t3 = t1+t2
t4 = t2*3 # it repeats 5,6,5,6,5,6
print(t3)

list1 = [1,2,3,4]
tuple(list1) #CONVERT LIST INTO TUPLE