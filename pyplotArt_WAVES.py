# by Matias I. Bofarull Oddo - 2022.03.02

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use("Agg")

points = 999999

x = []
y = []

sequence = list(np.linspace(-4, 8, int(points ** (1 / 2))))

for i in range(len(sequence)):
    for j in range(len(sequence)):
        x.append(sequence[j])
        y.append(sequence[i])

X = np.add(1, np.subtract(x, np.sin(np.power(y, 2))))
Y = np.add(1, np.subtract(y, np.cos(np.power(x, 2))))

fig = plt.figure(figsize=(10, 10))
fig.patch.set_facecolor("w")
ax = fig.add_subplot(111)
plt.gca().set_position([0, 0, 1, 1])

plt.scatter(X, Y, s=0.5, alpha=0.25, c="k", edgecolor="none")

plt.axis("off")
plt.savefig("pyplotArt_WAVES_Bright.png", dpi=400)
