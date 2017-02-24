import matplotlib.pyplot as plt
import numpy as np
from moviepy.video.io.bindings import mplfig_to_npimage
import moviepy.editor as mpy
import imageio
import pandas as pd



# Need to load tools for moviepy (one time only)
#imageio.plugins.ffmpeg.download()

# Chnange Directory to your working directory

# get data
city_pop = pd.read_excel('US_metro_area_population_1790_2010.xls', sheetname='metro_data_to_pandas') 

# get data for a single city
nyc = city_pop[(city_pop.metro_region == 'New York')]
boston = city_pop[(city_pop.metro_region == 'Boston')]
               
# build plot arrays
x = pd.np.array(nyc.year)
y1 = pd.np.array(nyc.population)/1000000
y2 = pd.np.array(boston.population)/1000000

#%%

# Make a static plot

fig_mpl, ax = plt.subplots(1,figsize=(6,5),facecolor='white')  # set up a figure window of a specfic size
ax.set_title('Populaiton Growth')
ax.set_ylim(-1,25)
ax.set_xlim(1780,2020)
plot = ax.plot(x,y1,'ro', markersize=10,markeredgecolor='k')




#%%
# Animate the plot --- plot one data point at a time

duration = 5   # length of movie in sections
fps = 5        # frames per second
 # note that i (our iterator) will equal duration * fps...  
 # this dictates how fast the movie will play.

 
 
# Set up plot outside of function that will make the slides 
fig_mpl, ax = plt.subplots(1,figsize=(6,5),facecolor='white')
xx = x  # x data 

zz = lambda d: y1  # the changing y dataset  -- using a function to update in the animation!

ax.set_title('Populaiton Growth')
ax.set_ylim(-1,25)
ax.set_xlim(1780,2020)
plot, = ax.plot(xx,zz(0),'ro', markersize=10,markeredgecolor='k')


# Animate with moviepy (update the plot for each t).  Then make the movie (mp4 or gif)
last_i = 0 # create an iterator
def make_frame_mpl(t):
    global last_i   # define a global variable that remembers the last iteratition number
    i = last_i      # set the current iteration number
    y1data = y1[:i]  # update data to feed the plot...  one point per iteration
    #y2data = y2[:i]    
    xdata = x[:i] 
    plot.set_data(xdata, y1data)  # update the plot
    #print(ydata)
    last_i = i+1    # update the iterator
    
    return mplfig_to_npimage(fig_mpl)  # RGB image of the figure <-- Make a "slide" of the plot
	
animation = mpy.VideoClip(make_frame_mpl, duration=duration)
animation.write_videofile('out.mp4', fps=fps)
#animation.write_gif('out.gif', fps=20)

# on Macs... strangely it is easiest to view GIFs in a web browswer

#%%
# Animate a continuous x,y data set

# exmaple from: http://zulko.github.io/blog/2014/11/29/data-animations-with-python-and-moviepy/

duration = 2

fig_mpl, ax = plt.subplots(1,figsize=(5,3),facecolor='white')
xx = np.linspace(-2,2,200)  # x data
zz = lambda d: np.sinc(xx**2)+np.sin(xx+d)  # the changing z data
ax.set_title('Elevation in y=0')
ax.set_ylim(-1.5,2.5)
line, = ax.plot(xx,zz(0), lw=3)

# Animate with moviepy (update the plot for each t).  Then make a MP4 or GIF

def make_frame_mpl(t):
	line.set_ydata( zz(2*np.pi*t/duration))  # update the plot
	return mplfig_to_npimage(fig_mpl)  # RGB image of the figure <-- Make a "slide" of the plot
	
animation = mpy.VideoClip(make_frame_mpl, duration=duration)
animation.write_videofile('sinc_mpl2.mp4', fps=20)

#%%

# An Example from the web that Runs in a Figure Window 
# using the Matplotlib Animation Library


"""
================
The Bayes update
================

This animation displays the posterior estimate updates as it is refitted when
new data arrives.
The vertical line represents the theoretical value to which the plotted
distribution should converge.
"""

# update a distribution based on new data.
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
from matplotlib.animation import FuncAnimation


class UpdateDist(object):
    def __init__(self, ax, prob=0.5):
        self.success = 0
        self.prob = prob
        self.line, = ax.plot([], [], 'k-')
        self.x = np.linspace(0, 1, 200)
        self.ax = ax

        # Set up plot parameters
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 15)
        self.ax.grid(True)

        # This vertical line represents the theoretical value, to
        # which the plotted distribution should converge.
        self.ax.axvline(prob, linestyle='--', color='black')

    def init(self):
        self.success = 0
        self.line.set_data([], [])
        return self.line,

    def __call__(self, i):
        # This way the plot can continuously run and we just keep
        # watching new realizations of the process
        if i == 0:
            return self.init()

        # Choose success based on exceed a threshold with a uniform pick
        if np.random.rand(1,) < self.prob:
            self.success += 1
        y = ss.beta.pdf(self.x, self.success + 1, (i - self.success) + 1)
        self.line.set_data(self.x, y)
        return self.line,

fig, ax = plt.subplots()
ud = UpdateDist(ax, prob=0.7)
anim = FuncAnimation(fig, ud, frames=np.arange(100), init_func=ud.init,
                     interval=100, blit=False)
plt.show()