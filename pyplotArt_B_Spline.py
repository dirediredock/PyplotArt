import numpy as np
import scipy.interpolate as si
import matplotlib.pyplot as plt
from random import randint

points = []

coord_min = 0
coord_max = 4

for k in range(8):
    row = []
    points_x = randint(coord_min, coord_max)
    points_y = randint(coord_min, coord_max)
    row.append(points_x)
    row.append(points_y)
    points.append(row)

control_point_x = []
control_point_y = []
for pair in points:
    control_point_x.append(pair[0])
    control_point_y.append(pair[1])

degree = 3

points = points + points[0 : degree + 1]
points = np.array(points)
x = points[:, 0]
y = points[:, 1]

interp_t = np.linspace(1, len(control_point_x) + 1, 30000)

t = range(len(x))

x_list = list(si.splrep(t, x, k=degree, per=1))
x_list[1] = [0.0] + x.tolist() + [0.0, 0.0, 0.0, 0.0]
x_i = si.splev(interp_t, x_list)

y_list = list(si.splrep(t, y, k=degree, per=1))
y_list[1] = [0.0] + y.tolist() + [0.0, 0.0, 0.0, 0.0]
y_i = si.splev(interp_t, y_list)

fig = plt.gcf()
fig.set_size_inches(8, 8)
fig.set_facecolor("k")
ax = fig.add_subplot(111)

plt.scatter(
    x_i,
    y_i,
    s=500,
    c=range(len(x_i)),
    cmap="inferno",
)

ax.set_aspect("equal")
plt.axis("off")
plt.show()
