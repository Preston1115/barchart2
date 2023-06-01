import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

'''
#makes bar chart
data = [12, 15, 5, 23, 3]
plt.bar(['Class A' ,'Class B','Class C','Class D','Class E'], data)
plt.ylabel('Number of Students with an A')
plt.xlabel('Class Name')
plt.show()
'''
#makes pie chart
y = np.array([5, 4, 8, 1, 9])
mylabels = ['Class A' ,'Class B','Class C','Class D','Class E']

plt.pie(y, labels = mylabels)
plt.title("Number of Students with F's for each class")
plt.show()

'''
#makes stacked bar chart
classes = ('Class A' ,'Class B','Class C','Class D','Class E',
)
grade_count = {
    "A": np.array([12, 15, 5, 23, 3]),
    "F": np.array([5, 4, 8, 1, 9]),
}
width = 0.5

fig, ax = plt.subplots()
bottom = np.zeros(5)

for boolean, grade in grade_count.items():
    p = ax.bar(classes, grade, width, label=boolean, bottom=bottom)
    bottom += grade

ax.set_title("Number of A and F grades")
ax.legend(loc="upper right")

plt.show()
'''