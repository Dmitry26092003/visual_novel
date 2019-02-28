import pygame
import os
from PIL import Image
from ctypes import *
import time
import pyautogui

try:
    f = open('data\settings.txt')
    audio_fl = bool(int(f.read().split('\n')[0].split(' = ')[1]))
    music_fl = bool(int(f.read().split('\n')[1].split(' = ')[1]))
    size = open(f.read().split('\n')[2].split(' = ')[1])
    f.close()
except Exception:
    f = open('data\settings.txt', 'w')
    f.write('audio_fl = 1\nmusic_fl = 1\nsize = FullHD')
    f.close()
    audio_fl = 1
    music_fl = 1
    size = 'FullHD'


def beautifull_write(x, y, width, hight,
                     text,
                     font='14690.ttf', size=70,
                     k=0.4,
                     t=0.5,
                     text_collor=(255, 255, 255), font_collor=None,
                     shade=False, shade_collor=()):
    f = pygame.font.Font('data\\font\{}'.format(font), size)
    x *= k
    y *= k
    x_start = x
    size *= k
    y_max = f.render('А', 1, text_collor).get_rect()[3]
    x_max = f.render('а', 1, text_collor).get_rect()[2]
    if shade:
        pass
    else:
        try:
            text = text.split()
            for i1 in range(len(text)):
                for i2 in text[i1]:
                    sim = f.render(i2, 1, text_collor, font_collor)
                    print(i2)
                    screen.blit(sim, (x, y))
                    x += x_max
                    pygame.display.flip()
                    time.sleep(t)
                print(len(text), '>', i1 + 1)
                print(x + x_max * (len(text[i1 + 1]) + 1), '>=', width)
                if (len(text) > i1 + 1) and (x + x_max * (len(text[i1 + 1]) + 1) >= width):
                    x = x_start
                    print('y_max = {}'.format(y_max))
                    y += y_max
                else:
                    sim = f.render(' ', 1, text_collor, font_collor)
                    print(' ')
                    screen.blit(sim, (x, y))
                    x += x_max
                    pygame.display.flip()
                time.sleep(t)
        except Exception as a:
            print(a)


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
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# создание окна 720 720
# screen = pygame.display.set_mode((720, 720))

screen.fill((0, 0, 0))
pygame.display.flip()
# рисование меню
# menu = load_image("game\{}.png".format(open('data\progress.txt').read()))
# screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
pygame.display.flip()

file_name = f'game\\{size}\\_'
# Игровой цикл
running = True
while running:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                file_name += '\\1'
            if event.key == pygame.K_2:
                file_name += '\\2'
            if event.key == pygame.K_3:
                file_name += '\\3'
            if event.key == pygame.K_4:
                file_name += '\\4'
            if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                file_name += '\\_'
    menu = load_image(f"{file_name}\\img.png")
    menu = pygame.transform.scale(menu, (x, y))
    screen.blit(menu, (0, 0))

    # текст
    try:
        beautifull_write(200, 200, 500, 200, open(f"data\\{file_name}\\text.txt", 'r').read())
    except Exception:
        pass
    # Выбор
    try:
        beautifull_write(200, 200, 500, 200, open(f"data\\{file_name}\\v.txt", 'r').read())
    except Exception:
        pass
    pygame.display.flip()
pygame.quit()
