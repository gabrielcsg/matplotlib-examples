import matplotlib.pyplot as plt

data = open("data/populacao_brasileira.csv").readlines()

years = []
population = []

for i in range(len(data)):
    if i != 0:
        line = data[i].split(";")
        years.append(int(line[0]))
        population.append(int(line[1]))

plt.title("Brazilian population growth 1980 - 2016")

plt.xlabel("years")
plt.ylabel("population x100mi")


plt.bar(years, population, color="#A4A4A4")
plt.plot(years, population, color="k", linestyle="--")

# show graphic
# plt.show()

plt.savefig("tmp/brazil_growth_population.png", dpi=300)
