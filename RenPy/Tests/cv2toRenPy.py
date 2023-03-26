#From https://stackoverflow.com/questions/64183409/how-do-i-convert-an-opencv-image-bgr-and-bgra-to-a-pygame-surface-object
import os
import pygame
import cv2 as cv
import numpy as np

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

pygame.init()
window = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

cvImage1 = cv.imread('woodtiles.jpg', cv.IMREAD_GRAYSCALE)
cvImage2 = cv.imread('woodtiles.jpg', cv.IMREAD_UNCHANGED)
cvImage3 = cv.imread('Apple1-256.png', cv.IMREAD_UNCHANGED)
pygameSurface1 = cvImageToSurface(cvImage1)
pygameSurface2 = cvImageToSurface(cvImage2)
pygameSurface3 = cvImageToSurface(cvImage3)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    window.blit(pygameSurface1, pygameSurface1.get_rect(topleft = window.get_rect().inflate(-10, -10).topleft))
    window.blit(pygameSurface2, pygameSurface2.get_rect(center = window.get_rect().center))
    window.blit(pygameSurface3, pygameSurface3.get_rect(bottomright = window.get_rect().inflate(-10, -10).bottomright))
    pygame.display.flip()

pygame.quit()
