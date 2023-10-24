import matplotlib.pyplot as plt
import numpy as np
#https://www.simplilearn.com/tutorials/statistics-tutorial/probability-density-function
#https://matplotlib.org/stable/users/explain/quick_start.html#quick-start
import matplotlib as mpl

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

fig = plt.figure()  # an empty figure with no Axes
fig, ax = plt.subplots()  # a figure with a single Axes
fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# a figure with one axes on the left, and two on the right:
fig, axs = plt.subplot_mosaic([['left', 'right_top'],
                               ['left', 'right_bottom']])