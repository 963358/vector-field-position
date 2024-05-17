# max possible velocity is max magnitude of vector (1) times grid size (7)
# make sure to model time interval so that it does not skip positions 

import matplotlib.pyplot as plt
import numpy as np


def init_point(x,y,z):
    ax.scatter(x,y,z, c="red", s=100)

def init_velocity(u,v,w):
    

def create_vectors():
    
    u, v, w = (np.random.uniform(-1.0, 1.0, size=(7,7,7)),
                np.random.uniform(-1.0, 1.0, size=(7,7,7)),
                np.random.uniform(-1.0, 1.0, size=(7,7,7))
                )

    # modify the boundaries
    # u cross w, direction of v axis 
    # back
    u[0,:] = 0
    w[0,:] = 0
    # front
    u[-1,:] = 0
    w[-1,:] = 0

    # u cross v, direction of w 
    # top 
    u[:,:,-1] = 0
    v[:,:,-1] = 0
    # bottom
    u[:,:,0] = 0
    v[:,:,0] = 0

    # v cross w, direction of u
    # left 
    v[:,0] = 0
    w[:,0] = 0
    # right
    v[:,-1] = 0
    w[:,-1] = 0

    # direction of v
    # back
    v[0,:] = 1
    # front
    v[-1,:] = -1
    
    # direction of w
    # top
    w[:,:,-1] = -1
    # bottom
    w[:,:,0] = 1    
    
    # direction of u
    # left 
    u[:,0] = 1 
    # right
    u[:,-1] = -1


    return u, v, w

ax = plt.figure().add_subplot(projection='3d')

# Make the grid (position)
x, y, z = np.meshgrid(np.arange(-3, 4, 1),
                     np.arange(-3, 4, 1),
                     np.arange(-3, 4, 1)
                     )
                     

u, v, w = create_vectors()


# x, y, z
init_point(np.random.uniform(-3,3), np.random.uniform(-3,3), np.random.uniform(-3,3))


ax.quiver(x, y, z, u, v, w, length=0.5, normalize=True)

plt.show()
