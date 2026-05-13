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
pygame.display.set_caption("DSA Explorer")

font = pygame.font.SysFont(None, 48)

clock = pygame.time.Clock()


def draw_menu():

    screen.fill((200, 200, 250))

    title = font.render("DSA Explorer", True, (0, 0, 0))
    title_rect = title.get_rect(center=(WIDTH // 2, 55))

    screen.blit(title, title_rect)

    buttons = {

        # LEFT COLUMN
        "Search": pygame.Rect(100, 130, 260, 55),

        "Stack": pygame.Rect(100, 200, 260, 55),

        "Queue": pygame.Rect(100, 270, 260, 55),

        "Linked List": pygame.Rect(100, 340, 260, 55),

        "BST": pygame.Rect(100, 410, 260, 55),

        # RIGHT COLUMN
        "Heap": pygame.Rect(440, 130, 260, 55),

        "Puzzles": pygame.Rect(440, 200, 260, 55),

        "Graphs": pygame.Rect(440, 270, 260, 55),

        "DP": pygame.Rect(440, 340, 260, 55),

        "Sorting": pygame.Rect(440, 410, 260, 55),
    }

    for name, rect in buttons.items():

        pygame.draw.rect(screen, (150, 150, 250), rect, border_radius=8)

        text = font.render(name, True, (0, 0, 0))

        text_rect = text.get_rect(center=rect.center)

        screen.blit(text, text_rect)

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

            elif buttons["Search"].collidepoint(pos):
                linear_search_visualizer.run(screen)

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