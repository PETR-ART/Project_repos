import sys
import pygame
import os


# для загрузки файлов
def load_image(name, colorkey=None):
    # Полный путь к файлу
    fullname = os.path.join('data/images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        pygame.quit()

    image = pygame.image.load(fullname)

    # для прозрачности изображения
    if colorkey is not None:
        image = image.convert()
        # если ключ -1, то убираем цвет который в левом нижнем углу
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    # отправляем изображение
    return image


pygame.init()

font = pygame.font.Font(None, 38)
font1 = pygame.font.Font(None, 60)

window_size = window_width, window_height = 800, 600
window = pygame.display.set_mode(window_size)
button_width, button_height = 100, 40
button_x = window_width // 2 - button_width // 2
button_start_y = window_height // 2 - button_height // 2 - 80
button_rating_y = window_height // 2 - button_height // 2
button_exit_y = window_height // 2 - button_height // 2 + 80

log_width = window_width // 2
log_height = window_height - (window_height - 100)
input_width = window_width * 0.2
input1_width = (window_width - input_width) // 2
input_height = window_height * 0.4

start_image = pygame.transform.scale(load_image('start_image.jpg'), window_size)
first_image = pygame.transform.scale(load_image('first_image.webp'), window_size)
America_image = pygame.transform.scale(load_image('America.jpg'), window_size)
Europe_image = pygame.transform.scale(load_image('Europe.jpg'), window_size)
Asia_image = pygame.transform.scale(load_image('Asia.jpg'), window_size)
Player_image = pygame.transform.scale(load_image('player.png'), window_size)


def Menu():
    pygame.display.set_caption("Меню")
    window.blit(start_image, (0, 0))

    pygame.draw.rect(window, 'brown', (button_x, button_start_y, button_width, button_height))
    pygame.draw.rect(window, 'brown', (button_x, button_rating_y, button_width, button_height))
    pygame.draw.rect(window, 'brown', (button_x, button_exit_y, button_width, button_height))

    font = pygame.font.Font(None, 38)
    text_start = font.render("Старт", True, 'white')
    text_rating = font.render("Рейтинг", True, 'white')
    text_exit = font.render("Выход", True, 'white')

    window.blit(text_start, (button_x + button_width // 2 - text_start.get_width() // 2,
                             button_start_y + button_height // 2 - text_start.get_height() // 2))
    window.blit(text_rating, (button_x + button_width // 2 - text_rating.get_width() // 2,
                              button_rating_y + button_height // 2 - text_rating.get_height() // 2))
    window.blit(text_exit, (button_x + button_width // 2 - text_exit.get_width() // 2,
                            button_exit_y + button_height // 2 - text_exit.get_height() // 2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print((mouse_x, mouse_y))
                if button_x <= mouse_x <= button_x + button_width:
                    if button_start_y <= mouse_y <= button_start_y + button_height:
                        Start()
                    elif button_rating_y <= mouse_y <= button_rating_y + button_height:
                        Rating()
                    elif button_exit_y <= mouse_y <= button_exit_y + button_height:
                        pygame.quit()
                        sys.exit()

        pygame.display.flip()


def Start():
    pygame.display.set_caption("Инициализация")

    window.blit(first_image, (0, 0))

    text_log = font.render('Введите логин', True, 'Brown')
    window.blit(text_log, (log_width - 90, log_height - 10, log_width, log_height))

    pygame.draw.rect(window, 'brown', (input_width, input_height,  window_width - input1_width, 100))

    pygame.draw.rect(window, 'brown', (button_x - 40, button_exit_y - 5, button_width + 80, button_height + 5))
    text_continue = font.render("Продолжить", True, 'white')
    window.blit(text_continue, (button_x + button_width // 2 - text_continue.get_width() // 2,
                                    button_exit_y + button_height // 2 - text_continue.get_height() // 2))

    pygame.draw.rect(window, 'brown', (button_x - 40, button_exit_y + 65, button_width + 80, button_height + 5))
    text_back = font.render("Назад", True, 'white')
    window.blit(text_back, (button_x + button_width // 2 - text_back.get_width() // 2,
                            button_exit_y + button_height // 2 - text_back.get_height() // 2 + 70))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print((mouse_x, mouse_y))
                if 310 <= mouse_x <= 490 and 355 <= mouse_y <= 400:
                    Check_setting()
                if 310 <= mouse_x <= 490 and 425 <= mouse_y <= 470:
                    Menu()

        pygame.display.flip()


def Rating():
    pygame.display.set_caption("Рейтинг")

    window.blit(first_image, (0, 0))

    text_check = font.render('Рекорды', True, 'Brown')
    window.blit(text_check, (350, 60, 400, 80))

    pygame.draw.rect(window, 'brown', (button_x - 40, button_exit_y + 125, button_width + 80, button_height + 5))
    text_back = font.render("Назад", True, 'white')
    window.blit(text_back, (button_x + button_width // 2 - text_back.get_width() // 2,
                            button_exit_y + button_height // 2 - text_back.get_height() // 2 + 130))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print((mouse_x, mouse_y))
                if 310 <= mouse_x <= 490 and 485 <= mouse_y <= 530:
                    Menu()
        pygame.display.flip()


def Check_setting():
    # Флаги Настроек Стран
    Europe = False
    America = False
    Asia = False
    # Флаги Цвета Кнопок У Стран
    Europe_color = 'brown'
    America_color = 'brown'
    Asia_color = 'brown'
    # Флаги Настроек Режима
    Flags = False
    Countries = False
    Facts = False
    # Флаги Цвета Кнопок У Настроек Режима
    Flags_color = 'brown'
    Countries_color = 'brown'
    Facts_color = 'brown'
    # Отображение заголовка
    pygame.display.set_caption("Выбор Режима")

    window.blit(first_image, (0, 0))

    # Отображение текста "Выберите режим"
    text_check = font.render('Выберите режим', True, 'Brown')
    window.blit(text_check, (310, 60, 400, 80))

    while True:
        # Отображение кнопок
        pygame.draw.rect(window, Europe_color,
                         (button_x - 250, button_exit_y - 220, button_width + 80, button_height + 5))
        text_europe = font.render("Европа", True, 'white')
        window.blit(text_europe, (button_x + button_width // 2 - text_europe.get_width() // 2 - 210,
                                  button_exit_y + button_height // 2 - text_europe.get_height() // 2 - 215))

        pygame.draw.rect(window, America_color,
                         (button_x - 50, button_exit_y - 220, button_width + 80, button_height + 5))
        text_europe = font.render("Америка", True, 'white')
        window.blit(text_europe, (button_x + button_width // 2 - text_europe.get_width() // 2 - 10,
                                  button_exit_y + button_height // 2 - text_europe.get_height() // 2 - 215))

        pygame.draw.rect(window, Asia_color,
                         (button_x + 150, button_exit_y - 220, button_width + 80, button_height + 5))
        text_europe = font.render("Азия", True, 'white')
        window.blit(text_europe, (button_x + button_width // 2 - text_europe.get_width() // 2 + 190,
                                  button_exit_y + button_height // 2 - text_europe.get_height() // 2 - 215))

        pygame.draw.rect(window, Flags_color,
                         (button_x - 250, button_exit_y - 120, button_width + 80, button_height + 5))
        text_europe = font.render("Флаги", True, 'white')
        window.blit(text_europe, (button_x + button_width // 2 - text_europe.get_width() // 2 - 210,
                                  button_exit_y + button_height // 2 - text_europe.get_height() // 2 - 118))

        pygame.draw.rect(window, Countries_color,
                         (button_x - 50, button_exit_y - 120, button_width + 80, button_height + 5))
        text_europe = font.render("Страны", True, 'white')
        window.blit(text_europe, (button_x + button_width // 2 - text_europe.get_width() // 2 - 10,
                                  button_exit_y + button_height // 2 - text_europe.get_height() // 2 - 118))

        pygame.draw.rect(window, Facts_color,
                         (button_x + 150, button_exit_y - 120, button_width + 80, button_height + 5))
        text_europe = font.render("Факты", True, 'white')
        window.blit(text_europe, (button_x + button_width // 2 - text_europe.get_width() // 2 + 190,
                                  button_exit_y + button_height // 2 - text_europe.get_height() // 2 - 118))

        pygame.draw.rect(window, 'brown', (button_x - 40, button_exit_y + 55, button_width + 80, button_height + 5))
        text_continue = font.render("Продолжить", True, 'white')
        window.blit(text_continue, (button_x + button_width // 2 - text_continue.get_width() // 2,
                                    button_exit_y + button_height // 2 - text_continue.get_height() // 2 + 60))

        pygame.draw.rect(window, 'brown', (button_x - 40, button_exit_y + 125, button_width + 80, button_height + 5))
        text_back = font.render("Назад", True, 'white')
        window.blit(text_back, (button_x + button_width // 2 - text_back.get_width() // 2,
                                button_exit_y + button_height // 2 - text_back.get_height() // 2 + 130))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print((mouse_x, mouse_y))
                if 310 <= mouse_x <= 490 and 485 <= mouse_y <= 530:
                    Start()

                if 100 <= mouse_x <= 280 and 140 <= mouse_y <= 180:
                    if Europe:
                        Europe_color = 'brown'
                        Europe = False
                    else:
                        Europe_color = 'red'
                        Europe = True

                if 300 <= mouse_x <= 480 and 140 <= mouse_y <= 180:
                    if America:
                        America_color = 'brown'
                        America = False
                    else:
                        America_color = 'red'
                        America = True

                if 500 <= mouse_x <= 680 and 140 <= mouse_y <= 180:
                    if Asia:
                        Asia_color = 'brown'
                        Asia = False
                    else:
                        Asia_color = 'red'
                        Asia = True

                if 100 <= mouse_x <= 280 and 240 <= mouse_y <= 280:
                    if Flags:
                        Flags_color = 'brown'
                        Flags = False
                    else:
                        Flags_color = 'red'
                        Flags = True

                if 300 <= mouse_x <= 480 and 240 <= mouse_y <= 280:
                    if Countries:
                        Countries_color = 'brown'
                        Countries = False
                    else:
                        Countries_color = 'red'
                        Countries = True

                if 500 <= mouse_x <= 680 and 240 <= mouse_y <= 280:
                    if Facts:
                        Facts_color = 'brown'
                        Facts = False
                    else:
                        Facts_color = 'red'
                        Facts = True

                if 310 <= mouse_x <= 490 and 415 <= mouse_y <= 460:
                    if America_color == 'red' and Asia_color == 'brown' and Europe_color == 'brown':
                        tip1 = 'America'
                    elif Asia_color == 'red' and America_color == 'brown' and Europe_color == 'brown':
                        tip1 = 'Asia'
                    elif Europe_color == 'red' and America_color == 'brown' and Asia_color == 'brown':
                        tip1 = 'Europe'
                    else:
                        tip1 = ''
                    if Flags_color == 'red' and Facts_color == 'brown' and Countries_color == 'brown' and tip1 != '':
                        tip2 = 'Flags'
                        Game(0, 0, tip1, tip2)
                    elif Facts_color == 'red' and Flags_color == 'brown' and Countries_color == 'brown' and tip1 != '':
                        tip2 = 'Facts'
                        Game(0, 0, tip1, tip2)
                    elif Countries_color == 'red' and Flags_color == 'brown' and Facts_color == 'brown' and tip1 != '':
                        tip2 = 'Countries'
                        Game(0, 0, tip1, tip2)
                    else:
                        print('ОШИБКА')
        pygame.display.flip()


def Game(player_x, player_y, tip1, tip2):
    print(tip1, tip2)
    cell_size = 40
    line_width = 1
    scaled_image = pygame.transform.scale(Player_image, (cell_size, cell_size))
    pygame.display.set_caption('Игра')
    clock = pygame.time.Clock()

    counter, text = 10, '10'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(mouse_x, mouse_y)
            if event.type == pygame.USEREVENT:
                counter -= 1
                if counter > 0:
                    text = str(counter).rjust(3)
                else:
                    end(res_game='Game over')

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player_y -= cell_size
                    if player_y < 0:
                        player_y += cell_size
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player_y += cell_size
                    if player_y >= window_height:
                        player_y -= cell_size
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player_x -= cell_size
                    if player_x < 0:
                        player_x += cell_size
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player_x += cell_size
                    if player_x >= window_width:
                        player_x -= cell_size

        window.fill((255, 255, 255))
        pygame.draw.rect(window, 'red', (760, 560, 800, 600))
        for y_ in range(0, window_height, cell_size):
            for x_ in range(0, window_width, cell_size):
                pygame.draw.rect(window, pygame.Color('black'),
                                 (x_, y_, cell_size, cell_size), line_width)
        if (player_x >= 0) and (player_x < window_width) and (player_y >= 0) and (player_y < window_height):
            window.blit(scaled_image, (player_x, player_y))

        window.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        pygame.display.flip()
        clock.tick(30)

        if player_x == 760 and player_y == 560:
            end(res_game='Victory')


def end(res_game):
    pygame.display.set_caption('Конец игры')
    window.blit(first_image, (0, 0))
    text_res = font1.render(res_game, True, 'Brown')
    window.blit(text_res, (320, 100))
    text_go = font.render('Для продолжения нажмите на любую клавишу', True, 'Brown')
    window.blit(text_go, (70, 150))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                Menu()
        pygame.display.flip()


# Будующие спрайты
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

running = True
Menu()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # В процессе
    tiles_group.draw(window)
    player_group.draw(window)
    pygame.display.flip()
