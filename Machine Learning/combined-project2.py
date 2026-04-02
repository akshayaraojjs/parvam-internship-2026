# Sales Distribution & Insights

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Sales": [100, 200, 150, 350, 250, 300, 400, 450]
}

df = pd.DataFrame(data)

print("Mean:", np.mean(df["Sales"]))
print("Standard Deviation:", np.std(df["Sales"]))

plt.hist(df["Sales"], bins=10)
plt.title("Sales Distribution")
plt.show()