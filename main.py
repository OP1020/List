#SECTION #1
color_list = ["red", "green", "blue", "yellow"]
print(color_list[0])
print(color_list[-1])

#SECTION #2
num_list = [4, 6, 4, 2, 9, 4, 1]
num_list.append(5)
print(num_list)
num_list.remove(4)
print(num_list)
num_list.count(4)
print(num_list)
num_list.index(9)
print(num_list)

#SECTION #3
fruit_list = ["apple", "banana", "cherry"]
fruit_list[1] = "orange"
fruit_list.pop()
print(fruit_list)