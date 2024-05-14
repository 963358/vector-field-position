import matplotlib
import numpy as np
import math as m
import sympy
from collections import namedtuple

# p1 = np.array[1, 1, 1] #position of object
# r1 = np.array[0, -1, 0] #position of receiver

p1 = np.array([100, -123, 120]) #position of object

#Hydrophone = namedtuple("Hydrophone", ["x", "y", "z"])

#4 hydrophones
h0 = np.array([0,0,0]) 
h1 = np.array([1,0,0]) 
h2 = np.array([0,1,0]) 
h3 = np.array([0,0,1]) 
c = 343 #speed of sound

amplitude = 1 #constant
wlength = 1 #lamda
frequency = c/wlength #constant
period = 1/frequency
#d = m.sqrt(pow(p1[0] - r1[0], 2) + pow(p1[1] - r1[1], 2) + pow(p1[2] - r1[2], 2))
#print(d);

t_int = 0.0001
t = 0

#distance from source to hydrophones
d0 = m.sqrt(pow(p1[0] - h0[0], 2) + pow(p1[1] - h0[1], 2) + pow(p1[2] - h0[2], 2)) 
d1 = m.sqrt(pow(p1[0] - h1[0], 2) + pow(p1[1] - h1[1], 2) + pow(p1[2] - h1[2], 2))
d2 = m.sqrt(pow(p1[0] - h2[0], 2) + pow(p1[1] - h2[1], 2) + pow(p1[2] - h2[2], 2))
d3 = m.sqrt(pow(p1[0] - h3[0], 2) + pow(p1[1] - h3[1], 2) + pow(p1[2] - h3[2], 2))

print (d0, d1, d2, d3)

startDist = min(d0, d1, d2, d3)
print(startDist)
soundwaves = np.array([-1*d0 + startDist, -1*d1 + startDist, -1*d2 + startDist, -1*d3 + startDist])
Rad = []

print(soundwaves)
#soundwaves[0] < 0 or soundwaves[1] < 0 or soundwaves[2] < 0 or soundwaves[3] < 0
while(True):
    if (soundwaves[0] >= 0 and soundwaves[1] >= 0 and soundwaves[2] >= 0 and soundwaves[3] >= 0): #when all hydrophones have picked up signal
        Rad.append(d0/wlength*2*m.pi)
        Rad.append(d1/wlength*2*m.pi)
        Rad.append(d2/wlength*2*m.pi)
        Rad.append(d3/wlength*2*m.pi)
        break;

    soundwaves[0] += t_int*c
    soundwaves[1] += t_int*c
    soundwaves[2] += t_int*c
    soundwaves[3] += t_int*c
    t+= t_int
    print(t)

distance_offset = [Rad[0] - Rad[1], Rad[0] - Rad[2], Rad[0] - Rad[3]] #phase shifts

print(distance_offset[0])

for i in range(3):
    distance_offset[i]*= (wlength/(2*m.pi))

X, Y, Z = sympy.symbols("x y z")

solved_values = sympy.nsolve(
        (
            h1[0] ** 2 + h1[1] ** 2 + h1[2] ** 2  - distance_offset[0] ** 2 - (2 * X * h1[0] + 2 * Y * h1[1] + 2 * Z * h1[2] - 2 * sympy.sqrt(X ** 2 + Y ** 2 + Z ** 2) * distance_offset[0]),
            h2[0] ** 2 + h2[1] ** 2 + h2[2] ** 2  - distance_offset[1] ** 2 - (2 * X * h2[0] + 2 * Y * h2[1] + 2 * Z * h2[2] - 2 * sympy.sqrt(X ** 2 + Y ** 2 + Z ** 2) * distance_offset[1]),
            h3[0] ** 2 + h3[1] ** 2 + h3[2] ** 2  - distance_offset[2] ** 2 - (2 * X * h3[0] + 2 * Y * h3[1] + 2 * Z * h3[2] - 2 * sympy.sqrt(X ** 2 + Y ** 2 + Z ** 2) * distance_offset[2]),
        ),
        (X, Y, Z),
        (1, 1, 1)
    )
print(solved_values)

# print("Sent!")
# while(True):
#     t += t_int
#     if(t >= d/c):
#         print("received!")
#         break;
#     else:
#         print(t)


# def compute_coordinates(signal_1, signal_2, signal_3, frequency):
#     SOUND_WATER_SPEED_M = 1500
#     wavelength = SOUND_WATER_SPEED_M / frequency

#     Hydrophone = namedtuple("Hydrophone", ["x", "y"])

#     hydrophone1 = Hydrophone(0, 0)
#     hydrophone2 = Hydrophone(0, -0.013)
#     hydrophone3 = Hydrophone(0.013, -0.013)

#     phase_shift0_1 = phase_difference(signal_1, signal_2)
#     phase_shift0_2 = phase_difference(signal_2, signal_3)

#     distance_offset0_1 = (phase_shift0_1) / (np.pi * 2) * wavelength
#     distance_offset0_2 = (phase_shift0_2) / (np.pi * 2) * wavelength

#     print(distance_offset0_1, distance_offset0_2)

#     X, Y = sympy.symbols("x y")

#     print(hydrophone2.x ** 2 + hydrophone2.y ** 2 - distance_offset0_1 ** 2 - (2 * X * hydrophone2.x + 2 * Y * hydrophone2.y - 2 * sympy.sqrt(X ** 2 + Y ** 2) * distance_offset0_1))
#     print(hydrophone3.x ** 2 + hydrophone3.y ** 2 - distance_offset0_2 ** 2 - (2 * X * hydrophone3.x + 2 * Y * hydrophone3.y - 2 * sympy.sqrt(X ** 2 + Y ** 2) * distance_offset0_2))

#     solved_values = sympy.nsolve(
#         (
#             hydrophone2.x ** 2 + hydrophone2.y ** 2 - distance_offset0_1 ** 2 - (2 * X * hydrophone2.x + 2 * Y * hydrophone2.y - 2 * sympy.sqrt(X ** 2 + Y ** 2) * distance_offset0_1),
#             hydrophone3.x ** 2 + hydrophone3.y ** 2 - distance_offset0_2 ** 2 - (2 * X * hydrophone3.x + 2 * Y * hydrophone3.y - 2 * sympy.sqrt(X ** 2 + Y ** 2) * distance_offset0_2),
#         ),
#         (X, Y),
#         (2, 2)
#     )

#     # print(math.degrees(math.atan(solved_values[1]/solved_values[0])))

#     return (solved_values[0], solved_values[1])
