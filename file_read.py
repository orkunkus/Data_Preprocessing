# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:57:01 2021

@author: orkun
"""

from tkinter import filedialog
import tkinter as tk

root = tk.Tk()
root.wm_attributes('-topmost', 1)
root.withdraw()

# ---Read File Path
file_path = filedialog.askopenfilename(parent=root, initialdir="/", title='Please select a file')
print(file_path)
