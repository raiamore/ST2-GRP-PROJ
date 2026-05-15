import pygame
from heap_logic import MinHeap

WIDTH, HEIGHT = 800, 600

heap = MinHeap()

processed_event = ""

# USER INPUT
typing_mode = False
priority_input = ""
task_input = ""
input_stage = "priority"


def draw_heap(screen):

    global processed_event
    global typing_mode
    global priority_input
    global task_input
    global input_stage

    FONT = pygame.font.SysFont(None, 30)

    screen.fill((25, 25, 35))

    title = FONT.render(
        "SPACE = Add Event | ENTER = Confirm | ESC = Back",
        True,
        (255, 255, 255)
    )

    screen.blit(title, (20, 20))

    # SHOW PROCESSED EVENT
    if processed_event != "":

        processed_text = FONT.render(
            f"Processed: {processed_event}",
            True,
            (255, 220, 100)
        )

        screen.blit(processed_text, (20, 60))

    # INPUT MODE
    if typing_mode:

        if input_stage == "priority":

            input_text = FONT.render(
                f"Enter Priority: {priority_input}",
                True,
                (255, 255, 0)
            )

        else:

            input_text = FONT.render(
                f"Enter Task Name: {task_input}",
                True,
                (255, 255, 0)
            )

        screen.blit(input_text, (20, 100))

    # EMPTY HEAP
    if heap.is_empty():

        empty_text = FONT.render(
            "No Events in Queue",
            True,
            (200, 200, 200)
        )

        screen.blit(empty_text, (280, 300))

    else:

        for i, value in enumerate(heap.heap):

            priority = value[0]
            event_name = value[1]

            x = WIDTH // 2 + (i % 4) * 120 - 180
            y = 170 + (i // 4) * 120

            pygame.draw.circle(
                screen,
                (100, 200, 255),
                (x, y),
                40
            )

            priority_text = FONT.render(
                str(priority),
                True,
                (0, 0, 0)
            )

            screen.blit(priority_text, (x - 10, y - 15))

            event_text = FONT.render(
                event_name,
                True,
                (255, 255, 255)
            )

            screen.blit(event_text, (x - 35, y + 45))

            # CONNECT TO PARENT
            if i > 0:

                parent = (i - 1) // 2

                parent_x = (
                    WIDTH // 2 +
                    (parent % 4) * 120 - 180
                )

                parent_y = (
                    170 +
                    (parent // 4) * 120
                )

                pygame.draw.line(
                    screen,
                    (255, 255, 255),
                    (parent_x, parent_y),
                    (x, y),
                    2
                )

    pygame.display.flip()


def run(screen):

    global processed_event
    global typing_mode
    global priority_input
    global task_input
    global input_stage

    running = True

    while running:

        draw_heap(screen)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                return

            if event.type == pygame.KEYDOWN:

                # START INPUT MODE
                if event.key == pygame.K_SPACE and not typing_mode:

                    typing_mode = True

                    priority_input = ""

                    task_input = ""

                    input_stage = "priority"

                # PROCESS MIN EVENT
                elif event.key == pygame.K_RETURN and not typing_mode:

                    removed = heap.extract_min()

                    if removed:

                        processed_event = (
                            f"{removed[1]} "
                            f"(Priority {removed[0]})"
                        )

                # EXIT
                elif event.key == pygame.K_ESCAPE:

                    running = False

                # HANDLE USER TYPING
                elif typing_mode:

                    # ENTER KEY
                    if event.key == pygame.K_RETURN:

                        # MOVE TO TASK INPUT
                        if input_stage == "priority":

                            if priority_input.isdigit():

                                input_stage = "task"

                        # FINALIZE INSERTION
                        else:

                            if task_input.strip() != "":

                                heap.insert(
                                    (
                                        int(priority_input),
                                        task_input
                                    )
                                )

                            typing_mode = False

                    # BACKSPACE
                    elif event.key == pygame.K_BACKSPACE:

                        if input_stage == "priority":

                            priority_input = (
                                priority_input[:-1]
                            )

                        else:

                            task_input = (
                                task_input[:-1]
                            )

                    # ONLY NUMBERS FOR PRIORITY
                    else:

                        if input_stage == "priority":

                            if event.unicode.isdigit():

                                priority_input += (
                                    event.unicode
                                )

                        else:

                            task_input += event.unicode
