# max possible velocity is max magnitude of vector (1) times grid size (7)
# make sure to model time interval so that it does not skip positions 

# https://stackoverflow.com/questions/58691789/how-to-interpolate-a-vector-field-with-python

# boundary points is hard to implement... does not work. need to try chance that the particle does not go out of bounds



import matplotlib.pyplot as plt
import numpy as np


def init_particle(n): 
    u,v,w = np.random.uniform(-1.0,1.0, size=3)
    x,y,z = np.random.uniform(0,n-1, size=3)
    return x,y,z, u,v,w

def create_field(n):
    
    u, v, w = (np.random.uniform(-2.0, 2.0, size=(n,n,n)),
                np.random.uniform(-2.0, 2.0, size=(n,n,n)),
                np.random.uniform(-2.0, 2.0, size=(n,n,n))
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
    v[0,:] = 2
    # front
    v[-1,:] = -2
    
    # direction of w
    # top
    w[:,:,-1] = -2
    # bottom
    w[:,:,0] = 2    
    
    # direction of u
    # left
    u[:,0] = 2
    # right
    u[:,-1] = -2


    return u, v, w


# create 4 subplots
# check subplot numbering (221 = 2x2, 1st subplot): https://stackoverflow.com/questions/3584805/what-does-the-argument-mean-in-fig-add-subplot111

def vectorField():
    n = 7
    points = []

    # Make the vector field (axis intervals)
    field_x, field_y, field_z = np.meshgrid(np.arange(0, n, 1),
                     np.arange(0, n, 1),
                     np.arange(0, n, 1)
                     )
                     
    field_u, field_v, field_w = create_field(n)
    
    t = 0
    interval = 0.15
    x,y,z, u,v,w = init_particle(n)

    fig = plt.figure()

    print("True data: \n")
    for subplot in range(0,4):
        # first graph is t = 0
        ax = fig.add_subplot(221+subplot, projection='3d')
        ax.title.set_text('t='+str(t))

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

        dx = field_x[round(x), round(y), round(z)]
        dy = field_y[round(x), round(y), round(z)]
        dz = field_z[round(x), round(y), round(z)]

        
        # adding vectors, method (r + v*t)
        u += dx*interval
        v += dy*interval
        w += dz*interval
        
        ax.quiver(x,y,z, u,v,w, color="r", length=2, normalize=True) 
        ax.scatter(x,y,z, color="r", s=100)
        
        print("t = ", t)
        print("velocity: ", np.sqrt(pow(u,2) + pow(v,2) + pow(w,2)))
        print("u: ", round(u,3), "v: ", round(v,3), "w: ", round(w,3))

        points.append([x,y,z])
        # adding position to vector (r_0 + v)
        x += u
        y += v
        z += w

        print("x: ", round(x,3), "y: ", round(y,3), "z: ", round(z,3))
        
        ax.quiver(field_x,field_y,field_z, field_u,field_v,field_w, length=0.5, normalize=True)
        
        t += interval
        t = round(t,3)


    plt.show()
    
    print("\n")

    return points

