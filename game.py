import pygame
import os
from PIL import Image
from ctypes  import *
audio_fl = bool(open('settings.txt').read().split('\n')[0].split(' = ')[1])
music_fl = bool(open('settings.txt').read().split('\n')[1].split(' = ')[1])

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

# Размеры экрана
x = windll.user32.GetSystemMetrics(0)
y = windll.user32.GetSystemMetrics(1)

# инициализация pygame
pygame.init()

# создание полноэкранного окна
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

# создание окна 720 720
#screen = pygame.display.set_mode((720, 720))

screen.fill((0, 0, 0))
pygame.display.flip()
# рисование меню
menu = load_image("game\{}.png".format(open('progress.txt').read()))
screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
pygame.display.flip()
# Игровой цикл
running = True
while running:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            xx, yy = pygame.mouse.get_pos()
            xx = xx - (x-menu.get_width())//2
            yy = yy - (y-menu.get_height())//2            

        if event.type == pygame.MOUSEMOTION:
            xx, yy = pygame.mouse.get_pos()
            xx = xx - (x-menu.get_width())//2
            yy = yy - (y-menu.get_height())//2
            
    # обновление экрана
    pygame.display.flip()
pygame.quit()