from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from moviepy.video.io.bindings import mplfig_to_npimage
import moviepy.editor as mpy
import imageio
import pandas as pd



# get data

# read in excel sheets as pandas dataframes
city_pop = pd.read_excel('US_metro_area_population_1790_2010.xls', sheetname='metro_data_to_pandas') 

# get data for a single year
year_pop = city_pop[(city_pop.year == 2010)]


'''
# get data for a single city
nyc = city_pop[(city_pop.metro_region == 'New York')]
boston = city_pop[(city_pop.metro_region == 'Boston')]
'''
            
# build plot arrays
lons = pd.np.array(year_pop.lon)
lats = pd.np.array(year_pop.lat)
pop = pd.np.array(year_pop.population)
marker_size = np.sqrt(pop)


#%%

# Create a Static Map with Data for 1 Census Year

# setup Lambert Conformal basemap.
# set resolution=None to skip processing of boundary datasets.

fig_mpl, ax = plt.subplots(1,figsize=(9,7.75),facecolor='white')
ax.set_title('20 Largest Metro Regions in 2010')
m = Basemap(width=6000000,height=4500000,projection='lcc',
            resolution='l',lat_1=45.,lat_2=55,lat_0=40,lon_0=-97.)

# lat1 and lat2 are the reference parallels for the conic projection
# lat and lon set the center of the map
# width and height are in meters

# Convert data to map coordinates -- CRITICAL!!
x, y = m(lons,lats) 

# draw them on the map
m.scatter(x,y,marker_size,marker='o',facecolor='r', edgecolor='k', alpha=0.5)

# add stuff to the map
# draw coastlines and political boundaries.
m.drawcoastlines()
m.drawcountries()
#m.drawstates()

# or use the NASA Blue Marble Imagery
#m.bluemarble()


#%%
# --- NOT WORKING YET ----

# Animate the Map --- plot one data point at a time

duration = 11.5   # length of movie in sections
fps = 2        # frames per second
 # note that i (our iterator) will equal duration * fps...  
 # this dictates how fast the movie will play.

 
 
# Set up plot outside of function that will make the slides 
fig_mpl, ax = plt.subplots(1,figsize=(9,7.75),facecolor='white')
ax.set_title('20 Largest Metro Regions in 2010')
m = Basemap(width=6000000,height=4500000,projection='lcc',
            resolution='l',lat_1=45.,lat_2=55,lat_0=40,lon_0=-97.)
m.drawcoastlines()
m.drawcountries()

x, y = m(lons,lats) 
xx = lambda d: x
zz = lambda d: y
m.scatter(x,y,marker_size,marker='o',facecolor='r', edgecolor='k', alpha=0.5)
plot = m.scatter(xx(0),zz(0),marker_size,marker='o',facecolor='r', edgecolor='k', alpha=0.5)

# Animate with moviepy (update the plot for each t).  Then make the movie (mp4 or gif)
last_i = 0 # create an iterator
def make_frame_mpl(t):
    global last_i   # define a global variable that remembers the last iteratition number
    i = last_i      # set the current iteration number
    ydata = y[:i]  # update data to feed the plot...  one point per iteration    
    xdata = x[:i] 
    plot.set_data(xdata, ydata)  # update the plot
    #print(ydata)
    last_i = i+1    # update the iterator
    
    return mplfig_to_npimage(fig_mpl)  # RGB image of the figure <-- Make a "slide" of the plot
	
animation = mpy.VideoClip(make_frame_mpl, duration=duration)
animation.write_videofile('out.mp4', fps=fps)
#animation.write_gif('out.gif', fps=20)

# on Macs... strangely it is easiest to view GIFs in a web browswer

#%%

# Grabbed From the Web...  : http://stackoverflow.com/questions/21207513/matplotlib-basemap-animation	

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
my_map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0,
          lat_0=0, lon_0=-130)
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'gray')
my_map.drawmapboundary()
my_map.drawmeridians(np.arange(0, 360, 30))
my_map.drawparallels(np.arange(-90, 90, 30))

x,y = my_map(0, 0)
point = my_map.plot(x, y, 'ro', markersize=5)[0]

def init():
    point.set_data([], [])
    return point,

# animation function.  This is called sequentially
def animate(i):
    lons, lats =  np.random.random_integers(-130, 130, 2)
    x, y = my_map(lons, lats)
    point.set_data(x, y)
    return point,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(plt.gcf(), animate, init_func=init,
                               frames=20, interval=500, blit=True)

plt.show()


