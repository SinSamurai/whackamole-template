import pygame
import random
import sys

pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

background_color = (144, 238, 144)
line_color = (0, 0, 0)


grid_size_x = 20
grid_size_y = 16
cell_width = screen_width // grid_size_x
cell_height = screen_height // grid_size_y

def draw_grid():
    for row in range(grid_size_y + 1):
        pygame.draw.line(screen, line_color, (0, row * cell_height), (screen_width, row * cell_height))
    for col in range(grid_size_x + 1):
        pygame.draw.line(screen, line_color, (col * cell_width, 0), (col * cell_width, screen_height))


mole_image = pygame.image.load("mole.png")
mole_image = pygame.transform.scale(mole_image, (cell_width, cell_height))


mole_x = 0
mole_y = 0


def move_mole():
    global mole_x, mole_y
    mole_x = random.randrange(0, grid_size_x) * cell_width
    mole_y = random.randrange(0, grid_size_y) * cell_height



while True:

    screen.fill(background_color)

    draw_grid()

    screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if mole_x <= mouse_x <= mole_x + cell_width and mole_y <= mouse_y <= mole_y + cell_height:
                move_mole()

    pygame.display.flip()
