import pygame

def run(screen):

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)
    big_font = pygame.font.SysFont(None, 34)

    WIDTH, HEIGHT = screen.get_size()
    NODE_RADIUS = 20


    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None


    class BST:
        def __init__(self):
            self.root = None

        def insert(self, value):
            def _insert(node, value):
                if not node:
                    return Node(value)
                if value < node.value:
                    node.left = _insert(node.left, value)
                else:
                    node.right = _insert(node.right, value)
                return node

            self.root = _insert(self.root, value)

        def search(self, value):
            path = []
            node = self.root

            while node:
                path.append(node)

                if value == node.value:
                    break
                elif value < node.value:
                    node = node.left
                else:
                    node = node.right

            return path


    def draw_tree(node, x, y, spacing, highlight_set):

        if not node:
            return

        color = (255, 80, 80) if node in highlight_set else (100, 200, 255)

        pygame.draw.circle(screen, color, (x, y), NODE_RADIUS)

        text = font.render(str(node.value), True, (0, 0, 0))
        screen.blit(text, (x - 10, y - 10))

        if node.left:
            pygame.draw.line(screen, (0, 0, 0), (x, y), (x - spacing, y + 80), 2)
            draw_tree(node.left, x - spacing, y + 80, spacing // 2, highlight_set)

        if node.right:
            pygame.draw.line(screen, (0, 0, 0), (x, y), (x + spacing, y + 80), 2)
            draw_tree(node.right, x + spacing, y + 80, spacing // 2, highlight_set)


    bst = BST()
    for v in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(v)

    input_text = ""

    search_button = pygame.Rect(10, 50, 120, 40)

    search_path = []
    search_index = 0
    search_active = False
    search_timer = 0
    search_target = None

    highlight_set = set()

    running = True


    def start_search():

        nonlocal search_path, search_index, search_active, search_timer, search_target, highlight_set, input_text

        if input_text.isdigit():

            val = int(input_text)

            search_target = val
            search_path = bst.search(val)

            search_index = 0
            search_timer = 0
            search_active = True
            highlight_set = set()

            input_text = ""


    while running:

        screen.fill((240, 240, 240))

        draw_tree(bst.root, WIDTH // 2, 130, 150, highlight_set)


        bar = font.render(
            "I=Insert | O=In | P=Pre | T=Post | D=Delete | ESC=Back",
            True,
            (0, 0, 0)
        )
        screen.blit(bar, (10, 10))

        pygame.draw.rect(screen, (180, 180, 180), search_button)
        screen.blit(font.render("SEARCH", True, (0, 0, 0)), (20, 60))


        pygame.draw.rect(screen, (255, 255, 255), (140, 50, 150, 40))
        pygame.draw.rect(screen, (0, 0, 0), (140, 50, 150, 40), 2)

        screen.blit(font.render(input_text, True, (0, 0, 0)), (150, 60))


        if search_active:

            search_timer += 1

            if search_timer % 20 == 0:

                if search_index < len(search_path):
                    highlight_set = set(search_path[:search_index + 1])
                    search_index += 1
                else:
                    search_active = False


        pygame.display.flip()

        if search_target is not None and not search_active:

            if search_path and search_path[-1].value == search_target:
                msg = big_font.render(f"FOUND: {search_target}", True, (0, 150, 0))
            else:
                msg = big_font.render("NOT FOUND", True, (200, 0, 0))

            screen.blit(msg, (WIDTH // 2 - 80, 80))


        pygame.display.flip()



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False


            if event.type == pygame.MOUSEBUTTONDOWN:


                if search_button.collidepoint(event.pos):
                    start_search()


            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False


                elif event.key == pygame.K_RETURN:
                    start_search()


                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]

                else:
                    input_text += event.unicode


        clock.tick(30)
