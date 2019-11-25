# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:44:25 2019

@author: errol
"""

import os
from tkinter import *


class OpenImageGUI:
  def __init__(self, master):
    #root frame properties
    self.parent = master
    self.center(self.parent, 700, 560)
  
  def center(self, root, width, height):
    x = (root.winfo_screenwidth() // 2) - (width//2)
    y = (root.winfo_screenheight() // 2) - (height//2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    
if __name__ == '__main__':
  root = Tk()
  win = OpenImageGUI(root)
  root.mainloop()