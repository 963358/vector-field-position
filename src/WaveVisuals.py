import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import cm
from mpl_toolkits import mplot3d
import numpy as np
import math as m

def Set_hydrophones():
    plt.plot(1, 0, 0, 'ro')
    plt.plot(0, 0, 0, 'ro')
    plt.plot(0, 1, 0, 'ro')
    plt.plot(0, 0, 1, 'ro')

fig = plt.figure()
plt.xlabel('x')
plt.ylabel('y')

ax = plt.axes(projection ='3d')
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.set_zlim(0, 20)

Set_hydrophones()

plt.plot(20, 20, 20, 'ro')

u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
r = 0.1
x = r*np.cos(u)*np.sin(v) + 20
y = r*np.sin(u)*np.sin(v) + 20
z = r*np.cos(v) + 20
ax.plot_wireframe(x, y, z, color="g")

d = m.sqrt(m.pow(20, 2)*3) #distance of hydrophones to the 


def init():
    ax.plot_surface(x, y, z, color="g")
    return fig,

def animate(i):
    # remove previous collections
    ax.clear()

    # add the new sphere
    x = (r+0.3*i)*np.cos(u)*np.sin(v) + 20
    y = (r+0.3*i)*np.sin(u)*np.sin(v) + 20
    z = (r+0.3*i)*np.cos(v) + 20

    Set_hydrophones()
    plt.plot(20, 20, 20, 'ro')

    ax.set_xlim(0, 50)
    ax.set_ylim(0, 50)
    ax.set_zlim(0, 50)

    if((r+0.3*i) > d):
        ani.event_source.stop()
    

    ax.plot_wireframe(x, y, z, color="g")
    return fig,

ani = animation.FuncAnimation(fig, animate, init_func = init, frames = 90, interval = 100)
plt.show()

# def run_animation():
#     anim_running = True

#     def onClick(event):
#         nonlocal anim_running
#         if anim_running:
#             anim.event_source.stop()
#             anim_running = False
#         else:
#             anim.event_source.start()
#             anim_running = True

#     def animFunc( ...args... ):
#         # Animation update function here

#     fig.canvas.mpl_connect('button_press_event', onClick)

#     anim = animation.FuncAnimation(fig, animFunc[,...other args])
