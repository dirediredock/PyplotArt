# by Matias I. Bofarull Oddo - 2021.11.30

import os
from PIL import Image
from numpy import array
import matplotlib.pyplot as plt
import matplotlib as mpl

# Change the filepath to the directory that contains this script
# and image data.

scriptsPath = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptsPath)
print("\nCurrent working directory: " + str(os.getcwd()) + "\n")
mpl.use("Agg")

# Import a 150 by 150 pixel grayscale image.

matrix = array(Image.open("GirlWithPearlEarring_scaled.jpg"))

# Glyphs by apparent pixel luminosity, from dim to bright.

glyphs = "     .  ' `^\",::l!i><|+_-?][}|{|\\/tfjrxnvczXYUJCOZmpdkWM##$$$$"

# Setup for export against bright and dark backgrounds.

saveName = ["pyplotArt_ASCII_Bright.png", "pyplotArt_ASCII_Dark.png"]
colorBackground = ["white", "black"]
colorGlyph = ["black", "white"]

# Running the ASCII art conversion.

for save_iteration in range(len(saveName)):

    glyphs = glyphs[::-1]

    pixel = []

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            luminosity = matrix[len(matrix) - x - 1][y][0]
            pixel.append(luminosity)

    letterMatrix = []
    letterString = []

    count = 0

    for i in range(len(matrix)):
        letterRow = []
        for j in range(len(matrix)):
            l = round((pixel[count] / (max(pixel))) * (len(glyphs) - 1))
            count += 1
            letterRow.append(glyphs[l])
            letterString.append(glyphs[l])
        letterMatrix.append(letterRow)

    for i in reversed(range(len(letterMatrix))):
        print()
        for j in letterMatrix[i]:
            print(j, end="")

    X = []
    Y = []
    I = []

    count = 0

    for i in range(len(matrix)):
        x = i + 1
        for j in range(len(matrix)):
            y = j + 1
            count += 1
            X.append(x)
            Y.append(y)
            I.append(count)

    fig = plt.figure(figsize=(10, 10))
    fig.patch.set_facecolor(colorBackground[save_iteration])
    ax = fig.add_subplot(111)

    plt.gca().set_position([0, 0, 1, 1])
    plt.scatter(X, Y, marker=".", color=colorBackground[save_iteration])
    plt.axis("off")

    for i, glyph in enumerate(letterString):
        ax.annotate(
            glyph,
            (Y[i], X[i]),
            ha="center",
            va="center",
            fontsize=6,
            font="Consolas",
            color=colorGlyph[save_iteration],
        )

    plt.savefig(saveName[save_iteration], dpi=600)
