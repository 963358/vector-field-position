import matplotlib
import numpy as np
import math as m
import sympy
from collections import namedtuple

# p1 = np.array[1, 1, 1] #position of object
# r1 = np.array[0, -1, 0] #position of receiver

def calculatePosition(Rad, wlength, h1): #calculates position of the object with hydrophones
#print("Radians:", Rad[0])
    # x = (d0/wlength - d1/wlength)*2*m.pi
    # print(x)

    distance_offset = [Rad[0] - Rad[1], Rad[0] - Rad[2], Rad[0] - Rad[3]] #phase shifts

    #print(distance_offset[0])

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
    print("Hydrophones have detected object at:", solved_values)
    #print(solved_values[0])
    return(solved_values)

def GetPosition(p1): #shifts the object to the next position
    for i in range (3):
        p1[i] += 5
    return p1

def GetDist (p1, h0, h1, h2, h3): #sets up distances of 
    d0 = m.sqrt(pow(p1[0] - h0[0], 2) + pow(p1[1] - h0[1], 2) + pow(p1[2] - h0[2], 2)) 
    d1 = m.sqrt(pow(p1[0] - h1[0], 2) + pow(p1[1] - h1[1], 2) + pow(p1[2] - h1[2], 2))
    d2 = m.sqrt(pow(p1[0] - h2[0], 2) + pow(p1[1] - h2[1], 2) + pow(p1[2] - h2[2], 2))
    d3 = m.sqrt(pow(p1[0] - h3[0], 2) + pow(p1[1] - h3[1], 2) + pow(p1[2] - h3[2], 2))

    dist = [d0, d1, d2, d3]
    return dist

def InitSoundwave(dist):
    startDist = min(dist[0], dist[1], dist[2], dist[3])
    soundwaves = np.array([-1*dist[0] + startDist, -1*dist[1] + startDist, -1*dist[2] + startDist, -1*dist[3] + startDist])
    return soundwaves

def GetVelocity(t_move, p0, p1):
    vel = []
    for i in range (3):
        vel.append((p1[0]-p0[0])/t_move)

    return vel


p1 = np.array([100, 120, 150]) #position of object
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

t_int = 0.001 #hydrophone input intervals
t_move = 0.1 #object movement intervals
t = 0 #simulation time

#distance from source to hydrophones
# d0 = m.sqrt(pow(p1[0] - h0[0], 2) + pow(p1[1] - h0[1], 2) + pow(p1[2] - h0[2], 2)) 
# d1 = m.sqrt(pow(p1[0] - h1[0], 2) + pow(p1[1] - h1[1], 2) + pow(p1[2] - h1[2], 2))
# d2 = m.sqrt(pow(p1[0] - h2[0], 2) + pow(p1[1] - h2[1], 2) + pow(p1[2] - h2[2], 2))
# d3 = m.sqrt(pow(p1[0] - h3[0], 2) + pow(p1[1] - h3[1], 2) + pow(p1[2] - h3[2], 2))
# dist = [d0, d1, d2, d3] #array of distances to the hydrophones

dist = GetDist(p1, h0, h1, h2, h3)
#print (dist[0], dist[1], dist[2], dist[3])

startDist = min(dist[0], dist[1], dist[2], dist[3])
# print(startDist)
# soundwaves = np.array([-1*d0 + startDist, -1*d1 + startDist, -1*d2 + startDist, -1*d3 + startDist])

soundwaves = InitSoundwave(dist) #represents distance traversed by wave
Rad = [0, 0, 0, 0] #phase of the wave
n = 1 
pCur = p1 #current detected position
pPrev = p1 #previous detected position (used for velocity calculation)
#solved_values = 

#print(soundwaves)
#soundwaves[0] < 0 or soundwaves[1] < 0 or soundwaves[2] < 0 or soundwaves[3] < 0
foundlocation = False;

while(True):

    if(t >= t_move*n): #object moves to the next location after t_move
        #p0 = solved_values
        #print("old pos:", p0)
        pPrev = pCur
        p1 = GetPosition(p1)
        dist = GetDist(p1, h0, h1, h2, h3)
        soundwaves = InitSoundwave(dist)
        print("New position:", p1)
        # if(n > 1):
        #         vel = GetVelocity(t_move, pCur, p1)
        #         print("Calculated velocity:", vel)
        foundlocation = False
        n +=1
        #solved_values = calculatePosition(Rad, wlength, h1)
        #print(dist)
    
    if (soundwaves[0] >= 0 and soundwaves[1] >= 0 and soundwaves[2] >= 0 and soundwaves[3] >= 0): #when all hydrophones have picked up signal
        # Rad.append(soundwaves[0]/wlength*2*m.pi)
        # Rad.append(soundwaves[1]/wlength*2*m.pi)
        # Rad.append(soundwaves[2]/wlength*2*m.pi)
        # Rad.append(soundwaves[3]/wlength*2*m.pi)
        Rad[0] = (dist[0]/wlength*2*m.pi)
        Rad[1] = (dist[1]/wlength*2*m.pi)
        Rad[2] = (dist[2]/wlength*2*m.pi)
        Rad[3] = (dist[3]/wlength*2*m.pi)

        if(foundlocation == False): #calculate position if location already not determined
            print("Move", n)
            pCur = calculatePosition(Rad, wlength, h1)
            foundlocation = True
            if(n > 1):
                vel = GetVelocity(t_move, pPrev, pCur)
                print("Calculated velocity:", vel)

        #break;

    soundwaves[0] += t_int*c
    soundwaves[1] += t_int*c
    soundwaves[2] += t_int*c
    soundwaves[3] += t_int*c
    t+= t_int

    #print(t) 
    if(n > 3): #after 3 moves, terminate code
        break;





# def calculatePosition(Rad, wlength, h1):
# #print("Radians:", Rad[0])
#     # x = (d0/wlength - d1/wlength)*2*m.pi
#     # print(x)

#     distance_offset = [Rad[0] - Rad[1], Rad[0] - Rad[2], Rad[0] - Rad[3]] #phase shifts

#     print(distance_offset[0])

#     for i in range(3):
#         distance_offset[i]*= (wlength/(2*m.pi))

#     X, Y, Z = sympy.symbols("x y z")

#     solved_values = sympy.nsolve(
#             (
#                 h1[0] ** 2 + h1[1] ** 2 + h1[2] ** 2  - distance_offset[0] ** 2 - (2 * X * h1[0] + 2 * Y * h1[1] + 2 * Z * h1[2] - 2 * sympy.sqrt(X ** 2 + Y ** 2 + Z ** 2) * distance_offset[0]),
#                 h2[0] ** 2 + h2[1] ** 2 + h2[2] ** 2  - distance_offset[1] ** 2 - (2 * X * h2[0] + 2 * Y * h2[1] + 2 * Z * h2[2] - 2 * sympy.sqrt(X ** 2 + Y ** 2 + Z ** 2) * distance_offset[1]),
#                 h3[0] ** 2 + h3[1] ** 2 + h3[2] ** 2  - distance_offset[2] ** 2 - (2 * X * h3[0] + 2 * Y * h3[1] + 2 * Z * h3[2] - 2 * sympy.sqrt(X ** 2 + Y ** 2 + Z ** 2) * distance_offset[2]),
#             ),
#             (X, Y, Z),
#             (1, 1, 1)
#         )

#     print("Hydrophones have detected object at:", solved_values)


# def getposition()

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
