# -*- coding: utf-8 -*-
"""SecHack365 Nightchallenge.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pLrW9TZgC8AlT9e98Kn633BpdlUyVxtR
"""

import tkinter as tk

for i in range(1, 1001):
    if i % 33 == 0:
        print("SEC")
    elif i % 13 == 0:
        print("HACK")
    elif i % 73 == 0:
        print("365")
    else:
        print(i)