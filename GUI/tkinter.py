#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
__author__ = 'James T. Dietrich'
__contact__ = 'james.t.dietrich@dartmouth.edu'
__copyright__ = '(c) James Dietrich 2016'
__license__ = 'MIT'
__date__ = 'Fri Feb 24 11:06:15 2017'
__version__ = '1.0'
__status__ = "initial release"
__url__ = "https://github.com/geojames/..."

"""
Name:           __name__.py
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
# Tkinter Examples

#------------------------------------------------------------------------------
#%% http://zetcode.com/gui/tkinter/introduction/

import tkinter as tk

class Window(tk.Frame):
  
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        
        self.initUI()
        
    
    def initUI(self):
      
        self.parent.title("Simple")
        self.pack(fill=tk.BOTH, expand=1)
        

def main():
  
    root = tk.Tk()
    root.geometry("250x150+300+300")
    app = Window(root)
    root.mainloop()  


if __name__ == '__main__':
    main()

#%%

import tkinter as tk


class Window(tk.Frame):
  
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
        
    def initUI(self):
      
        self.parent.title("Quit button")

        self.pack(fill=tk.BOTH, expand=1)

        quitButton = tk.Button(self, text="Quit", command=self.quit)
        quitButton.place(x=50, y=50)


def main():
  
    root = tk.Tk()
    root.geometry("250x150+300+300")
    app = Window(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
    
#%%  http://www.tkdocs.com/tutorial/firstexample.html

from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

# Setup window
root = Tk()
root.title("Feet to Meters")

# Set window layout
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# variables
feet = StringVar()
meters = StringVar()

# add feet input box
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

# create label for output and add caluclate button
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# add other labels
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# apply the window layout
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# make the feet text box the "focus" and bind the enter/return key to the calc button
feet_entry.focus()
root.bind('<Return>', calculate)

# run in a loop
root.mainloop()

#%%