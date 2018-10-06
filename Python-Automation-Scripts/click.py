#!/usr/bin/python2.7

"""
------------------------------------------
		License Information
------------------------------------------
        GNU GENERAL PUBLIC LICENSE
        Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation, Inc. 
https://fsf.org/ Everyone is permitted to copy and 
distribute verbatim copies of this license document, 
but changing it is not allowed.

Note: For detailed license information, 
please read the LICENSE file in the repository[Repository Name: Python-Automation]
"""

"""
script name   : click.py
Functionality : Keeps the window active by clicking every 10 seconds
Created on    : 21 SEP 2017
"""

__author__ = 'Ganesh'

import win32api, win32con
import time
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


while 1:
    click(10,10)
    time.sleep(10)