import pygame


def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    pygame.display.flip()

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == '__main__':
    main()
