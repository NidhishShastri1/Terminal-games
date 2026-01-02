import os
import random
import sys

WIDTH = 10
HEIGHT = 10
TREASURES = 5
TRAPS = 5

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def create_map():
    grid = [["." for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for i in range(WIDTH):
        grid[0][i] = "#"
        grid[HEIGHT-1][i] = "#"
    for i in range(HEIGHT):
        grid[i][0] = "#"
        grid[i][WIDTH-1] = "#"

    return grid

def place_random(grid, symbol, count):
    placed = 0
    while placed < count:
        x = random.randint(1, WIDTH-2)
        y = random.randint(1, HEIGHT-2)
        if grid[y][x] == ".":
            grid[y][x] = symbol
            placed += 1

def draw(grid, player_x, player_y, score):
    clear()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x == player_x and y == player_y:
                print("P", end=" ")
            else:
                print(grid[y][x], end=" ")
        print()
    print(f"\n💰 Score: {score}")
    print("Move: W A S D | Quit: Q")

def main():
    grid = create_map()
    place_random(grid, "T", TREASURES)
    place_random(grid, "X", TRAPS)

    exit_x, exit_y = WIDTH-2, HEIGHT-2
    grid[exit_y][exit_x] = "E"

    player_x, player_y = 1, 1
    score = 0

    while True:
        draw(grid, player_x, player_y, score)
        move = input(">> ").lower()

        if move == "q":
            print("👋 You quit the game")
            sys.exit()

        dx, dy = 0, 0
        if move == "w": dy = -1
        elif move == "s": dy = 1
        elif move == "a": dx = -1
        elif move == "d": dx = 1
        else:
            continue

        nx, ny = player_x + dx, player_y + dy

        if grid[ny][nx] == "#":
            continue

        if grid[ny][nx] == "T":
            score += 10
            grid[ny][nx] = "."

        if grid[ny][nx] == "X":
            draw(grid, player_x, player_y, score)
            print("\n💀 You stepped on a trap!")
            print(f"Final Score: {score}")
            sys.exit()

        if grid[ny][nx] == "E":
            draw(grid, player_x, player_y, score)
            print("\n🎉 YOU ESCAPED THE DUNGEON!")
            print(f"Final Score: {score}")
            sys.exit()

        player_x, player_y = nx, ny

if __name__ == "__main__":
    main()
