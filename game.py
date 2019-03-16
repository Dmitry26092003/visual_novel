import datetime
import os
import time
from ctypes import *

import pygame

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


def game(audio_fl, music_fl, size, file_name=''):
    def beautifull_write(x, y, width, hight,
                         text,
                         font='14690.ttf', size=35,
                         k=1,
                         t=0.06,
                         text_collor=(255, 255, 255), font_collor=None,
                         shade=False, shade_collor=()):
        # tap_music = pygame.mixer.Sound(os.path.join('data\\music\\typewriter.wav'))
        # tap_music.play(-1)
        f = pygame.font.Font('data\\font\{}'.format(font), size)
        x *= k
        y *= k
        x_start = x
        size *= k
        y_max = f.render('А', 1, text_collor).get_rect()[3]
        if shade:
            pass
        else:
            try:
                for text1 in text.split('\n'):
                    text = text1.split()
                    for i1 in range(len(text)):
                        for i2 in text[i1]:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                                        t = 0
                                    if event.key == pygame.K_ESCAPE:
                                        raise SystemExit
                            sim = f.render(i2, 1, text_collor, font_collor)
                            screen.blit(sim, (x, y))
                            x += sim.get_rect()[2]
                            pygame.display.flip()
                            time.sleep(t)
                        if (len(text) > i1 + 1) and (
                                x + sim.get_rect()[2] * (len(text[i1 + 1]) + 1) >= width):
                            x = x_start
                            y += y_max
                        else:
                            sim = f.render('   ', 1, text_collor, font_collor)
                            screen.blit(sim, (x, y))
                            x += sim.get_rect()[2]
                            pygame.display.flip()
                        time.sleep(t)
                    x = x_start
                    y += y_max
            except Exception as a:
                print(a)
        # tap_music.stop()

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

    s = f'game\\{size}\\_'

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

    # Игровой цикл
    running = True
    game_fl = True
    while running:
        # обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if '1' in os.listdir(path=f"data\\{s + file_name}"):
                        file_name += '\\1'
                        game_fl = True
                if event.key == pygame.K_2:
                    if '2' in os.listdir(path=f"data\\{s + file_name}"):
                        file_name += '\\2'
                        game_fl = True
                if event.key == pygame.K_3:
                    if '3' in os.listdir(path=f"data\\{s + file_name}"):
                        file_name += '\\3'
                        game_fl = True
                if event.key == pygame.K_4:
                    if '4' in os.listdir(path=f"data\\{s + file_name}"):
                        file_name += '\\4'
                        game_fl = True
                if event.key == pygame.K_s:  # Сохранение
                    with open(
                            f"data\\saves\\{'.'.join(str(datetime.datetime.now()).split(':'))}.txt",
                            'w') as save:
                        save.write(file_name)
                if event.key == pygame.K_l:  # Загрзка сохранения
                    pass
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                    if '_' in os.listdir(path=f"data\\{s + file_name}"):
                        file_name += '\\_'
                        game_fl = True
        if game_fl:
            try:
                game_fl = False
                menu = load_image(f"{s + file_name}\\img.png")
                menu = pygame.transform.scale(menu, (x, y))
                screen.blit(menu, (0, 0))
                # текст
                try:
                    tex_bar = load_image(f"game\\{size}\\text_bar.png")
                    tex_bar = pygame.transform.scale(tex_bar,
                                                     (int(1820 * x / 1920), int(150 * y / 1080)))
                    screen.blit(tex_bar, (int(50 * x / 1920), int(900 * y / 1080)))
                    beautifull_write(int(55 * x / 1920), int(910 * y / 1080), int(1720 * x / 1920),
                                     int(150 * y / 1080),
                                     open(f"data\\{s + file_name}\\text.txt", 'r').read(), size=35)
                except Exception as a:
                    print(a)
                    time.sleep(0.5)
                    file_name += '\\_'
                    game_fl = True
                k = (x // 1280)
                # Выбор
                try:
                    f = open(f"data\\{s + file_name}\\1.txt", 'r').read()
                    tex_bar_1 = load_image(f"game\\{size}\\text_bar_2.png")
                    tex_bar_1 = pygame.transform.scale(tex_bar_1,
                                                       (int(620 * x / 1920), int(50 * y / 1080)))
                    screen.blit(tex_bar_1, (int(50 * x / 1920), int(845 * y / 1080)))
                    beautifull_write(int(55 * x / 1920), int(850 * y / 1080), int(600 * x / 1920),
                                     int(45 * y / 1080),
                                     f,
                                     text_collor=(255, 0, 0), size=30)
                except Exception as a:
                    pass
                try:
                    f = open(f"data\\{s + file_name}\\2.txt", 'r').read()

                    tex_bar_2 = load_image(f"game\\{size}\\text_bar_2.png")
                    tex_bar_2 = pygame.transform.scale(tex_bar_2,
                                                       (int(620 * x / 1920), int(50 * y / 1080)))
                    screen.blit(tex_bar_2, (int(50 * x / 1920), int(790 * y / 1080)))
                    beautifull_write(int(55 * x / 1920), int(795 * y / 1080), int(600 * x / 1920),
                                     int(45 * y / 1080),
                                     f,
                                     text_collor=(255, 0, 0), size=30)
                except Exception as a:
                    pass
                try:
                    f = open(f"data\\{s + file_name}\\3.txt", 'r').read()
                    tex_bar_3 = load_image(f"game\\{size}\\text_bar_2.png")
                    tex_bar_3 = pygame.transform.scale(tex_bar_3,
                                                       (int(620 * x / 1920), int(50 * y / 1080)))
                    screen.blit(tex_bar_3, (int(50 * x / 1920), int(735 * y / 1080)))
                    beautifull_write(int(55 * x / 1920), int(740 * y / 1080), int(600 * x / 1920),
                                     int(45 * y / 1080),
                                     f,
                                     text_collor=(255, 0, 0), size=30)
                except Exception as a:
                    pass
                try:
                    f = open(f"data\\{s + file_name}\\4.txt", 'r').read()
                    tex_bar_4 = load_image(f"game\\{size}\\text_bar_2.png")
                    tex_bar_4 = pygame.transform.scale(tex_bar_4,
                                                       (int(620 * x / 1920), int(50 * y / 1080)))
                    screen.blit(tex_bar_4, (int(50 * x / 1920), int(680 * y / 1080)))
                    beautifull_write(int(55 * x / 1920), int(685 * y / 1080), int(600 * x / 1920),
                                     int(45 * y / 1080),
                                     f,
                                     text_collor=(255, 0, 0), size=30)
                except Exception as a:
                    pass
                pygame.display.flip()
            except SystemExit:
                running = False

    with open(
            f"data\\saves\\{'.'.join(str(datetime.datetime.now()).split(':'))}.txt", 'w') as save:
        save.write(file_name)


if __name__ == '__main__':
    game(audio_fl=audio_fl, music_fl=music_fl, size=size)
    pygame.quit()
