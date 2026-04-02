# Correlation Visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [20000, 30000, 40000, 50000, 60000]
}

df = pd.DataFrame(data)

corr = np.corrcoef(df["Experience"], df["Salary"])
print("Correlation Matrix:\n", corr)

plt.scatter(df["Experience"], df["Salary"])
plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()