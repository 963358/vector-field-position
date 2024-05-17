# max possible velocity is max magnitude of vector (1) times grid size (7)
# make sure to model time interval so that it does not skip positions 

# https://stackoverflow.com/questions/58691789/how-to-interpolate-a-vector-field-with-python

import matplotlib.pyplot as plt
import numpy as np

def init_particle(): 
    u,v,w = np.random.uniform(-1.0,1.0, size=3)
    x,y,z = np.random.uniform(-3.0,3.0, size=3)
    return x,y,z, u,v,w


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


# Make the vector field (axis intervals)
field_x, field_y, field_z = np.meshgrid(np.arange(-3, 4, 1),
                     np.arange(-3, 4, 1),
                     np.arange(-3, 4, 1)
                     )
                     
field_u, field_v, field_w = create_field()


# create 4 subplots
# check subplot numbering (221 = 2x2, 1st subplot): https://stackoverflow.com/questions/3584805/what-does-the-argument-mean-in-fig-add-subplot111

t = 0
interval = 1
x,y,z u,v,w = init_particle()

for subplot in range(0,4):
    # first graph is t = 0
    ax = plt.figure().add_subplot(221+subplot, projection='3d')
    
    dx,dy,dz = init_velocity[x,y,z]

    ax.quiver(x,y,z, dx,dy,dz, c="green", length=0.5, normalize=True) 
    ax.scatter(x,y,z, c="red", s=100)
    
    # euler's method
    x += dx
    y += dy
    z += dz
    
    ax.quiver(field_x,field_y,field_z, field_u,field_v,field_w, length=0.5, normalize=True)

    t += interval


plt.show()
