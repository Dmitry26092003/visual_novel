import pygame
import os
from PIL import Image
from ctypes  import *
import time
audio_fl = bool(int(open('data\settings.txt').read().split('\n')[0].split(' = ')[1]))
music_fl = bool(int(open('data\settings.txt').read().split('\n')[1].split(' = ')[1]))
size = open('data\settings.txt').read().split('\n')[2].split(' = ')[1]
print(audio_fl, music_fl)
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


def exit():
    global audio_fl
    global music_fl
    global menu_music
    fl = True
    screen.blit(exit_image, ((x-exit_image.get_width())//2, (y-exit_image.get_height())//2))
    while fl:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                xx, yy = pygame.mouse.get_pos()
                xx = xx - (x-exit_image.get_width())//2
                yy = yy - (y-exit_image.get_height())//2
                if 20 < xx < 100 and 80 < yy < 120:
                    if audio_fl:
                        click_sound.play()
                    time.sleep(1)
                    return True
                elif 120 < xx < 180 and 100 < yy < 120:
                    if audio_fl:
                        click_sound.play()
                    return False
        pygame.display.flip()
                


def settings():
    global audio_fl
    global music_fl
    global menu_music
    fl = True
    menu = load_image("menu\{}\settings\main.png".format(size))
    screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
    while fl:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                xx, yy = pygame.mouse.get_pos()
                xx = xx - (x-menu.get_width())//2
                yy = yy - (y-menu.get_height())//2
                if 25 < xx < 280:
                    if 340 < yy < 415:
                        if audio_fl:
                            click_sound.play()                    
                        fl = False
                    #elif 
                if 340 < xx < 401:
                    if 210 < yy < 238:
                        if audio_fl:
                            click_sound.play()
                        audio_fl = not audio_fl
                        open('data\settings.txt', 'w').write('audio_fl = {}\nmusic_fl = {}'.format(str(int(audio_fl)), str(int(music_fl))))
                    elif 280 < yy < 308:
                        if audio_fl:
                            click_sound.play()
                        if not music_fl:
                            menu_music = pygame.mixer.Sound(os.path.join('data\music\menu.wav'))
                            menu_music.play(-1)
                        else:
                            menu_music.stop()                            
                        music_fl = not music_fl
                        open('data\settings.txt', 'w').write('audio_fl = {}\nmusic_fl = {}'.format(str(int(audio_fl)), str(int(music_fl))))                        
            if event.type == pygame.MOUSEMOTION:
                xx, yy = pygame.mouse.get_pos()
                xx = xx - (x-menu.get_width())//2
                yy = yy - (y-menu.get_height())//2
                if 25 < xx < 280 and 340 < yy < 415:
                    menu = load_image("menu\{}\settings\main_exit.png".format(size))
                else:
                    menu = load_image("menu\{}\settings\main.png".format(size))
        if audio_fl:
            audio_bt = load_image("menu\{}\settings\on.png".format(size))
        else:
            audio_bt = load_image("menu\{}\settings\off.png".format(size))
        if music_fl:
            music_bt = load_image("menu\{}\settings\on.png".format(size))
        else:
            music_bt = load_image("menu\{}\settings\off.png".format(size))
        menu.transform(x, y)
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
exit_image = load_image("menu\quit.png")
if music_fl:
    menu_music = pygame.mixer.Sound(os.path.join('data\music\menu.wav'))
    menu_music.play(-1)
click_sound = pygame.mixer.Sound(os.path.join('data\music\click.wav'))
screen.fill((0, 0, 0))
pygame.display.flip()
# рисование меню
menu = load_image("menu\{}\start_menu\main_0.png".format(size))
menu.transform(x, y)
screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
pygame.display.flip()


# Игровой цикл
running = True
while running:
    pygame.display.flip()    
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
                    if audio_fl:
                        click_sound.play()
                    
                    pygame.display.flip()
                    e = exit()
                    if e:
                        running = False
                        pygame.display.flip()
                    
                elif 350 < yy < 430:
                    if audio_fl:
                        click_sound.play()                        
                    settings()
                    menu = load_image("menu\{}\start_menu\main_0.png".format(size))
                    menu.transform(x, y)                    
                    screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))                    
                    pygame.display.flip()                    
                elif 170 < yy < 245:
                    if audio_fl:
                        click_sound.play()                        
                    os.system('python game.py')
                    running = False
                elif 255 < yy < 330:
                    if audio_fl:
                        click_sound.play()                        
                    open('data\saves\progress.txt', 'w').write('1')
                    os.system('python game.py')
                    running = False                  
        if event.type == pygame.MOUSEMOTION:
            xx, yy = pygame.mouse.get_pos()
            xx = xx - (x-menu.get_width())//2
            yy = yy - (y-menu.get_height())//2
            if 25 < xx < 425:
                if 170 < yy < 245:
                    menu = load_image("menu\{}\start_menu\main_load_game.png".format(size))
                    menu.transform(x, y)                    
                    screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
                    pygame.display.flip()
                elif 255 < yy < 330:
                    menu = load_image("menu\{}\start_menu\main_new_game.png".format(size))
                    menu.transform(x, y)                    
                    screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
                    pygame.display.flip()
                elif 350 < yy < 430:
                    menu = load_image("menu\{}\start_menu\main_settings.png".format(size))
                    menu.transform(x, y)                    
                    screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
                    pygame.display.flip()
                elif 440 < yy < 515:
                    menu = load_image("menu\{}\start_menu\main_info.png".format(size))
                    menu.transform(x, y)                    
                    screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
                    pygame.display.flip()
                elif 520 < yy < 595:
                    menu = load_image("menu\{}\start_menu\main_exit.png".format(size))
                    menu.transform(x, y)                    
                    screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
                    pygame.display.flip()
                else:
                    menu = load_image("menu\{}\start_menu\main_0.png".format(size))
                    menu.transform(x, y)                    
                    screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
                    pygame.display.flip()
            else:
                menu = load_image("menu\{}\start_menu\main_0.png".format(size))
                menu.transform(x, y)                
                screen.blit(menu, ((x-menu.get_width())//2, (y-menu.get_height())//2))
                pygame.display.flip()                
    # обновление экрана
    pygame.display.flip()
pygame.quit()
