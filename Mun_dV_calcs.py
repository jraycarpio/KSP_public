# Calculate dV's for Mun transfer in Kerbal Space Program
# By Jonathan Carpio



import math



# Standard gravitational constant for Kerbin
GM_k = 3.5315999770464 * math.pow(10, 12)

# Standard gravitational constant for the Mun
GM_mun = 6.5138 * math.pow(10, 10)

# Radius for initial circular orbit around Kerbin
r1 = 700000

# Semi-major axis of transfer manuever (elliptical orbit)
a_trans = 6175000

# Distance (radius) from spacecraft to Kerbin, upon closest approach to the Mun
r2 = 11650000

# Radius for final circular orbit around the Mun
rFinal = 400000



# Define functions for mathematical equations
def visviva(r, a, GM):
    return math.sqrt((2*GM/r) - (GM/a))

def circVel(r, GM):
    return math.sqrt(GM/r)

def dV(v2, v1):
    return v2 - v2



# Calculate delta V's and print results
dV1 = circVel(r1, GM_k) 
dV2 = visviva(r1, a_trans, GM_k) - circVel(r1, GM_k)
dV3 = circVel(rFinal, GM_mun) - visviva(r2, a_trans, GM_k)


print('\n\n')
print('delta V1 = ' + str(dV1) + ' m/s')
print('delta V2 = ' + str(dV2) + ' m/s')
print('delta V3 = ' + str(dV3) + ' m/s')
print(visviva(r2, a_trans, GM_k))
print('\n')

