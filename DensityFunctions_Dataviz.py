# by Matias I. Bofarull Oddo - 2021.12.28

import numpy as np
import matplotlib.pyplot as plt
from numpy import random as R

plt.rcParams.update({"font.sans-serif": "Lato"})
fontSize = 12


def DensityDotplot(dataset, name):
    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot(111)
    density = ax.violinplot(
        dataset,
        points=999,
        widths=2,
        vert=True,
        showmeans=False,
        showmedians=False,
        showextrema=False,
        # quantiles=[0.0, 0.95],
        # bw_method="scott",
        # bw_method="silverman",
        bw_method=0.0333,
    )
    for dot in density["bodies"]:
        mean = np.mean(dot.get_paths()[0].vertices[:, 0])
        dot.get_paths()[0].vertices[:, 0] = np.clip(
            dot.get_paths()[0].vertices[:, 0], mean, np.inf
        )
    index_density = np.linspace(1, 2, len(dataset))
    plt.scatter(
        list(index_density),
        sorted(dataset, reverse=True),
        s=0.5,
        c="k",
    )
    ax.set_xlim([0.95, 2.05])
    plt.xticks([])
    plt.xlabel("Density & Dotplot")
    plt.title(name + " distribution")
    plt.show()


def QuickScatterplot(dataset, name):
    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot(111)
    ax.scatter(list(range(len(dataset))), dataset, s=0.5)
    plt.xlabel("Scatterplot")
    plt.title(name + " distribution")
    plt.show()


def QuickHistogram(dataset, name):
    plt.figure(figsize=(9, 9))
    plt.hist(dataset, bins=999, orientation="horizontal")
    plt.xlabel("Histogram")
    plt.title(name + " distribution")
    plt.show()


#############################################################################

title = "Triangular"

left = -5
peak = 0
right = +5
nums = 99999
nums_triangular = R.default_rng().triangular(left, peak, right, size=nums)

DensityDotplot(nums_triangular, title)
QuickScatterplot(nums_triangular, title)
QuickHistogram(nums_triangular, title)

#############################################################################

title = "Normal or Gaussian"

mu = 0
sigma = 1
nums = 99999
nums_normal = R.default_rng().normal(mu, sigma, nums)

DensityDotplot(nums_normal, title)
QuickScatterplot(nums_normal, title)
QuickHistogram(nums_normal, title)

#############################################################################

title = "Stepwise"


def StepwiseFunction(size, steps):
    output = []
    for i in range(size):
        for mod in range(steps):
            if i % steps == mod:
                output.append(mod + 1)
    return output


nums = 99999
nums_stepwise = StepwiseFunction(nums, 10)

DensityDotplot(nums_stepwise, title)
QuickScatterplot(nums_stepwise, title)
QuickHistogram(nums_stepwise, title)

#############################################################################
