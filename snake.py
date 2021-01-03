# page - https://www.edureka.co/blog/snake-game-with-pygame/
import pygame
import random
import sys
pygame.init()  # dostep do wszystkich metod z pygame
width = 900
height = 600
dis = pygame.display.set_mode((width, height))  # rozmiar okna
pygame.display.update()  # aktualizuje ekran
pygame.display.set_caption('snake zrobiony ze strony, pewnie dziala cool')  # daje tytul na samej gorze

starting_x = width / 2
starting_y = height / 2
x_delta = 0
y_delta = 0

snake_size = 30

clock = pygame.time.Clock()

# Food
"""class Food2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def re_generate_food():
        Food.x = random.randrange(0, width - snake_size, snake_size)
        Food.y = random.randrange(0, height - snake_size, snake_size)


apple = Food2(random.randrange(0, width - snake_size, snake_size), random.randrange(0, height - snake_size, snake_size))
print(apple.x, apple.y)"""


class Food:
    x = random.randrange(0, width - snake_size, snake_size)
    y = random.randrange(0, height - snake_size, snake_size)

    @staticmethod
    def re_generate_food():
        Food.x = random.randrange(0, width - snake_size, snake_size)
        Food.y = random.randrange(0, height - snake_size, snake_size)




previous = pygame.K_RIGHT  # previous to zmienna przetrzymujaca poprzednio wcisniety klawisz
first_round_in_game = True  # first iteration of loop game_over

snake = list()
snake.append([starting_x, starting_y])
print(snake)
steps = list()

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # event ktory po nacisnieciu przycisku wylaczania zamienia game_over na True
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and previous != pygame.K_RIGHT:
                x_delta = -snake_size
                y_delta = 0
                previous = pygame.K_LEFT
            if event.key == pygame.K_RIGHT and previous != pygame.K_LEFT:
                x_delta = snake_size
                y_delta = 0
                previous = pygame.K_RIGHT
            if event.key == pygame.K_UP and previous != pygame.K_DOWN:
                x_delta = 0
                y_delta = -snake_size
                previous = pygame.K_UP
            if event.key == pygame.K_DOWN and previous != pygame.K_UP:
                x_delta = 0
                y_delta = snake_size
                previous = pygame.K_DOWN


    starting_x += x_delta
    starting_y += y_delta
    dis.fill("black")
    # Draw Food outside of snake
    while Food.x == starting_x and Food.y == starting_y:
        Food.re_generate_food()
        if not first_round_in_game:
            print("jedzonko")
            snake.append([starting_x - x_delta, starting_y - y_delta])
            steps.append((x_delta, y_delta))
            #print(snake)
    first_round_in_game = False
    pygame.draw.rect(dis, "red", [Food.x, Food.y, snake_size, snake_size])

    #print(snake)
    for index in range(len(snake)):
        if index == 0:
            snake[index][0] += x_delta
            snake[index][1] += y_delta
        else:
            snake[index][0] = snake[index - 1][0] - x_delta
            snake[index][1] = snake[index - 1][1] - y_delta


    #print(snake)
    """for index, element in enumerate(snake):
        element[0] -= index * x_delta
        element[1] -= index * y_delta"""

    # Draw snake
    for element in snake:
        pygame.draw.rect(dis, "blue", [element[0], element[1], snake_size, snake_size])  # rysujemy niebieski prostokat w miejscu 200x150 o wymiarach 10x10
    pygame.draw.rect(dis, "blue", [starting_x, starting_y, snake_size, snake_size])

    pygame.display.update()

    if starting_x < 0 or starting_x > width - snake_size or starting_y < 0 or starting_y > height - snake_size:  # wychodzenie poza krawedzie rysunku
        game_over = True

    clock.tick(7)

pygame.quit()  # wylacza wszyskie podmoduły pygame
quit()
