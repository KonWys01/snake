# page - https://www.edureka.co/blog/snake-game-with-pygame/
import pygame
import random
import time
pygame.init()  # all pygame functions

width = 900
height = 600
snake_size = 30

dis = pygame.display.set_mode((width, height))  # rozmiar okna
pygame.display.update()
pygame.display.set_caption('snake')  # title at the top left corner

font_style = pygame.font.SysFont(None, 30)


def message(msg, color):
    message_to_show = font_style.render(msg, True, color)
    dis.blit(message_to_show, [width / 6, height / 2])


score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, "yellow")
    dis.blit(value, [0, 0])


class Food:
    x = random.randrange(0, width, snake_size)
    y = random.randrange(0, height, snake_size)

    @staticmethod
    def re_generate_food():
        Food.x = random.randrange(0, width, snake_size)
        Food.y = random.randrange(0, height, snake_size)


# snake eats itself - program stops
def snake_eat_itself(snake_list):
    for coordinate in snake_list:
        if snake_list.count(coordinate) > 1:
            return True


def game_loop():
    # make whole loop work
    game_over = False

    # first round in the game
    previous = pygame.K_RIGHT
    first_round_in_game = True  # first iteration of loop game_over

    # first positions
    starting_x = 0
    starting_y = 0
    x_delta = 0
    y_delta = 0

    # making first snake
    snake = list()
    snake.append([starting_x, starting_y])

    number_of_elements = width / snake_size * height / snake_size
    clock = pygame.time.Clock()

    game_restart = True
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

        # Generate Food outside of head
        while snake[0][0] == Food.x and snake[0][1] == Food.y:
            Food.re_generate_food()
            first_round_in_game = False
            if not first_round_in_game:
                snake.append([starting_x - x_delta, starting_y - y_delta])
                break
        first_round_in_game = False

        # All food has been eaten
        if number_of_elements == len(snake):
            print("Good Job, you have won!")
            time.sleep(2)
            game_over = True

        # Generate Food outside of whole snake
        while [Food.x, Food.y] in snake:
            Food.re_generate_food()

        pygame.draw.rect(dis, "red", [Food.x, Food.y, snake_size, snake_size])

        # Make all elements of snake move
        for index in range(len(snake) - 1, -1, -1):
            if index == 0:
                snake[index][0] += x_delta
                snake[index][1] += y_delta
            else:
                snake[index][0] = snake[index - 1][0]
                snake[index][1] = snake[index - 1][1]

        # Collision of snake with itself
        if snake_eat_itself(snake):
            game_over = True

        # Draw whole snake
        for element in snake:
            pygame.draw.rect(dis, "blue", [element[0], element[1], snake_size, snake_size])  # draw all blue cubes

        pygame.draw.rect(dis, "blue", [starting_x, starting_y, snake_size, snake_size])

        # Draw head of the snake
        for index in range(0, len(snake), 1):
            if index == 0:
                pygame.draw.rect(dis, "white", [snake[index][0], snake[index][1], snake_size, snake_size])
                break

        # Displaying your score
        your_score(len(snake) - 1)
        pygame.display.update()

        # snake is off the edge
        if starting_x < 0 or starting_x > width - snake_size or starting_y < 0 or starting_y > height - snake_size:
            game_over = True
        clock.tick(10)

    message("You lost this round, wanna start again type Y, wanna end type N", "red")
    pygame.display.update()
    while game_restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # ends whole game
                game_restart = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    game_loop()
                if event.key == pygame.K_n:
                    quit()
                    game_restart = False
                    break


game_loop()
pygame.quit()  # turns off all pygame modules
quit()
