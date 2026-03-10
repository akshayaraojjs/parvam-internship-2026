# List Properties:
# Ordered, Mutable (Changeable) and Allow Duplicate Values
# It is represented using "[]"
# Values are stored in respective index numbers starting from 0

vegetables = ["Carrot", "Tomato", "Potato", "Onion", "Radish", "Carrot", "Potato"]
print(vegetables, type(vegetables))

# Ordered property refers to the sequence followed by the list items

# We can have Duplicate values in the list
print(vegetables[0], vegetables[3])

# List Methods:
# append, insert, remove, pop, clear, copy, extend, count, index, reverse, sort

# Append method is used to add the new list item at the end of the list
vegetables.append("Cucumber")
vegetables.append("Brinjal")
print(vegetables)

# Insert method is used to add new item at any specific index position
# insert(index/position, value)
vegetables.insert(1, "Beans")
vegetables.insert(3, "Beetroot")
print(vegetables)

# Pop method is used to remove the last item from the list
vegetables.pop()
# pop(index) or pop() for last item
vegetables.pop(3)
print(vegetables)

# Remove method is used to remove the specific value from the list
# remove(item)
vegetables.remove("Carrot")
# If we try to remove the unknown item, we will get "ValueError"
# vegetables.remove("Beetroot")
print(vegetables)

# Count method is used to check the number of item repeatitions in the list
# count(item)
potatoCount = vegetables.count("Potato")
print("Potato is repeated for", potatoCount, "times in the list")

# Copy method is used to copy the list items from one list to another list
basket = []
print(basket)
# new_list = old_list.copy()
basket = vegetables.copy()
print("Items added to the basket:", basket)

# Extend method is used to add or copy the items from another list to the existing list
# list1.extend(list2)
fruits = ["Apple", "Banana", "Strawberry", "Mango", "Apple"]
basket.extend(fruits)
print(basket)

# Reverse method is used to change the order of the list items
basket.reverse()
print(basket)

# Index method will return the position or index of the list item
firstApple = basket.index("Apple")
# index(item, start-position)
secondApple = basket.index("Apple", 2)
print("First Apple is found at index:", firstApple)
print("Second Apple is found at index:", secondApple)

# Sort method is used to sort the list items in Ascending or Descending Order
# By default, ascending order will be used by sort method
basket.sort()
print("Items in Ascending Order:", basket)
basket.sort(reverse=True)
print("Items in Descending Order:", basket)


# Clear method is used to remove all items from the list
vegetables.clear()
print(vegetables)

# del method can be used to remove the list itself
del(vegetables)
# If the list is tried to access again, we will get "NameError"
# print(vegetables)