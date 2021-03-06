#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import sys


def plot(styles):
    for style in styles:
        plt.style.use("./styles/{}.mplstyle".format(style))
    data = np.linspace(0, 1)
    plt.figure()
    for n in range(8):
        plt.plot(data + 0.2*n, label="Line {}".format(n))
    plt.xlabel("$x$-label")
    plt.ylabel("$y$-label")
    plt.title("Title $f = ma$")
    plt.legend(loc="best")
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        styles = sys.argv[1:]
    else:
        styles = ["arial"]

    plot(styles)
