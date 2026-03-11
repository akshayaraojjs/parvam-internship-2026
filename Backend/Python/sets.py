# Sets are represented using flower bracket "{}"

# Set Properties:
# Unordered, Immutable (Unchangeable), Do not allow Duplicated Values

multiplesOf2 = {2, 4, 6, 8, 10, 12, 2, 8}
print(multiplesOf2, type(multiplesOf2))

# In set, True and 1 is considered as same value, False and 0 is considered as same value
randomSet = {1, True, False, 0}
print(randomSet)

# Set Methods:
# union, intersection, difference, copy, difference_update, intersection_update, isdisjoint, issubset, issuperset, pop, remove, symmetric_difference, symmetric_difference_update, update, clear, add

set1 = {3, 5, 11, 14, 19, 21, 2, 6}
set2 = {7, 5, 13, 23, 29, 16, 8, 11}
print("Set 1 contains:", set1)
print("Set 2 contains:", set2)

# Union (|): Set 1 + Set 2 (Combine)
print("Union of Set 1 and Set 2:", set1.union(set2))

# Update (|=): Unions the set and update the set
set1.union(set2)
print("Set 1 contains:", set1)

set1.update(set2)
print("Set 1 modifies to:", set1)

# Intersection (&): Set 1 & Set 2 (Common Items)
print("Intersection of Set 1 & Set 2:",set1.intersection(set2))
# Original Set is unchanged or not updated
print(set1)

# Difference (-): Set 1 - Set 2 (Removes the Common Items)
print("Difference of Set 1 & Set 2:", set1.difference(set2))  
print("Difference of Set 2 & Set 1:", set2.difference(set1))  

# Difference Update (-=): Keeps only uncommon elements by removing common elements
# set1.difference_update(set2)
# print("After Difference(Set 1 - Set 2), Set 1 contains:", set1)
# set2.difference_update(set1)
# print("After Difference(Set 2 - Set 1), Set 2 contains:", set2)

# Symmetric Difference (^):
print("Symmetric Difference of Set 1 & Set 2:", set1.symmetric_difference(set2))
print("Symmetric Difference (Set 1 ^ Set 2):", set1 ^ set2)

# Symmetric Difference Update (^=):
set3 = set1 ^ set2
print(set3)

# Is Disjoint: Checks whether any elements are common in both the sets, if common elements found, we will get "False", if no common elements found, we will get "True"

# If Intersection elements found, result is False, if intersection elements does not found, result is True
print("Does both set does not contains common elements:", set1.isdisjoint(set2))
# set3 = {2, 4, 6, 8}
# set4 = {1, 3, 5, 7}
# print(set3.isdisjoint(set4))

# Is Subset & Is Superset:
set3 = {1, 2, 3, 4, 5, 6, 7, 8}
set4 = {1, 3, 5, 7}
# set3 contains all items of set4 => Superset (Parent)
# set4 is a child of set3 => Subset (Child)
print("Set 3 is a parent of Set 4:",set3.issuperset(set4))
print("Set 4 is a child of Set 3:", set4.issubset(set3))

# pop: (Removes random elements from the set)
print("Original Set 1 contains:", set1)
set1.pop()
set1.pop()
print("After Pop, Set 1 contains:", set1)

# remove: (Removes the specific element from the set)
set1.remove(14)
print(set1)

# discard:
# KeyError will be thrown, if we try to use remove method for removing the unknown element from the set
# set1.remove(14)

# But discard method ignores the unknown element and doesn't throw any error
set1.discard(14)
print(set1)

# add: Adding new items to the set
set1.add(25)
set1.add(27)
print("After Adding new items, Set 1 contains:",set1)

# copy: Copies the item from one set to another
new_set = set1.copy()
print("Copied the items from Set 1, New Set contains:",new_set)

# Intersection Update (&=): Removes the items which are not common in both sets
set1.intersection_update(set2)
# Original Set is updated or modified after intersection_update() method
print("Intersection Update:",set1)