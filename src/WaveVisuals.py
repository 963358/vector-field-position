import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

def Set_hydrophones():
    plt.plot(10, 0, 0, 'ro')
    plt.plot(0, 0, 0, 'ro')
    plt.plot(0, 10, 0, 'ro')
    plt.plot(0, 0, 10, 'ro')

fig = plt.figure()
ax = fig.add_subplot(projection ='3d')



u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
r = 0.1
x = r*np.cos(u)*np.sin(v) + 20
y = r*np.sin(u)*np.sin(v) + 20
z = r*np.cos(v) + 20

d = np.sqrt(np.power(20, 2)*3) #distance of hydrophones to the 


def init():
    ax.plot_surface(x, y, z, color="g")
    return fig,

def animate(i):
    # remove previous collections
    ax.clear()
    
    Set_hydrophones()
    # add the new sphere
    x = (r+0.3*i)*np.cos(u)*np.sin(v) + 20
    y = (r+0.3*i)*np.sin(u)*np.sin(v) + 20
    z = (r+0.3*i)*np.cos(v) + 20

    Set_hydrophones()
    plt.plot(20, 20, 20, 'ro')

    ax.set_xlim(0, 50)
    ax.set_ylim(0, 50)
    ax.set_zlim(0, 50)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    if((r+0.3*i) > d):
        ani.event_source.stop()
    

    ax.plot_wireframe(x, y, z, color="g")
    return fig,

ani = animation.FuncAnimation(fig, animate, init_func = init, frames = 90, interval = 100)

plt.show()
