import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

title = "Graphics"
x_axis = "X"
y_axis = "Y"

# title
plt.title(title)

# axes
plt.xlabel(x_axis)
plt.ylabel(y_axis)


# plt.bar(x1, y1, label="Group 1")
# plt.bar(x2, y2, label="Group 2")
# plt.legend()

plt.plot(x1, y1, color="#003300", linestyle="--")
plt.scatter(x1, y1, label="My points", color="g", marker="*", s=100)
plt.legend()

plt.show()
# plt.savefig("tmp/fig.png", dpi=300)
