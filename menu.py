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

def settings():
    global audio_fl
    global music_fl
    fl = True
    menu = load_image("menu\settings\main.png")
    screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
    while fl:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                xx, yy = pygame.mouse.get_pos()
                xx = xx - (x-menu.get_width())//2
                yy = yy - (y-menu.get_height())//2
                if 25 < xx < 280 and 340 < yy < 415:
                    fl = False
                    menu = load_image("menu\start_menu\main_0.png")
                    open('settings.txt', 'w').write('audio_fl = {}\nmusic_fl = {}'.format(str(audio_fl), str(music_fl)))
                if 340 < xx < 401:
                    if 210 < yy < 238:
                        audio_fl = not audio_fl
                    if 280 < yy < 308:
                        music_fl = not music_fl
            if event.type == pygame.MOUSEMOTION:
                xx, yy = pygame.mouse.get_pos()
                xx = xx - (x-menu.get_width())//2
                yy = yy - (y-menu.get_height())//2
                if 25 < xx < 280 and 340 < yy < 415:
                    menu = load_image("menu\settings\main_exit.png")
                else:
                    menu = load_image("menu\settings\main.png")
        if audio_fl:
            audio_bt = load_image("menu\settings\on.png")
        else:
            audio_bt = load_image("menu\settings\off.png")
        if music_fl:
            music_bt = load_image("menu\settings\on.png")
        else:
            music_bt = load_image("menu\settings\off.png")
        screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
        screen.blit(audio_bt, ((x-menu.get_width())//2 + 340, (y-menu.get_height())//2 + 210))
        screen.blit(music_bt, ((x-menu.get_width())//2 + 340, (y-menu.get_height())//2 + 280))
        pygame.display.flip()

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
menu = load_image("menu\start_menu\main_0.png")
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
            if 25 < xx < 425:
                if 520 < yy < 595:
                    pygame.quit()
                elif 350 < yy < 430:
                    settings()
                elif 170 < yy < 245:
                    os.system('python game.py')
                    pygame.quit()
                elif 255 < yy < 330:
                    open('progress.txt', 'w').write('1')
                    os.system('python game.py')
                    pygame.quit()                    
        if event.type == pygame.MOUSEMOTION:
            xx, yy = pygame.mouse.get_pos()
            xx = xx - (x-menu.get_width())//2
            yy = yy - (y-menu.get_height())//2
            if 25 < xx < 425:
                if 170 < yy < 245:
                    menu = load_image("menu\start_menu\main_load_game.png")
                    screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
                    pygame.display.flip()
                elif 255 < yy < 330:
                    menu = load_image("menu\start_menu\main_new_game.png")
                    screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
                    pygame.display.flip()
                elif 350 < yy < 430:
                    menu = load_image("menu\start_menu\main_settings.png")
                    screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
                    pygame.display.flip()
                elif 440 < yy < 515:
                    menu = load_image("menu\start_menu\main_info.png")
                    screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
                    pygame.display.flip()
                elif 520 < yy < 595:
                    menu = load_image("menu\start_menu\main_exit.png")
                    screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
                    pygame.display.flip()
                else:
                    menu = load_image("menu\start_menu\main_0.png")
                    screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
                    pygame.display.flip()
            else:
                menu = load_image("menu\start_menu\main_0.png")
                screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
                pygame.display.flip()                
    # обновление экрана
    pygame.display.flip()
pygame.quit()