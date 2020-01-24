import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
import math

fig = plt.figure()
ax = plt.axes(projection='3d')



r_start = -5 # chunck of real number space to feed equation
r_end = 5

z_pad = 2 # padding between onion layers

growth_rate_r = 1.2 # expand real number space by x percent to better see next layer 
growth_rate_density = .8

density_init = 40

contours = [-1, 1]

Z = []
X = []
Y = []

pad = 0
for c in contours:


    real_x = np.linspace(r_start, r_end, density_init)
    real_y = np.linspace(r_start, r_end, density_init)

    for i in real_x:
        for j in real_y:
            if(math.sqrt(i**2 + j**2) < r_end):
                #rather than feeding a grid, I wanna feed a circle

                #solve for z in z^2 = contour + x^2 + y^2
                val = c + i**2 + j**2
                if val > 0:
                    Z.append(math.sqrt(val) + pad)
                    Z.append(-math.sqrt(val) - pad)
                    X.append(i)
                    X.append(i)
                    Y.append(j)
                    Y.append(j)

    r_start *= growth_rate_r
    r_end *= growth_rate_r
    density_init *= growth_rate_density
    pad += z_pad

ax.scatter(X, Y, Z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.title("contours of onion at : " + str(contours))
plt.show()
