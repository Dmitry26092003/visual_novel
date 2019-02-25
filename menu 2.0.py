import pygame
import os
from PIL import Image
from ctypes  import *
import time
import pyautogui

# Размеры экрана
x = windll.user32.GetSystemMetrics(0)
y = windll.user32.GetSystemMetrics(1)

k = y/1080

buttons_setting_text = ['Size',
                        'Audio',
                        'Music',
                        'Font',
                        'Exit']
buttons_setting_pressed = [0, 0, 0, 0, 0]
# загружаем настройки
try:
    f = open('data\settings.txt')
    audio_fl = bool(int(f.read().split('\n')[0].split(' = ')[1]))
    music_fl = bool(int(f.read().split('\n')[1].split(' = ')[1]))
    size = open(f.read().split('\n')[2].split(' = ')[1])
    font_font = open(f.read().split('\n')[3].split(' = ')[1])
    font_size = open(f.read().split('\n')[4].split(' = ')[1])    
    f.close()
    font = [font_font, int(font_size*k)]
except Exception:
    f = open('data\settings.txt', 'w')    
    f.write('audio_fl = 1\nmusic_fl = 1\nsize = FullHD\nfont_font = "14690.ttf"\nfont_size = 36')
    f.close()    
    audio_fl = 1
    music_fl = 1
    size = 'FullHD'
    font = ['14690.ttf', int(36*k)]
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

# функция выхода
def exit():
    global audio_fl
    global music_fl
    global menu_music
    global x, y    
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
                
# кнопка
def button(x, y, text, species):
    global size
    global k
    global t
    f = pygame.font.Font('data\\font\{}'.format(font[0]), font[1])
    xx, yy = pygame.mouse.get_pos()
    if species:
        bt = load_image("menu\{}\main_button_green.png".format(size))
        bt = pygame.transform.scale(bt, (int(578*k), int(92*k)))
    else:
        bt = load_image("menu\{}\main_button.png".format(size))
        bt = pygame.transform.scale(bt, (int(578*k), int(92*k)))
    t = f.render(text, 1, (252, 226, 204))
    screen.blit(bt, (x, y))
    screen.blit(t, (x + int(578 * k - t.get_rect()[2]) // 2, y + int(92 * k - t.get_rect()[3]) // 2))
    

def settings():
    global audio_fl
    global music_fl
    global menu_music
    global x, y
    global size
    global click_sound
    fl = True
    size_fl = False
    menu = load_image("menu\{}\main.png".format(size))
    screen.blit(menu, (0, 0))
    while fl:
        screen.blit(menu, (0, 0))
        for i in range(len(buttons_setting_text)):           
            button(25*k, (150+102*i)*k, buttons_setting_text[i], buttons_setting_pressed[i])
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                xx, yy = pygame.mouse.get_pos()
                if int(25*k) < xx < int(578*k):
                    if 150*k < yy < 242*k:
                        buttons_setting_pressed[0] = 1
                        if 1 in event.buttons:
                            if audio_fl:
                                click_sound.play()
                    else:
                        buttons_setting_pressed[0] = 0
                        
            '''
                xx, yy = pygame.mouse.get_pos()
                if 25*pix_new_x < xx < 280*pix_new_x:
                    if 340*pix_new_y < yy < 415*pix_new_y:
                        if audio_fl:
                            click_sound.play()
                        fl = False
                        open('data\settings.txt', 'w').write('audio_fl = {}\nmusic_fl = {}\nsize = {}'.format(str(int(audio_fl)), str(int(music_fl)), size))
                        return 0
                    elif 120*pix_new_y < yy < 185*pix_new_y:
                        if audio_fl:
                            click_sound.play()                        
                        size_fl = not size_fl

                if 340*pix_new_x < xx < 401*pix_new_x:
                    if 210*pix_new_y < yy < 238*pix_new_y:
                        if audio_fl:
                            click_sound.play()
                        audio_fl = not audio_fl
                        break
                    elif 280*pix_new_y < yy < 308*pix_new_y:
                        if audio_fl:
                            click_sound.play()
                        if not music_fl:
                            menu_music = pygame.mixer.Sound(os.path.join('data\music\menu.wav'))
                            menu_music.play(-1)
                        else:
                            menu_music.stop()                            
                        music_fl = not music_fl
                        break
            if event.type == pygame.MOUSEMOTION:
                xx, yy = pygame.mouse.get_pos()
                if 25*pix_new_x < xx < 280*pix_new_x:
                    if 340*pix_new_y < yy < 415*pix_new_y:
                        menu = load_image("menu\{}\settings\main_exit_green.png".format(size))
                        menu = pygame.transform.scale(menu, (x, y))
                        screen.blit(menu, (0, 0))                            
                        pygame.display.update((17*pix_new_x, 112*pix_new_y),(312*pix_new_x, 305*pix_new_y))
                        
                    elif 120*pix_new_y < yy < 185*pix_new_y:
                        menu = load_image("menu\{}\settings\main_size_green.png".format(size))
                        menu = pygame.transform.scale(menu, (x, y))
                        screen.blit(menu, (0, 0))                            
                        pygame.display.update((17*pix_new_x, 112*pix_new_y),(312*pix_new_x, 305*pix_new_y))
                        
                    else:
                        menu = load_image("menu\{}\settings\main.png".format(size))
                        menu = pygame.transform.scale(menu, (x, y))
                        screen.blit(menu, (0, 0))                            
                        pygame.display.update((17*pix_new_x, 112*pix_new_y),(312*pix_new_x, 305*pix_new_y))
                        
                else:
                    menu = load_image("menu\{}\settings\main.png".format(size))
                    menu = pygame.transform.scale(menu, (x, y))
                    screen.blit(menu, (0, 0))                            
                    pygame.display.update((17*pix_new_x, 112*pix_new_y),(312*pix_new_x, 305*pix_new_y))
                    
        if audio_fl:
            audio_bt = load_image("menu\{}\settings\on.png".format(size))
        else:
            audio_bt = load_image("menu\{}\settings\off.png".format(size))
        if music_fl:
            music_bt = load_image("menu\{}\settings\on.png".format(size))
        else:
            music_bt = load_image("menu\{}\settings\off.png".format(size))
        menu = pygame.transform.scale(menu, (x, y))
        screen.blit(menu, (0, 0))
        screen.blit(audio_bt, (340*pix_new_x, 210*pix_new_y))
        screen.blit(music_bt, (340*pix_new_x, 280*pix_new_y))
        pygame.display.flip()

'''

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
pix_new_x = x/1280
pix_new_y = y/720
print(pix_new_x, pix_new_y)
menu = pygame.transform.scale(menu, (x, y))
screen.blit(menu, (0, 0))
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
            if 25*pix_new_x < xx < 425*pix_new_x:
                if 520*pix_new_y < yy < 595*pix_new_y:
                    if audio_fl:
                        click_sound.play()
                    
                    pygame.display.flip()
                    e = exit()
                    if e:
                        running = False
                        pygame.display.flip()
                    
                elif 350*pix_new_y < yy < 430*pix_new_y:
                    if audio_fl:
                        click_sound.play()                        
                    settings()
                    menu = load_image("menu\{}\start_menu\main_0.png".format(size))
                    menu = pygame.transform.scale(menu, (x, y))               
                    screen.blit(menu, (0, 0))                    
                    pygame.display.flip()                    
                elif 170*pix_new_y < yy < 245*pix_new_y:
                    if audio_fl:
                        click_sound.play()                        
                    os.system('python game.py')
                    running = False
                elif 255*pix_new_y < yy < 330*pix_new_y:
                    if audio_fl:
                        click_sound.play()                        
                    open('data\saves\progress.txt', 'w').write('1')
                    os.system('python game.py')
                    running = False                  
        if event.type == pygame.MOUSEMOTION:
            xx, yy = pygame.mouse.get_pos()
            if 25*pix_new_x < xx < 425*pix_new_x:
                if 170*pix_new_y < yy < 245*pix_new_y:
                    menu = load_image("menu\{}\start_menu\main_load_game_green.png".format(size))
                    menu = pygame.transform.scale(menu, (x, y))
                    screen.blit(menu, (0, 0))                            
                    pygame.display.update((36*pix_new_x, 250*pix_new_y),(598*pix_new_x, 641*pix_new_y)) 
                elif 255*pix_new_y < yy < 330*pix_new_y:
                    menu = load_image("menu\{}\start_menu\main_new_game_green.png".format(size))
                    menu = pygame.transform.scale(menu, (x, y))
                    screen.blit(menu, (0, 0))
                    pygame.display.update((36*pix_new_x, 250*pix_new_y),(598*pix_new_x, 641*pix_new_y)) 
                elif 350*pix_new_y < yy < 430*pix_new_y:
                    menu = load_image("menu\{}\start_menu\main_settings_green.png".format(size))
                    menu = pygame.transform.scale(menu, (x, y))                
                    screen.blit(menu, (0, 0))
                    pygame.display.update((36*pix_new_x, 250*pix_new_y),(598*pix_new_x, 641*pix_new_y)) 
                elif 440*pix_new_y < yy < 515*pix_new_y:
                    menu = load_image("menu\{}\start_menu\main_info_green.png".format(size))
                    menu = pygame.transform.scale(menu, (x, y))                 
                    screen.blit(menu, (0, 0))
                    pygame.display.update((36*pix_new_x, 250*pix_new_y),(598*pix_new_x, 641*pix_new_y)) 
                elif 520*pix_new_y < yy < 595*pix_new_y:
                    menu = load_image("menu\{}\start_menu\main_exit_green.png".format(size))
                    menu = pygame.transform.scale(menu, (x, y))                   
                    screen.blit(menu, (0, 0))
                    pygame.display.update((36*pix_new_x, 250*pix_new_y),(598*pix_new_x, 641*pix_new_y)) 
                else:
                    menu = load_image("menu\{}\start_menu\main_0.png".format(size))
                    menu = pygame.transform.scale(menu, (x, y))                 
                    screen.blit(menu, (0, 0))
                    pygame.display.update((36*pix_new_x, 250*pix_new_y),(598*pix_new_x, 641*pix_new_y)) 
            else:
                menu = load_image("menu\{}\start_menu\main_0.png".format(size))
                menu = pygame.transform.scale(menu, (x, y))               
                screen.blit(menu, (0, 0))
                pygame.display.update((36*pix_new_x, 250*pix_new_y),(598*pix_new_x, 641*pix_new_y)) 
    # обновление экрана
    pygame.display.flip()
pygame.quit()
