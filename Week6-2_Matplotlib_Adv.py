#------------------------------------------------------------------------------
__author__ = 'James T. Dietrich'
__contact__ = 'james.t.dietrich@dartmouth.edu'
__copyright__ = '(c) James Dietrich 2016'
__license__ = 'MIT'
__date__ = 'Wed Nov 16 11:33:39 2016'
__version__ = '1.0'
__status__ = "initial release"
__url__ = "https://github.com/geojames/..."

"""
Name:           Week6-1_Matplotlib_Adv.py
Compatibility:  Python 3.5
Description:    This program does stuff

URL:            https://github.com/geojames/...

Requires:       libraries

Dev ToDo:

AUTHOR:         James T. Dietrich
ORGANIZATION:   Dartmouth College
Contact:        james.t.dietrich@dartmouth.edu
Copyright:      (c) James Dietrich 2016

"""
#------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# MESHGRID
#
# Meshgrid is a command/function that allows you to easily build X and Y 
#   grids from 1-D arrays/vectors which can be used to evaluate equations
#   in 2D or 3D space

# different conventions for naming meshed variables
# x > xv
# x > xx
# x > xg
#
# meshgrid takes to 1-D arrays of X and Y coordinates and returns two X and Y
#   "meshes" 2D arrays that cover the X and Y spaces

x = np.linspace(-10.,10.,30)
y = np.linspace(-10.,10.,30)

xg, yg = np.meshgrid(x,y)

r = np.sqrt((xg**2 + yg**2))
z = np.sin(r) * xg**2

plt.pcolor(z)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(xg, yg, z,rstride=1, cstride=1, cmap='coolwarm')


# 3D Subplots

fig = plt.figure(figsize=plt.figaspect(0.33333))

ax1 = fig.add_subplot(1, 3, 1)
ax1.pcolor(z, cmap = 'hot')

ax2 = fig.add_subplot(1, 3, 2, projection='3d')
ax2.plot_surface(xg, yg, z,rstride=1, cstride=1, cmap='hot')

ax3 = fig.add_subplot(1, 3, 3, projection='3d')
ax3.contour(xg,yg,z)


#%% Formatted text for plots
#
# Matplotlib 
# http://matplotlib.org/users/mathtext.html#mathtext-tutorial

# it basically uses TeX syntax and formatting codes

def f(x,y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
xx,yy = np.meshgrid(x, y)

#plt.axes([0.025, 0.025, 0.95, 0.95])

plt.contourf(xx, yy, f(xx, yy), 8, alpha=.75, cmap=plt.cm.hot)
C = plt.contour(xx, yy, f(xx, yy), 8, colors='black', linewidth=0.5)
plt.clabel(C, inline=1, fontsize=10)

plt.text (-2.5,-2,r'$\frac{1-x}{2 + x^5 + y^3} \times e^{(-x^2 -y^2)}$',fontsize=20)

plt.xlabel(r'$\mathbf{Bold \ x}$ x', fontsize=20)
plt.ylabel(r'$\mathit{Y-Label}$', fontsize=20)
plt.title('Regular ' r'$\mathbf{Bold}$ $\mathit{and \ italic}$ words')


#%% Double Y Axis Plots (from the Matplotlib Gallery)

fig, ax1 = plt.subplots()
t = np.arange(0.01, 10.0, 0.01)
s1 = np.exp(t)
ax1.plot(t, s1, 'b-')
ax1.set_xlabel('time (s)')
# Make the y-axis label and tick labels match the line color.
ax1.set_ylabel('exp', color='b')
for tl in ax1.get_yticklabels():
    tl.set_color('b')


ax2 = ax1.twinx()
s2 = np.sin(2*np.pi*t)
ax2.plot(t, s2, 'r.')
ax2.set_ylabel('sin', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')