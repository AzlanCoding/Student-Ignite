from PIL.Image import frombytes, merge#, tobytes
import numpy as np
import time
from direct.showbase.ShowBase import ShowBase
from panda3d.core import PandaNode
from panda3d.core import Vec3
from panda3d.core import Spotlight
from panda3d.core import Camera
from panda3d.core import NodePath
from panda3d.core import TransformState
from panda3d.core import RenderState
from panda3d.direct import throw_new_frame

from panda3d.core import loadPrcFileData
loadPrcFileData('', 'state-cache false')
loadPrcFileData('', 'transform-cache false')


SHOW_IMAGE = True
SHOW_MEM_STATS = True

if SHOW_IMAGE:
    import pygame

if SHOW_MEM_STATS:
    import  memory_profiler

def cvImageToSurface(cvImage):
    if cvImage.dtype.name == 'uint16':
        cvImage = (cvImage / 256).astype('uint8')
    size = cvImage.shape[1::-1]
    if len(cvImage.shape) == 2:
        cvImage = np.repeat(cvImage.reshape(size[1], size[0], 1), 3, axis = 2)
        format = 'RGB'
    else:
        format = 'RGBA' if cvImage.shape[2] == 4 else 'RGB'
        cvImage[:, :, [0, 2]] = cvImage[:, :, [2, 0]]
    surface = pygame.image.frombuffer(cvImage.flatten(), size, format)
    return surface.convert_alpha() if format == 'RGBA' else surface.convert()

class MyApp(ShowBase):
    def __init__(self, screen_size=84):
        ShowBase.__init__(self, windowType='offscreen')

        # Spotlight
        self.light = Spotlight('light')
        self.lightNP = self.render.attachNewNode(self.light)
        self.lightNP.setPos(0, 10, 10)
        self.lightNP.lookAt(0, 10, 10)
        self.render.setLight(self.lightNP)

        # Block
        node = PandaNode('Block')
        block_np = self.render.attachNewNode(node)
        model = loader.loadModel("./uploads_files_2112820_2016+Custom+Range+Rover+Sport+OBJ/2016 Custom Range Rover Sport.obj")
        model.reparentTo(block_np)

        self.start_time = time.time()


    def get_camera_image(self, requested_format=None):
        dr = self.camNode.getDisplayRegion(0)
        tex = dr.getScreenshot()
        data = tex.getRamImage().getData()
        #image = np.frombuffer(data, np.uint8)
        #image.shape = (tex.getYSize(), tex.getXSize(), tex.getNumComponents())
        sx=tex.getXSize()
        sy=tex.getYSize()
        b,g,r,a = frombytes("RGBA",(sx,sy),data).split()
        pyGmImg= pygame.image.fromstring(merge("RGBA",(r,g,b,a)).tobytes(),(sx,sy),"RGBA",True)
        #img2 = pygame.image.fromstring(image,(sx,sy),
        return pyGmImg


    def rotate_light(self):
        radius = 10
        step = 0.1
        t = time.time() - self.start_time
        angleDegrees = t * step
        angleRadians = angleDegrees * (np.pi / 180.0)
        self.lightNP.setPos(radius * np.sin(angleRadians), -radius * np.cos(angleRadians), 3)
        self.lightNP.lookAt(0, 0, 0)


    def step(self):
        self.rotate_light()
        self.graphicsEngine.renderFrame()
        image = self.get_camera_image()
        return image


def main():
    pygame.init()
    PyWin = pygame.display.set_mode((1536, 864),pygame.RESIZABLE)
    app = MyApp(screen_size=84*1)
    app.eventMgr.restart()
    step_num = 0

    if SHOW_MEM_STATS:
        last_mem = memory_profiler.memory_usage()[0]

    while True:
        step_num += 1
        image = app.step()

        if SHOW_IMAGE:
            #cv2.imshow('state', image)
            PyWin.fill(0)
            PyWin.blit(image, (0,0))
            pygame.display.flip()
            #key = cv2.waitKey(1) & 0xFF
            #if key == 27 or key == ord('q'):
                #print(type(image))
                #print("Pressed ESC or q, exiting")
                #exit()

        if SHOW_MEM_STATS:
            if step_num % 1000 == 0:
                now_mem = memory_profiler.memory_usage()[0]
                if step_num != 1000:
                    print('Memory per 1k steps:', now_mem-last_mem, 'MB')
                last_mem = now_mem

if __name__ == '__main__':
    main()
