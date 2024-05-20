import matplotlib
import numpy as np
import sympy

def calculateRad(dist, wlength):
    Rad = []
    Rad.append((dist[0]/wlength*2*np.pi))
    Rad.append((dist[1]/wlength*2*np.pi))
    Rad.append((dist[2]/wlength*2*np.pi))
    Rad.append((dist[3]/wlength*2*np.pi))
        
    return Rad

def calculatePosition(Rad, wlength, hydrophones): #calculates position of the object with hydrophones
 
    h0 = hydrophones[0]
    h1 = hydrophones[1]
    h2 = hydrophones[2]
    h3 = hydrophones[3]

    distance_offset = [Rad[0] - Rad[1], Rad[0] - Rad[2], Rad[0] - Rad[3]] #phase shifts


    for i in range(3):
        distance_offset[i]*= (wlength/(2*np.pi))

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
    
    return(solved_values)

def GetPosition(p1): #shifts the object to the next position
    for i in range (3):
        p1[i] += 5
    return p1

def GetDist (p1, hydrophones): #sets up distances of 
    h0 = hydrophones[0]
    h1 = hydrophones[1]
    h2 = hydrophones[2]
    h3 = hydrophones[3]

    d0 = np.sqrt(pow(p1[0] - h0[0], 2) + pow(p1[1] - h0[1], 2) + pow(p1[2] - h0[2], 2)) 
    d1 = np.sqrt(pow(p1[0] - h1[0], 2) + pow(p1[1] - h1[1], 2) + pow(p1[2] - h1[2], 2))
    d2 = np.sqrt(pow(p1[0] - h2[0], 2) + pow(p1[1] - h2[1], 2) + pow(p1[2] - h2[2], 2))
    d3 = np.sqrt(pow(p1[0] - h3[0], 2) + pow(p1[1] - h3[1], 2) + pow(p1[2] - h3[2], 2))

    dist = [d0, d1, d2, d3]
    return dist

def InitSoundwave(dist):
    startDist = min(dist)

    soundwaves = np.array([-1*dist[0] + startDist, -1*dist[1] + startDist, -1*dist[2] + startDist, -1*dist[3] + startDist])
    
    return soundwaves

def GetVelocity(t_move, p0, p1):
    vel = []
    for i in range (3):
        vel.append((p1[i]-p0[i])/t_move)

    return vel


def calculate_wave(points):    
    hydrophones = np.array([[0,0,0], [1,0,0], [0,1,0], [0,0,1]]) 
    
    c = 343 #speed of sound

    amplitude = 1 #constant
    wlength = 1 #lamda
    frequency = c/wlength #constant
    period = 1/frequency
    
    t_int = 0.001 #hydrophone input intervals
    t_move = 0.15 #object movement intervals
   
    for i in range(3): # 4 points total, 2+1 is final one    
        pPrev = points[i] #position of object

        distPrev = GetDist(pPrev, hydrophones)

        soundwavesPrev = InitSoundwave(distPrev) #represents distance traversed by wave


        pCur = points[i+1]
            
        distCur = GetDist(pCur, hydrophones)
        soundwavesCur = InitSoundwave(distCur)


        radPrev = calculateRad(distPrev, wlength)
        radCur = calculateRad(distCur, wlength)

        pPrev = calculatePosition(radPrev, wlength, hydrophones)
        pCur = calculatePosition(radCur, wlength, hydrophones)
            

        vel = GetVelocity(t_move, pPrev, pCur)
        
        print("Calculated velocity: t = ", round(i*t_move,3), " --> ", round((i+1)*t_move,3))

        print("u: ", round(vel[0],3), "v: ", round(vel[1],3), "w: ", round(vel[2],3))
#        print("Velocity = ", np.sqrt(pow(round(vel[0],3), 2) + pow(round(vel[1],3), 2) + pow(round(vel[2],3), 2)))

        print("\n")
