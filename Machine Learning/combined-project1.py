# Employee Salary Analysis Dashboard

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Dept": ["IT", "HR", "IT", "HR", "QA", "IT", "QA", "IT"],
    "Salary": [50000, 65000, 35000, 45000, 30000, 55000, 60000, 75000]
}

df = pd.DataFrame(data)

# Calculate Average Salary
print("Average Salary:", np.mean(df["Salary"]))

dept_salary = df.groupby("Dept").mean()

dept_salary.plot(kind='bar')
plt.title("Avg Salary by Department")
plt.show()