# max possible velocity is max magnitude of vector (1) times grid size (7)
# make sure to model time interval so that it does not skip positions 

import matplotlib.pyplot as plt
import numpy as np

def init_particle(): 
    u,v,w = np.random.uniform(-1.0,1.0, size=3)
    x,y,z = np.random.uniform(-3.0,3.0, size=3)
    print("initial u,v,w: ", u,v,w, "initial x,y,z: ", x,y,z)
    return x,y,z, u,v,w


def create_point(x,y,z):
    ax.scatter(x,y,z, c="red", s=100)

def create_velocity(u,v,w):
    return
def create_field():
    
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
field_x, field_y, field_z = np.meshgrid(np.arange(-3, 4, 1),
                     np.arange(-3, 4, 1),
                     np.arange(-3, 4, 1)
                     )
                     

field_u, field_v, field_w = create_field()


ax.quiver(field_x, field_y, field_z, field_u, field_v, field_w, length=0.5, normalize=True)

plt.show()
