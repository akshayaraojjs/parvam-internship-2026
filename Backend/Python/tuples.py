# Tuple is represented using paranthesis "()"

# Tuple Properties:
# Ordered, Immutable (Unchangeable) and Allow Duplicate Values

# Index starts from 0
bikes = ("Pulsar NS125", "Royal Enfield Classic 350", "INS Vikranth", "TVS XL100", "Hero Splender", "Honda Activa", "TVS XL100")

print(bikes)
print(type(bikes))

# Accessing the value using its index number
print(bikes[1])

# Accessing the value using negative indexing
print(bikes[-3])

# Tuple Methods:
# count, index
print("Number of Items in Bikes Tuple: ",len(bikes))

# count - give the count of the items repeatitions
TvsBikeCount = bikes.count("TVS XL100")
print("TVS XL100 bike is repeated for",TvsBikeCount, "times")

# index
print("Hero Splender bike is found at", bikes.index("Hero Splender"), "position")