import tkinter as tk 
from tkinter import ttk
from turtle import bgcolor

class world (ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        

        #label
        self.label = ttk.Label( self, test ='', bg='white')
        