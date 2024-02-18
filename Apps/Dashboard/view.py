from typing import Tuple
from customtkinter import (
    CTk, 
    CTkButton, 
    CTkFrame, 
    CTkLabel,
    BOTH, 
    TOP,
    LEFT,
    StringVar,
)

def Dashboard_frame(parent):
    '''
    Frame Base Para apoyarse
    params:
        - parent: Widget padre donde se alojará el frame
    returns:
        - dashboard_frame: Frame que se alojará en parent dado
    '''
    dashboard_frame = CTkFrame(parent, fg_color="White")
    name = CTkLabel(dashboard_frame, text="Dashboard", text_color="Black")
    name.pack()
    return dashboard_frame

class Main_Windows(CTk):
    '''
    Interface Principal de la APP sobre esta se deben montar los respectivos Frames
    '''
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title("Modelos de Teoría de Colas")
        self.seccion = StringVar()
        self.WIDTH = 800
        self.HEIGHT = 400
        self.wm_iconbitmap("./logo.ico")
        self.minsize(self.WIDTH, self.HEIGHT)
        self.initialize()

    def initialize(self):
        self.navbar = CTkFrame(self, height=30, fg_color="#0e141a", corner_radius=0)
        self.navbar.pack(fill = BOTH, side = TOP)
        # Navbar Start
        self.seccion_label = CTkLabel(self.navbar, textvariable=self.seccion)
        self.seccion_label.pack()
        # Navbar End

        self.sidebar = CTkFrame(self, width = 150, fg_color="#1e2833", corner_radius=0)
        self.sidebar.pack(fill = BOTH, side = LEFT)

        # Menu Start
        '''
        Sección donde se insertan los botones en la barra lateral y se le asigna su 
        correspondiente frame
        '''
        self.dashboard_boton = CTkButton(self.sidebar, text="Dashboard", height=40, command=lambda:self.switch_frame(Dashboard_frame,"Dashboard"))
        self.dashboard_boton.pack(pady = 5, padx = 5)
        # ---------------------------------
        self.model1_boton = CTkButton(self.sidebar, text="Model1", height=40, command=lambda:self.switch_frame(Dashboard_frame, "Dashboard2"))
        self.model1_boton.pack(pady = (0,5), padx = 5)
        # ---------------------------------
        self.model1_boton = CTkButton(self.sidebar, text="Model2", height=40, command=lambda:self.switch_frame(Dashboard_frame, "Dashboard3"))
        self.model1_boton.pack(pady = (0,5), padx = 5)
        # ---------------------------------
        self.model1_boton = CTkButton(self.sidebar, text="Model3", height=40, command=lambda:self.switch_frame(Dashboard_frame, "Dashboard4"))
        self.model1_boton.pack(pady = (0,5), padx = 5)
        # Menu End

        self.content = CTkFrame(self, fg_color="#1f2329", corner_radius=0)
        self.content.pack(expand=True, fill=BOTH)

        # Default Frame
        self.switch_frame(Dashboard_frame, "Dashboard")
    
    def switch_frame(self, new_frame, section):
        '''
        Función que permite el cambio de Frames
        Implementada por los botones de la barra lateral
        '''
        if  len(self.content.winfo_children()) > 0:
            self.content.winfo_children()[0].destroy()
        new = new_frame(self.content)
        new.pack(expand=True, fill = BOTH)
        self.seccion.set(section)