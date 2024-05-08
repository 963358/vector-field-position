import matplotlib
import numpy as np
import math as m

p1 = np.array[1, 1, 1] #position of object
r1 = np.array[0, -1, 0] #position of receiver
c = 343 #speed of sound

amplitude = 1 #constant
frequency = 10 #constant
d = m.sqrt(pow(p1[0] - r1[0], 2) + pow(p1[1] - r1[1], 2) + pow(p1[2] - r1[2], 2))

print(d);
t_int = 0.001
t = 0

# print("Sent!")
# while(True):
#     t += t_int
#     if(t >= d/c):
#         print("received!")
#         break;
#     else:
#         print(t)


