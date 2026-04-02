# Student Marks Comparison
import matplotlib.pyplot as plt

students = ["A", "B", "C", "D"]
marks = [80, 85, 75, 90]

plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Age Distibution Analysis
ages = [20, 23, 22, 21, 20, 25, 24, 22, 23, 20, 21, 23, 25, 24, 26]
# How the data is distributed by giving the width b/w each bar to show its frequency 
plt.hist(ages, bins=15)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()