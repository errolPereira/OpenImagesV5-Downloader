# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 19:44:25 2019

@author: errol
"""

import os
from tkinter import *
from tkinter import ttk
import wget


class OpenImageGUI:
  def __init__(self, master):
    #root frame properties
    self.parent = master
    self.parent.title('OpenImagesV5 Downloader')
    #self.parent.focus_force()
    self.center(self.parent, 700, 560)
    
    #frame for downloading csv files
    self.downloadPanel = Toplevel()
    self.center(self.downloadPanel, 350, 60)
    self.downloadPanel.focus_force()
    self.downloadFrame = Frame(self.downloadPanel, bg='#55A3AA')
    self.downloadFrame.pack(fill=BOTH, expand=1)
    
    
    #input form for downloadFrame
    self.message = Label(self.downloadFrame, text='Do you want to download the annotations and label information?', bg='#55A3AA')
    self.message.grid(row=0, column=0, columnspan=2)
    self.yesDownload = Button(self.downloadFrame, text='Yes', command=self.download_csv, width=10, height=1, padx=2, pady=1, bg='#79fd02')
    self.yesDownload.grid(row=1
                          ,column=0)
    self.noDownload = Button(self.downloadFrame, text='No', command=self.destroyPanel, width=10, height=1, padx=2, pady=1, bg='#8602FD')
    self.noDownload.grid(row=1,column=1)
    self.downloadPanel.protocol("WM_DELETE_WINDOW", self.destroyPanel)
  
  
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
  
  #function to download the csv files of OpenImagesV5
  def download_csv(self):
    print('Downloading')
    '''
    wget https://storage.googleapis.com/openimages/2018_04/class-descriptions-boxable.csv
 
    wget https://storage.googleapis.com/openimages/2018_04/train/train-annotations-bbox.csv
 
    wget https://storage.googleapis.com/openimages/2018_04/validation/validation-annotations-bbox.csv
 
    wget https://storage.googleapis.com/openimages/2018_04/test/test-annotations-bbox.csv 
    '''
    
    wget.download('https://storage.googleapis.com/openimages/2018_04/class-descriptions-boxable.csv', 'csv/')
    self.progress = ttk.Progressbar(self.downloadFrame, orient="horizontal",
                                        length=200, mode="determinate")
    self.progress.grid(row=2, column=0)
      
    
    
  def destroyPanel(self):
    self.downloadPanel.destroy()
    self.parent.focus_force()
    
if __name__ == '__main__':
  root = Tk()
  win = OpenImageGUI(root)
  root.mainloop()