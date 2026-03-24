import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create sample dataset
data = {
    "Name": ["Ali", "John", "Mary", "Amina", "David"],
    "Math": [78, 85, 90, 88, 76],
    "Science": [82, 79, 95, 91, 80],
    "English": [75, 80, 85, 87, 70]
}

# Convert to DataFrame (Pandas)
df = pd.DataFrame(data)

print("Dataset:")
print(df)

# -----------------------------------
# 📊 Matplotlib Example (Basic Plot)
# -----------------------------------
plt.figure()
plt.plot(df["Name"], df["Math"], marker='o')
plt.title("Math Scores (Matplotlib)")
plt.xlabel("Students")
plt.ylabel("Score")
plt.show()

# -----------------------------------
# 🎨 Seaborn Example (Better Visual)
# -----------------------------------
plt.figure()
sns.barplot(x="Name", y="Science", data=df)
plt.title("Science Scores (Seaborn)")
plt.show()

# -----------------------------------
# 🔥 Combined Visualization
# -----------------------------------
plt.figure()
sns.heatmap(df.set_index("Name"), annot=True, cmap="coolwarm")
plt.title("All Subjects Heatmap")
plt.show()
plt.savefig("my_graph.png")

Name,Math,Science,English,History
Ali,78,82,75,80
John,85,79,80,78
Mary,90,95,85,92
Amina,88,91,87,89
David,76,80,70,75

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file (Pandas)
df = pd.read_csv("students.csv")

print("First 5 rows:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

# -----------------------------------
# 📊 Average score per subject
# -----------------------------------
avg_scores = df.mean(numeric_only=True)

plt.figure()
avg_scores.plot(kind='bar')
plt.title("Average Score per Subject (Matplotlib)")
plt.ylabel("Score")
plt.show()

# -----------------------------------
# 🎨 Seaborn Pairplot (relationships)
# -----------------------------------
sns.pairplot(df.drop("Name", axis=1))
plt.show()

# -----------------------------------
# 🔥 Heatmap (correlation)
# -----------------------------------
plt.figure()
sns.heatmap(df.drop("Name", axis=1).corr(), annot=True, cmap="coolwarm")
plt.title("Subject Correlation Heatmap")
plt.show()