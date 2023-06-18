from ursina import *                    # Import the ursina engine
import cv2
import numpy as np
import win32gui
from win32con import SW_HIDE

@staticmethod
def hide_window(name):
    try:
        win32gui.ShowWindow(win32gui.FindWindow(None, name), SW_HIDE)
    except win32gui.error:
        print("Error while finding or hiding window")
        return None

window.title = 'Ursina Output'          # The window title
#window.setMinimized(True)

global frames
frames = 0

app = Ursina()    # Initialise your Ursina app




window.borderless = False               # Show a border
#window.fullscreen = False               # Do not go Fullscreen
#window.exit_button.visible = False      # Do not show the in-game red X that loses the window
#window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter

cube = Entity(model='cube', color=color.orange, scale=(2,2,2))

app.graphicsEngine.renderFrame()

def update():
    global frames
    cube.rotation_y += time.dt * 100    # Rotate every time update is called
    if held_keys['t']:                  # If t is pressed
        print(held_keys['t'])           # Print the value
    dr = app.camNode.getDisplayRegion(0)
    tex = dr.getScreenshot()
    data = tex.getRamImage()
    image = np.frombuffer(data, np.uint8)
    image.shape = (tex.getYSize(), tex.getXSize(), tex.getNumComponents())
    img = np.fliplr(np.flip(image))[:,:,::-1]
    cv2.imshow('state', img)
    if frames < 2:
        hide_window('Ursina Output')
        frames += 1
app.run()
