import numpy as np
my_array = np.array([1, 2, 3, 4, 5])
print("Array:", my_array)
print("Array * 2:", my_array * 2)  
print("Mean:", np.mean(my_array)) 
print("Square Roots:", np.sqrt(my_array)) 
 
my_array = ([10, 20, 30, 40, 50])
print("array:", my_array)
print("maximum number:", np.max(my_array))
print("minimum number", np.min(my_array))

result = my_array * 3
print("after multiplying by * 3:", result)
print(my_array * 3)
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'Score': [85, 90, 95]
}

df = pd.DataFrame(data)

print(df)
print("Names:", df['Name'])
print("Scores above 90:")
print(df[df['Score'] > 90])

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

plt.bar(names, scores, color='skyblue')
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.show()

activities = ['Sleeping', 'Eating', 'Coding', 'Gaming']
hours = [8, 2, 8, 6]

plt.pie(hours, labels=activities, autopct='%1.1f%%')
plt.title("Daily Activities")
plt.show()


import pandas as pd
data = {
    'Year': [2021, 2022, 2023],
    'Users': [1500, 3000, 5000]
}

df = pd.DataFrame(data)
plt.plot(df['Year'], df['Users'], marker='o')
plt.title("User Growth Over Time") 
plt.xlabel("Year")
plt.ylabel("Users")
plt.grid(True)
plt.show()
