states = ("Karnataka", "Tamil Nadu", "Kerala")
print(states, type(states))

# Type Conversion: Tuple => List
# Using list() method, we can convert the tuples to list
statesList = list(states)
print(statesList, type(statesList))

statesList.append("Maharashtra")
print(statesList)

statesList.remove("Kerala")
print(statesList)

# Againing converting the modified list to tuple using tuple() method
states = tuple(statesList)
print(states, type(states))