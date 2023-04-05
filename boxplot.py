# Boxplot
import matplotlib.pyplot as plt
import random

vector = []

for i in range(100):
    vector.append(random.randint(0, 50))

plt.title("Boxplot")
plt.boxplot(vector)
plt.show()
