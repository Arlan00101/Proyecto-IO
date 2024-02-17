from typing import Tuple
from customtkinter import (
    CTk, 
    CTkButton, 
    CTkFrame, 
    CTkLabel,
    BOTH, 
    TOP,
    LEFT
)

def Dashboard_frame(parent):
    dashboard_frame = CTkFrame(parent, fg_color="White")
    name = CTkLabel(dashboard_frame, text="Dashboard", text_color="Black")
    name.pack()
    return dashboard_frame

class Main_Windows(CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title("Dashboard")
        self.WIDTH = 800
        self.HEIGHT = 400
        self.minsize(self.WIDTH, self.HEIGHT)
        self.initialize()

    def initialize(self):
        self.navbar = CTkFrame(self, height=30, bg_color="Gray", corner_radius=0)
        self.navbar.pack(fill = BOTH, side = TOP)
        self.sidebar = CTkFrame(self, width = 150, bg_color="Gray", corner_radius=0)
        self.sidebar.pack(fill = BOTH, side = LEFT)

        # Menu Start
        self.dashboard_boton = CTkButton(self.sidebar, text="Dashboard", height=40, command=lambda:self.switch_frame(Dashboard_frame))
        self.dashboard_boton.pack(pady = 5)
        # ---------------------------------
        
        # Menu End

        self.content = CTkFrame(self, fg_color="Gray", corner_radius=0)
        self.content.pack(expand=True, fill=BOTH)

        self.switch_frame(Dashboard_frame)
    
    def switch_frame(self,new_frame):
        if  len(self.content.winfo_children()) > 0:
            self.content.winfo_children()[0].destroy()
        new = new_frame(self.content)
        new.pack(expand=True, fill = BOTH)