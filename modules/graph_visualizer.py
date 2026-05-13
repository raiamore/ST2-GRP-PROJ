import pygame
import collections

WIDTH, HEIGHT = 800, 600

nodes_pos = {
    'A': (150, 180),
    'B': (320, 140),
    'C': (320, 320),
    'D': (550, 180),
    'E': (750, 280),
    'F': (550, 450)
}

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def draw_graph(
        screen,
        visited=set(),
        current=None,
        traversal=[],
        selected=None,
        mode=""
):

    FONT = pygame.font.SysFont(None, 32)

    screen.fill((240, 240, 240))

    # DRAW EDGES
    for node, neighbors in graph.items():

        x1, y1 = nodes_pos[node]

        for neighbor in neighbors:

            x2, y2 = nodes_pos[neighbor]

            pygame.draw.line(
                screen,
                (0, 0, 0),
                (x1, y1),
                (x2, y2),
                3
            )

    # DRAW NODES
    for node, (x, y) in nodes_pos.items():

        color = (180, 180, 180)

        # SELECTED START NODE
        if node == selected:
            color = (100, 150, 255)

        # VISITED NODES
        if node in visited:
            color = (100, 220, 100)

        # CURRENT NODE
        if node == current:
            color = (255, 120, 120)

        pygame.draw.circle(screen, color, (x, y), 35)

        text = FONT.render(node, True, (0, 0, 0))

        text_rect = text.get_rect(center=(x, y))

        screen.blit(text, text_rect)

    # INSTRUCTIONS
    instructions = FONT.render(
        "B = BFS | D = DFS | Click Node = Start | ESC = Back",
        True,
        (0, 0, 0)
    )

    screen.blit(instructions, (20, 20))

    # MODE DISPLAY
    mode_text = FONT.render(
        f"Mode: {mode}",
        True,
        (0, 0, 0)
    )

    screen.blit(mode_text, (20, 60))

    # SELECTED NODE DISPLAY
    if selected:

        selected_text = FONT.render(
            f"Selected Start Node: {selected}",
            True,
            (0, 0, 0)
        )

        screen.blit(selected_text, (20, 100))

    # TRAVERSAL DISPLAY
    traversal_display = " -> ".join(traversal[-10:])

    traversal_text = FONT.render(
        "Traversal: " + traversal_display,
        True,
        (0, 0, 0)
    )

    screen.blit(traversal_text, (20, 550))

    pygame.display.update()


def get_clicked_node(pos):

    x_mouse, y_mouse = pos

    for node, (x, y) in nodes_pos.items():

        distance = ((x_mouse - x) ** 2 + (y_mouse - y) ** 2) ** 0.5

        if distance <= 35:
            return node

    return None


def bfs(screen, start):

    queue = collections.deque([start])

    visited = set()

    traversal = []

    while queue:

        current = queue.popleft()

        if current not in visited:

            visited.add(current)

            traversal.append(current)

            draw_graph(
                screen,
                visited,
                current,
                traversal,
                start,
                "BFS"
            )

            pygame.time.wait(700)

            for neighbor in graph[current]:

                if neighbor not in visited:
                    queue.append(neighbor)


def dfs(screen, start):

    stack = [start]

    visited = set()

    traversal = []

    while stack:

        current = stack.pop()

        if current not in visited:

            visited.add(current)

            traversal.append(current)

            draw_graph(
                screen,
                visited,
                current,
                traversal,
                start,
                "DFS"
            )

            pygame.time.wait(700)

            for neighbor in reversed(graph[current]):

                if neighbor not in visited:
                    stack.append(neighbor)


def run(screen):

    running = True

    selected_start = None

    while running:

        draw_graph(
            screen,
            selected=selected_start
        )

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                return

            if event.type == pygame.MOUSEBUTTONDOWN:

                selected_start = get_clicked_node(event.pos)

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_b and selected_start:

                    bfs(screen, selected_start)

                elif event.key == pygame.K_d and selected_start:

                    dfs(screen, selected_start)

                elif event.key == pygame.K_ESCAPE:

                    running = False