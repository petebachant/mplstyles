#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("./arial.mplstyle")

data = np.linspace(0, 1)

for n in range(8):
    plt.plot(data + 0.2*n, label="Line {}".format(n))

plt.xlabel("$x$-label")
plt.ylabel("$y$-label")
plt.title("Title $f = ma$")
plt.grid(True)
plt.legend(loc="best")
plt.show()
