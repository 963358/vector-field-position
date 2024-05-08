"""
==============
3D quiver plot
==============

Demonstrates plotting directional arrows at points on a 3D meshgrid.
"""

import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')

# Make the grid (position)
x, y, z = np.meshgrid(np.arange(-7, 7, 1),
                      np.arange(-7, 7, 1),
                      np.arange(-7, 7, 1))

# Make the direction data for the arrows
u = np.random.uniform(0, 1)
v = np.random.uniform(0, 1)
w = np.random.uniform(0, 1)
ax.quiver(x, y, z, u, v, w, length=0.3, normalize=True)

plt.show()
