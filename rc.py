import os
import time
import random
import sys

WIDTH = 30
HEIGHT = 20
ROAD_LEFT = 10
ROAD_RIGHT = 20
SPEED = 0.12

def clear():
    os.system("cls")

def draw(player_x, enemies, score):
    clear()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x == ROAD_LEFT or x == ROAD_RIGHT:
                print("|", end="")
            elif (x, y) == (player_x, HEIGHT - 2):
                print("▲", end="")
            elif (x, y) in enemies:
                print("█", end="")
            else:
                print(" ", end="")
        print()
    print(f"Score: {score}")
    print("A/D to move | Q to quit")

def main():
    player_x = (ROAD_LEFT + ROAD_RIGHT) // 2
    enemies = []
    score = 0
    spawn_timer = 0

    import msvcrt

    while True:
        # Input
        if msvcrt.kbhit():
            key = msvcrt.getch().decode().lower()
            if key == "a" and player_x > ROAD_LEFT + 1:
                player_x -= 1
            elif key == "d" and player_x < ROAD_RIGHT - 1:
                player_x += 1
            elif key == "q":
                sys.exit()

        # Spawn enemy
        spawn_timer += 1
        if spawn_timer > 8:
            spawn_x = random.randint(ROAD_LEFT + 1, ROAD_RIGHT - 1)
            enemies.append((spawn_x, 1))
            spawn_timer = 0

        # Move enemies
        new_enemies = []
        for x, y in enemies:
            if y + 1 == HEIGHT - 2 and x == player_x:
                clear()
                print("💥 CRASH!")
                print(f"Final Score: {score}")
                sys.exit()
            if y < HEIGHT - 1:
                new_enemies.append((x, y + 1))

        enemies = new_enemies

        score += 1
        draw(player_x, enemies, score)

        time.sleep(SPEED)

if __name__ == "__main__":
    main()
