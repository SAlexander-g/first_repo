import pygame
import sys

#hello
size = width, height = 800, 600
black = 0, 0, 0

green = (0, 255, 0)

thickness = 5

ppi = 3.1415


def drawHead(x, y, screen): 
    #400 300 250
    pygame.draw.circle(screen, green, (x, y), 250, thickness)
    pygame.draw.circle(screen, green, (x - 100, y - 100), 30, thickness)
    pygame.draw.circle(screen, green, (x + 100, y - 100), 30, thickness)

    pygame.draw.line(screen, green, (x, y - 50), (x, y + 80), thickness)

    r = pygame.Rect(x - 160, y - 70, 320, 250)
    #pygame.draw.rect(screen, green, r, 1)
    pygame.draw.arc(screen, green, r, 5/4*ppi, 7/4*ppi, thickness)

def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    game_over = False

    while not game_over:
        # обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Логика работы
        # тут

        # Отрисовка кадра
        screen.fill(black)   # чёрный фон, рисуется первым!

        drawHead(400,300, screen)
        

        # Подтверждение отрисовки и ожидание
        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


if __name__ == '__main__':
    main()
