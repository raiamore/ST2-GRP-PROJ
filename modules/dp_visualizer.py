import pygame
import random

WIDTH, HEIGHT = 900, 780

ROWS = 10
COLS = 10

CELL_SIZE = 50

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (100, 220, 100)
BLUE = (100, 180, 255)
RED = (255, 120, 120)
GREY = (200, 200, 200)
YELLOW = (255, 230, 80)

TEXT = (0, 0, 0)


def create_grid():

    grid = []

    for row in range(ROWS):

        current_row = []

        for col in range(COLS):

            # KEEP START AND END OPEN
            if (row, col) == (0, 0) or (row, col) == (ROWS - 1, COLS - 1):

                current_row.append(0)

            elif random.random() < 0.2:

                current_row.append(-1)

            else:

                current_row.append(0)

        grid.append(current_row)

    return grid


def reconstruct_path(dp_grid):

    # NO VALID PATH
    if dp_grid[ROWS - 1][COLS - 1] <= 0:

        return []

    path = []

    row = ROWS - 1
    col = COLS - 1

    while (row, col) != (0, 0):

        path.append((row, col))

        top = 0
        left = 0

        if row > 0 and dp_grid[row - 1][col] != -1:

            top = dp_grid[row - 1][col]

        if col > 0 and dp_grid[row][col - 1] != -1:

            left = dp_grid[row][col - 1]

        # PRIORITIZE TOP FIRST
        if top > 0:

            row -= 1

        elif left > 0:

            col -= 1

        else:

            return []

    path.append((0, 0))

    path.reverse()

    return path


def fill_dp(grid, screen):

    FONT = pygame.font.SysFont(None, 30)

    rows = len(grid)
    cols = len(grid[0])

    if grid[0][0] == -1:

        grid[0][0] = 0

    else:

        grid[0][0] = 1

    for row in range(rows):

        for col in range(cols):

            if grid[row][col] == -1:

                continue

            if row == 0 and col == 0:

                continue

            top = 0
            left = 0

            if row > 0 and grid[row - 1][col] != -1:

                top = grid[row - 1][col]

            if col > 0 and grid[row][col - 1] != -1:

                left = grid[row][col - 1]

            # DYNAMIC PROGRAMMING
            grid[row][col] = top + left

            draw_grid(
                screen,
                grid,
                FONT,
                current=(row, col)
            )

            pygame.time.wait(120)

    # BUILD ONE VALID PATH
    path = reconstruct_path(grid)

    return path


def draw_grid(screen, grid, font, current=None, path=None):

    screen.fill((240, 240, 240))

    title_font = pygame.font.SysFont(None, 40)

    title = title_font.render(
        "SPACE = Run DP | R = Reset | ESC = Back",
        True,
        TEXT
    )

    screen.blit(title, (20, 20))

    if path is None:

        path = []

    for row in range(ROWS):

        for col in range(COLS):

            x = col * CELL_SIZE + 180
            y = row * CELL_SIZE + 80

            color = WHITE

            # OBSTACLES
            if grid[row][col] == -1:

                color = BLACK

            # RECONSTRUCTED VALID PATH
            elif (row, col) in path:

                color = YELLOW

            # CURRENT PROCESSING CELL
            elif current == (row, col):

                color = BLUE

            else:

                color = GREEN

            pygame.draw.rect(
                screen,
                color,
                (x, y, CELL_SIZE, CELL_SIZE)
            )

            pygame.draw.rect(
                screen,
                GREY,
                (x, y, CELL_SIZE, CELL_SIZE),
                2
            )

            # DRAW DP VALUES
            if grid[row][col] != -1:

                text = font.render(
                    str(grid[row][col]),
                    True,
                    TEXT
                )

                text_rect = text.get_rect(
                    center=(
                        x + CELL_SIZE // 2,
                        y + CELL_SIZE // 2
                    )
                )

                screen.blit(text, text_rect)

    # TOTAL PATHS
    total_paths = grid[ROWS - 1][COLS - 1]

    if total_paths <= 0:

        result_message = "No Valid Path Found"

    else:

        result_message = (
            f"Total Paths = {total_paths}   |   Valid Path Highlighted"
        )

    # BIGGER RESULT FONT
    result_font = pygame.font.SysFont(None, 38)

    result_text = result_font.render(
        result_message,
        True,
        RED
    )

    # POSITION BELOW GRID
    result_rect = result_text.get_rect(
        center=(WIDTH // 2, HEIGHT - 150)
    )

    screen.blit(result_text, result_rect)

    pygame.display.update()


def run(screen):

    FONT = pygame.font.SysFont(None, 30)

    grid = create_grid()

    path = []

    running = True

    while running:

        draw_grid(
            screen,
            grid,
            FONT,
            path=path
        )

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                return

            if event.type == pygame.KEYDOWN:

                # RUN DP
                if event.key == pygame.K_SPACE:

                    path = fill_dp(grid, screen)

                    draw_grid(
                        screen,
                        grid,
                        FONT,
                        path=path
                    )

                # RESET GRID
                elif event.key == pygame.K_r:

                    grid = create_grid()

                    path = []

                # EXIT VISUALIZER
                elif event.key == pygame.K_ESCAPE:

                    running = False
