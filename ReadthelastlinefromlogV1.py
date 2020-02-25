#!/usr/bin/env python

#This small auto Python scrip file - Read the last a line from text file.
#Created by Tommas Huang
#Date: 2020-02-24
#Version: 1.0

#The OS module in python provides functions for interacting with the operating system. OS, comes under Python's standard utility modules.
import os
with open('/Users/TommasHuang/Documents/log-2.txt', 'rb') as f:
#Open file path. rb opens in binary read-write mode
        f.seek(-3, os.SEEK_END)
        #The seek () method is used to move the file read pointer to the specified position.
        while f.read(1) != b'\n':
                f.seek(-3, os.SEEK_CUR) 
                #os.SEEK_CUR: indicates the relative current position of the file
        print(f.readline().decode())
