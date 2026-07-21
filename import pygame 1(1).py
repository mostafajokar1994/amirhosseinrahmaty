import pygame
import random


WIDTH = 1000
HEIGHT = 700

CELL_SIZE = 10

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animal Ecosystem")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 22)

# ------------------
# رنگ ها
# ------------------

BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
WHITE = (255, 255, 255)

RABBIT_COLOR = (255, 255, 255)
FOX_COLOR = (255, 140, 0)
WOLF_COLOR = (120, 120, 120)
HIPPO_COLOR = (160, 60, 200)

# ------------------
# حیوان پایه
# ------------------

class Animal:

    def __init__(self, x, y, energy):

        self.x = x
        self.y = y
        self.energy = energy

    def move(self):

        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

        self.x = max(0, min(WIDTH // CELL_SIZE - 1, self.x))
        self.y = max(0, min(HEIGHT // CELL_SIZE - 1, self.y))

        self.energy -= 1

# ------------------

class Grass:

    def __init__(self):

        self.x = random.randint(0, WIDTH // CELL_SIZE - 1)
        self.y = random.randint(0, HEIGHT // CELL_SIZE - 1)

# ------------------

class Rabbit(Animal):

    def __init__(self):
        super().__init__(
            random.randint(0, WIDTH // CELL_SIZE - 1),
            random.randint(0, HEIGHT // CELL_SIZE - 1),
            50
        )

# ------------------

class Fox(Animal):

    def __init__(self):
        super().__init__(
            random.randint(0, WIDTH // CELL_SIZE - 1),
            random.randint(0, HEIGHT // CELL_SIZE - 1),
            80
        )

# ------------------

class Wolf(Animal):

    def __init__(self):
        super().__init__(
            random.randint(0, WIDTH // CELL_SIZE - 1),
            random.randint(0, HEIGHT // CELL_SIZE - 1),
            120
        )

# ------------------

class Hippo(Animal):

    def __init__(self):
        super().__init__(
            random.randint(0, WIDTH // CELL_SIZE - 1),
            random.randint(0, HEIGHT // CELL_SIZE - 1),
            150
        )

# ------------------
# جهان
# ------------------

grasses = [Grass() for _ in range(300)]

rabbits = [Rabbit() for _ in range(40)]

foxes = [Fox() for _ in range(15)]

wolves = [Wolf() for _ in range(8)]

hippos = [Hippo() for _ in range(4)]

# ------------------

def distance(a, b):

    return abs(a.x - b.x) + abs(a.y - b.y)

# ------------------

running = True

while running:

    clock.tick(30)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # ------------------
    # رشد علف
    # ------------------

    for _ in range(3):
        grasses.append(Grass())

    # ------------------
    # خرگوش
    # ------------------

    for rabbit in rabbits[:]:

        rabbit.move()

        for grass in grasses[:]:

            if distance(rabbit, grass) < 2:

                grasses.remove(grass)

                rabbit.energy += 20

                break

        if rabbit.energy > 90:

            rabbits.append(Rabbit())

            rabbit.energy -= 30

        if rabbit.energy <= 0:

            rabbits.remove(rabbit)

    # ------------------
    # روباه
    # ------------------

    for fox in foxes[:]:

        fox.move()

        for rabbit in rabbits[:]:

            if distance(fox, rabbit) < 2:

                rabbits.remove(rabbit)

                fox.energy += 35

                break

        if fox.energy > 150:

            foxes.append(Fox())

            fox.energy -= 50

        if fox.energy <= 0:

            foxes.remove(fox)

    # ------------------
    # گرگ
    # ------------------

    for wolf in wolves[:]:

        wolf.move()

        targets = rabbits + foxes

        for prey in targets[:]:

            if distance(wolf, prey) < 2:

                if prey in rabbits:
                    rabbits.remove(prey)

                if prey in foxes:
                    foxes.remove(prey)

                wolf.energy += 50

                break

        if wolf.energy > 220:

            wolves.append(Wolf())

            wolf.energy -= 70

        if wolf.energy <= 0:

            wolves.remove(wolf)

    # ------------------
    # اسب آبی
    # ------------------

    for hippo in hippos[:]:

        hippo.move()

        if random.random() < 0.002:

            hippos.append(Hippo())

        if hippo.energy <= 0:
            hippos.remove(hippo)

    # ------------------
    # رسم
    # ------------------

    screen.fill(BLACK)

    for grass in grasses:

        pygame.draw.rect(
            screen,
            GREEN,
            (grass.x * CELL_SIZE,
             grass.y * CELL_SIZE,
             CELL_SIZE,
             CELL_SIZE)
        )

    for rabbit in rabbits:

        pygame.draw.circle(
            screen,
            RABBIT_COLOR,
            (rabbit.x * CELL_SIZE,
             rabbit.y * CELL_SIZE),
            4
        )

    for fox in foxes:

        pygame.draw.circle(
            screen,
            FOX_COLOR,
            (fox.x * CELL_SIZE,
             fox.y * CELL_SIZE),
            5
        )

    for wolf in wolves:

        pygame.draw.circle(
            screen,
            WOLF_COLOR,
            (wolf.x * CELL_SIZE,
             wolf.y * CELL_SIZE),
            6
        )

    for hippo in hippos:

        pygame.draw.circle(
            screen,
            HIPPO_COLOR,
            (hippo.x * CELL_SIZE,
             hippo.y * CELL_SIZE),
            8
        )

    text = font.render(
        f"Grass:{len(grasses)}  Rabbit:{len(rabbits)}  Fox:{len(foxes)}  Wolf:{len(wolves)}  Hippo:{len(hippos)}",
        True,
        WHITE
    )

    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()