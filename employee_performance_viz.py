"""
Employee Performance Visualization

Author email (for verification): 23f2001336@ds.study.iitm.ac.in
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("employees.csv")

# Calculate R&D department count
rd_count = (df["department"] == "R&D").sum()
print("Number of employees in R&D department:", rd_count)

# Create histogram using matplotlib
plt.figure(figsize=(8, 5))
df["department"].value_counts().plot(kind="bar")
plt.title("Department Distribution of Employees")
plt.xlabel("Department")
plt.ylabel("Employee Count")
plt.tight_layout()
plt.savefig("department_histogram.png", dpi=120)
plt.close()

print("Histogram saved as department_histogram.png")
