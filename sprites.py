import os
from ctypes import *

import pygame

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# screen.fill((0, 0, 0))
pygame.display.flip()
xx = windll.user32.GetSystemMetrics(0)
yy = windll.user32.GetSystemMetrics(1)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


def button(x, y, text_ru, text_en, size, language='ru', induced=False):
    global xx, yy

    if induced:
        button = load_image(f"menu\\{size}\\green_button.png")
    else:
        button = load_image(f"menu\\{size}\\button.png")

    if size == 'FullHD':
        button = pygame.transform.scale(button, (int(452 * (xx / 1920)), 90 * int(yy / 1080)))
        screen.blit(button, (int(x * (xx / 1920)), int(y * (yy / 1080))))
    else:
        button = pygame.transform.scale(button, (int(301 * (xx / 1280)), 60 * int((yy / 720))))
        screen.blit(button, (int(x * (xx / 1280)), int(y * (yy / 720))))


def left_gradient(size):
    global xx, yy

    gradient = load_image(f"menu\\{size}\\left_gradient.png")
    if size == 'FullHD':
        gradient = pygame.transform.scale(gradient, (int(602 * (xx / 1920)), yy))
    else:
        gradient = pygame.transform.scale(gradient, (int(401 * (xx / 1280)), yy))
    screen.blit(gradient, (0, 0))


def right_gradient(size):
    global xx, yy

    gradient = load_image(f"menu\\{size}\\right_gradient.png")
    if size == 'FullHD':
        gradient = pygame.transform.scale(gradient, (int(1320 * (xx / 1920)), yy))
        screen.blit(gradient, (int(600 * (xx / 1280)), 0))
    else:
        gradient = pygame.transform.scale(gradient, (int(880 * (xx / 1280)), yy))
        screen.blit(gradient, (int(400 * (xx / 1280)), 0))
pygame.quit()
