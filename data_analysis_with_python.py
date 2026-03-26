import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Create Dataset
data = {
    "Name": ["Ali", "John", "Mary", "Amina", "David", "Sara", "Peter"],
    "Math": [80, 70, 90, 60, 85, np.nan, 75],
    "English": [75, 65, 88, 70, 80, 78, np.nan],
    "Science": [85, 60, 95, 65, 90, 82, 70]
}

df = pd.DataFrame(data)
print(df)
#Explore Data
print(df.head())
print(df.info())
print(df.describe())
#check missing values:
print(df.isnull().sum())
#Fill missing values with mean:
df["Math"].fillna(df["Math"].mean(), inplace=True)
df["English"].fillna(df["English"].mean(), inplace=True)
#add Total Score:
df["Total"] = df["Math"] + df["English"] + df["Science"]
#Add Average Score:
df["Average"] = df["Total"] / 3

#Top student:
top_student = df.loc[df["Total"].idxmax()]
print(top_student)
#Weakest student:
weak_student = df.loc[df["Total"].idxmin()]
print(weak_student)

#Subject performance:
print(df[["Math", "English", "Science"]].mean())

#Sorting & Filtering
#Top 3 students:
top3 = df.sort_values(by="Total", ascending=False).head(3)
print(top3)
#Students scoring above 240:
high_scores = df[df["Total"] > 240]
print(high_scores)

#Bar Chart (Total Scores)
plt.figure()
plt.bar(df["Name"], df["Total"])
plt.title("Total Scores per Student")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.show()

#Histogram (Distribution)
plt.figure()
sns.histplot(df["Total"])
plt.title("Distribution of Total Scores")
plt.show()

#Heatmap (Subject Comparison)
plt.figure()
sns.heatmap(df[["Math", "English", "Science"]], annot=True)
plt.title("Score Heatmap")
plt.show()

#best students,hardest subjects
print("Best student:", df.loc[df["Total"].idxmax(), "Name"])
print("Hardest subject:", df[["Math","English","Science"]].mean().idxmin())
#Save Results
df.to_csv("cleaned_student_data.csv", index=False)