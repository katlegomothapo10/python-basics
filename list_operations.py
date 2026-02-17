numbers = [10, 20, 30, 40, 50]

print("original list: " + str(numbers))

numbers.append(60)
print("after append: " + str(numbers))

numbers.remove(20)
print("after 20 remove: " + str(numbers))

print("first element: " + str(numbers[0]))
print("numbers in the list: " + str(len(numbers)))
