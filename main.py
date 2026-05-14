import pygame
from modules import stack_visualizer
from modules import queue_visualizer
from modules import linkedlist_visualizer
from modules import bst_visualizer
from modules import sorting_visualizer
from modules import linear_search_visualizer
from modules import heap_visualizer
from modules import pathfinding_visualizer
from modules import graph_visualizer
from modules import dp_visualizer

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont(None, 48)
clock = pygame.time.Clock()

def draw_menu():
    screen.fill((200, 200, 250))

    title = font.render("DSA Explorer", True, (0, 0, 0))
    screen.blit(title, (260, 80))

    buttons = {
        "Stack": pygame.Rect(300, 180, 200, 50),
        "Queue": pygame.Rect(300, 250, 200, 50),
        "Linked List": pygame.Rect(300, 320, 200, 50),
        "BST": pygame.Rect(300, 390, 200, 50),
        "Sorting": pygame.Rect(300, 460, 200, 50),

        "Heap": pygame.Rect(550, 180, 200, 50),
        "Puzzles": pygame.Rect(550, 250, 200, 50),
        "Graphs": pygame.Rect(550, 320, 200, 50),
        "DP": pygame.Rect(550, 390, 200, 50),
    }

    for name, rect in buttons.items():
        pygame.draw.rect(screen, (150, 150, 250), rect)
        text = font.render(name, True, (0, 0, 0))
        screen.blit(text, (rect.x + 20, rect.y + 10))

    pygame.display.flip()
    return buttons


running = True

while running:

    buttons = draw_menu()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            if buttons["Stack"].collidepoint(pos):
                stack_visualizer.run(screen)

            elif buttons["Queue"].collidepoint(pos):
                queue_visualizer.run(screen)

            elif buttons["Linked List"].collidepoint(pos):
                linkedlist_visualizer.run(screen)

            elif buttons["BST"].collidepoint(pos):
                bst_visualizer.run(screen)

            elif buttons["Sorting"].collidepoint(pos):
                sorting_visualizer.run(screen)

            elif buttons["Heap"].collidepoint(pos):
                heap_visualizer.run(screen)

            elif buttons["Puzzles"].collidepoint(pos):
                pathfinding_visualizer.run(screen)

            elif buttons["Graphs"].collidepoint(pos):
                graph_visualizer.run(screen)

            elif buttons["DP"].collidepoint(pos):
                dp_visualizer.run(screen)

    clock.tick(30)

pygame.quit()
