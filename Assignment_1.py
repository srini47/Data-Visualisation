# -*- coding: utf-8 -*-
"""Assignment 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cBgtAgSyB68AV5UU8AIqUmpVQhcjRXio
"""

x = np.arange(0, 10)
y = x * x
plt.title("Square Graph", color="r")
plt.xlabel("Integer", color="b")
plt.ylabel("Square", color="c")
plt.plot(x, y, "gx-", linewidth=1, markersize=2)