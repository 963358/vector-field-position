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

def init_point(x,y,z):
    ax.scatter(x,y,z, c="red", s=100)

def create_vectors():
    
    u, v, w = (np.random.uniform(-1.0, 1.0, size=(7,7,7)),
                np.random.uniform(-1.0, 1.0, size=(7,7,7)),
                np.random.uniform(-1.0, 1.0, size=(7,7,7))
                )

    # modify the boundaries
    # u cross w, direction of v axis 
    # back
    u[0,:] = 0
    v[0,:] = 1
    w[0,:] = 0

    # front
    u[-1,:] = 0
    v[-1,:] = -1
    w[-1,:] = 0

    # u cross v, direction of w 
    # top 
    u[:,:,-1] = 0
    v[:,:,-1] = 0
    w[:,:,-1] = -1

    # corners

    # bottom
    u[:,:,0] = 0
    v[:,:,0] = 0
    w[:,:,0] = 1


    # v cross w, direction of u
    # left 
    u[:,0] = 1
    v[:,0] = 0
    w[:,0] = 0

    # right
    u[:,-1] = -1
    v[:,-1] = 0
    w[:,-1] = 0

    u[0,0,0], v[0,0,0], w[0,0,0], v[3,0,0], w[3,0,0], u[-3,-3,0], w[-3,-3,0], u[0,0,3], v[0,0,3], u[-3,3,3], v[3,0,3], w[3,0,3] = 1

    u[3,3,3], v[3,3,3], w[3,3,3], u[3,0,0], v[-3,-3,0], w[0,0,3], v[-3,3,3], w[-3,3,3], u[3,0,3] = -1




    return u, v, w


ax = plt.figure().add_subplot(projection='3d')

# Make the grid (position)
x, y, z = np.meshgrid(np.arange(-3, 4, 1),
                     np.arange(-3, 4, 1),
                     np.arange(-3, 4, 1)
                     )
                     


u, v, w = create_vectors()


# x, y, z
init_point(1,2,3)


ax.quiver(x, y, z, u, v, w, length=0.5, normalize=True)

plt.show()
