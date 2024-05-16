"""
==============
3D quiver plot
==============

Demonstrates plotting directional arrows at points on a 3D meshgrid.
"""

# max possible velocity is max magnitude of vector (1) times grid size (7)
# make sure to model time interval so that it does not skip positions 

import matplotlib.pyplot as plt
import numpy as np

def init_point():
    init_x, init_y, init_z = 1,1,1

def create_vectors():
    
    u, v, w = (np.random.uniform(-1.0, 1.0, size=(7,7,7)),
                np.random.uniform(-1.0, 1.0, size=(7,7,7)),
                np.random.uniform(-1.0, 1.0, size=(7,7,7))
                )

    # modify the boundaries
    # u cross v
    u[0,:] = 0
    v[0,:] = 0
    w[0,:] = 1

    u[-1,:] = 0
    v[-1,:] = 0
    w[-1,:] = -1

    # v cross w
    u[:,:,-1] = 1
    v[:,:,-1] = 0
    w[:,:,-1] = 0

    u[:,:,0] = -1
    v[:,:,0] = 0
    w[:,:,0] = 0

    # u cross w
    u[:,0] = 0
    v[:,0] = 1
    w[:,0] = 0

    u[:,-1] = 0
    v[:,-1] = -1
    w[:,-1] = 0

    return u, v, w


ax = plt.figure().add_subplot(projection='3d')

# Make the grid (position)
x, y, z = np.meshgrid(np.arange(-3, 4, 1),
                     np.arange(-3, 4, 1),
                     np.arange(-3, 4, 1)
                     )
                     


u, v, w = create_vectors()



ax.quiver(x, y, z, u, v, w, length=1, normalize=True)

plt.show()
