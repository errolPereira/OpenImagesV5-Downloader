# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:44:25 2019

@author: errol
"""

import os
from tkinter import *
from tkinter import ttk
import wget
import time 
import requests


class OpenImageGUI:
  def __init__(self, master):
    #root frame properties
    self.parent = master
    self.parent.title('OpenImagesV5 Downloader')
    #self.parent.focus_force()
    self.center(self.parent, 570, 330)
    
    #Main Frame
    self.frame = Frame(self.parent)
    self.frame.pack(fill=BOTH, expand=1)
    self.parent.resizable(width=False, height=False)
    
    # Control Panel
    self.app_frame = Frame(self.frame)
    self.app_frame.grid(row=0, column=0, sticky=W + N)
    
    #labels
    self.img_class = Label(self.app_frame, text='Image Clases', anchor='w')
    self.img_class.grid(row=1, column=0, sticky=W + N, pady=10)
    
    self.mode = Label(self.app_frame, text='Mode', anchor='w')
    self.mode.grid(row=2, column=0, sticky=W + N, pady=10)
    
    self.occluded = Label(self.app_frame, text='Include Ocluded images', anchor='w')
    self.occluded.grid(row=3, column=0, sticky=W + N, pady=10)
    
    self.truncated = Label(self.app_frame, text='Include truncated images', anchor='w')
    self.truncated.grid(row=4, column=0, sticky=W + N, pady=10)
    
    self.groupOf = Label(self.app_frame, text='Include groupOf images', anchor='w')
    self.groupOf.grid(row=5, column=0, sticky=W + N, pady=10)
    
    self.depiction = Label(self.app_frame, text='Include depiction images', anchor='w')
    self.depiction.grid(row=6, column=0, sticky=W + N, pady=10)
    
    self.inside = Label(self.app_frame, text='Include inside images', anchor='w')
    self.inside.grid(row=7, column=0, sticky=W + N, pady=10)
    
    #inputs
    self.class_in = Entry(self.app_frame, text="Enter label", width=70)
    self.class_in.grid(row=1, column=1, sticky=W + N, columnspan=5, pady=10)
    
    
    self.var_mode = StringVar()
    self.var_mode.set('train') 

    self.var_occlude = IntVar()
    self.var_occlude.set(1)  

    self.var_truncated = IntVar()
    self.var_truncated.set(1)

    self.var_groupOf = IntVar()
    self.var_groupOf.set(1)  

    self.var_depiction = IntVar()
    self.var_depiction.set(1)         
    
    self.var_inside = IntVar()
    self.var_inside.set(1)   
    
    # Dictionary to create multiple buttons 
    values = {"train" : "train", 
              "test" : "test", 
              "val" : "validation"} 
    
    values_inc = {
            'yes' : '1',
            'no' : '0'
        }
    
    for i, (text, value) in enumerate(values.items()): 
        Radiobutton(self.app_frame, text = text, variable = self.var_mode, 
                    value = value, width=10).grid(row=2, column=i+1) 
    
    for i, (text, value) in enumerate(values_inc.items()): 
        Radiobutton(self.app_frame, text = text, variable = self.var_occlude, 
                    value = value, width=10).grid(row=3, column=i+1) 
    
    for i, (text, value) in enumerate(values_inc.items()): 
        Radiobutton(self.app_frame, text = text, variable = self.var_truncated, 
                    value = value, width=10).grid(row=4, column=i+1) 
    
    for i, (text, value) in enumerate(values_inc.items()): 
        Radiobutton(self.app_frame, text = text, variable = self.var_groupOf, 
                    value = value, width=10).grid(row=5, column=i+1) 
    
    for i, (text, value) in enumerate(values_inc.items()): 
        Radiobutton(self.app_frame, text = text, variable = self.var_depiction, 
                    value = value, width=10).grid(row=6, column=i+1) 
    
    for i, (text, value) in enumerate(values_inc.items()): 
        Radiobutton(self.app_frame, text = text, variable = self.var_inside, 
                    value = value, width=10).grid(row=7, column=i+1) 
        
    self.submit = Button(self.app_frame, text='Start Downloading', width=20, height=1,  bg='red', pady=5, command=self.preprocess_input)
    self.submit.grid(row=8, column=0, columnspan=7)
    
    
    
  #function to extract the classes and user inputs and start downloading   
  def preprocess_input(self):
      '''
          This function will preprocess the inputs of the user and call the download function
          to start downloading.
          
          Input : None
                  
          Output : None.
      '''
      #getting classes
      classes = self.class_in.get().split(',')
      #stipping spaces and keeping only unique classes
      classes = list(dict.fromkeys([s.strip() for s in classes]))
      
      self.download_dataset(classes)
      
      
  #function to start the download
  def download_dataset(self, classes):
    print('Downloading')
    command = 'python downloadIo.py --classes {0} --mode {1} --groupOf={2} --inside={3} --occlude={4} --depiction={5} --truncated={6}'.format(
     classes, self.var_mode.get(), self.var_groupOf.get(), self.var_inside.get(), 
     self.var_occlude.get(), self.var_depiction.get(), self.var_truncated.get()
     )
    print(command)
    os.system(command)
    
    
    
  #function to center the application on the screen
  def center(self, root, width, height):
    '''
      This function will center the application on the scree.
      
      Input : root - window to be centered
              width - width of the window
              height - height of the window
      Output : None.
    '''
    x = (root.winfo_screenwidth() // 2) - (width//2)
    y = (root.winfo_screenheight() // 2) - (height//2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

  def destroyPanel(self):
    self.downloadPanel.destroy()
    self.parent.focus_force()
    
if __name__ == '__main__':
  root = Tk()
  win = OpenImageGUI(root)
  root.mainloop()