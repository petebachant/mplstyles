#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import sys


def plot(style):
    plt.style.use("./{}.mplstyle".format(style))
    data = np.linspace(0, 1)
    plt.figure()
    for n in range(8):
        plt.plot(data + 0.2*n, label="Line {}".format(n))
    plt.xlabel("$x$-label")
    plt.ylabel("$y$-label")
    plt.title("Title $f = ma$")
    plt.grid(True)
    plt.legend(loc="best")
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        style = sys.argv[1]
    else:
        style = "arial"
    
    plot(style)
