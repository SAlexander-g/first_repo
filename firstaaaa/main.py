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

    vx = 5
    vy = 5
    px = 400
    py = 300

    i = 0

    while not game_over:
        # обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True


        left = x <= 250
        right = x >= 550
        top = y <= 250
        bottom = y >= 350

        if left or right:
            vx = - vx
        if top or bottom:
            vy = - vy

        # Логика работы
        # тут
        px += i * vx
        py += i * vy
        i += 1
        # Отрисовка кадра
        screen.fill(black)   # чёрный фон, рисуется первым!

        drawHead(px,py, screen)
        

        # Подтверждение отрисовки и ожидание
        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


if __name__ == '__main__':
    main()
