from ursina import *                    # Import the ursina engine
import pygame
#import numpy as np
import win32gui
from win32con import SW_HIDE
from PIL.Image import frombytes, merge#, tobytes

@staticmethod
def hide_window(name):
    try:
        win32gui.ShowWindow(win32gui.FindWindow(None, name), SW_HIDE)
    except win32gui.error:
        print("Error while finding or hiding window")
        return None


pygame.init()


window.title = 'Ursina Output'          # The window title
#window.setMinimized(True)

global PyWin

PyWin = pygame.display.set_mode((1536, 864),pygame.RESIZABLE)

global frames
frames = 0

app = Ursina()    # Initialise your Ursina app




window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
#window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter

cube = Entity(model='cube', color=color.orange, scale=(2,2,2))

app.graphicsEngine.renderFrame()

def update():
    global frames
    global PyWin
    cube.rotation_y += time.dt * 100    # Rotate every time update is called
    if held_keys['t']:                  # If t is pressed
        print(held_keys['t'])           # Print the value
    dr = app.camNode.getDisplayRegion(0)
    tex = dr.getScreenshot()
    data = tex.getRamImage().getData()
    sx=tex.getXSize()
    sy=tex.getYSize()
    b,g,r,a = frombytes("RGBA",(sx,sy),data).split()
    pyGmImg= pygame.image.fromstring(merge("RGBA",(r,g,b,a)).tobytes(),(sx,sy),"RGBA",True)
    PyWin.fill(0)
    PyWin.blit(pyGmImg, (0,0))
    pygame.display.flip()
    if frames < 2:
        hide_window('Ursina Output')
        frames += 1
app.run()
