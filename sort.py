numbers = [8, 1, 99, 2, 6, 3]
numbers.sort()  # sort ascending order and original array
numbers.sort(reverse=True)  # sort descending order and original array
new_list = sorted(numbers, reverse=True)  # not change original array

print(new_list)
print(numbers)

list1 = ["b", "c", "a", "d"]

list2 = ["bdasf", "cgdaf", "agdaf", "gfda"] #sort bases or first letter if two starts with same so compare whole word
list1.sort(reverse=True)
print(list1)
