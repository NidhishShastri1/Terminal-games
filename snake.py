import os
import time
import random
import sys

WIDTH = 30
HEIGHT = 15
SPEED = 0.15

def clear():
    os.system("cls")

def food_pos(snake):
    while True:
        f = (random.randint(1, WIDTH-2), random.randint(1, HEIGHT-2))
        if f not in snake:
            return f

def draw(snake, food, score):
    clear()
    print("╔" + "═"*(WIDTH-2) + "╗")
    for y in range(1, HEIGHT-1):
        print("║", end="")
        for x in range(1, WIDTH-1):
            if (x, y) == snake[0]:
                print("O", end="")
            elif (x, y) in snake:
                print("o", end="")
            elif (x, y) == food:
                print("*", end="")
            else:
                print(" ", end="")
        print("║")
    print("╚" + "═"*(WIDTH-2) + "╝")
    print(f"Score: {score}  |  W A S D to move | Q quit")

def main():
    snake = [(5,5), (4,5), (3,5)]
    direction = (1,0)
    food = food_pos(snake)
    score = 0

    import msvcrt

    while True:
        draw(snake, food, score)

        if msvcrt.kbhit():
            k = msvcrt.getch().decode().lower()
            if k == "w" and direction != (0,1): direction = (0,-1)
            elif k == "s" and direction != (0,-1): direction = (0,1)
            elif k == "a" and direction != (1,0): direction = (-1,0)
            elif k == "d" and direction != (-1,0): direction = (1,0)
            elif k == "q": sys.exit()

        hx, hy = snake[0]
        dx, dy = direction
        nh = (hx+dx, hy+dy)

        if nh in snake or nh[0] in (0, WIDTH-1) or nh[1] in (0, HEIGHT-1):
            clear()
            print("💀 GAME OVER")
            print("Final Score:", score)
            sys.exit()

        snake.insert(0, nh)

        if nh == food:
            score += 10
            food = food_pos(snake)
        else:
            snake.pop()

        time.sleep(SPEED)

if __name__ == "__main__":
    main()
