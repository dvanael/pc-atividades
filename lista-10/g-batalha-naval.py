# G. Batalha Naval

num_navios = int(input())
posicoes = []
for _ in range(num_navios):
    posicoes.append(list(map(int, input().split())))

grid = [["" for _ in range(10)] for _ in range(10)]


def add_ships_on_grid(grid: list[list], posicoes: list[list[int]]) -> str:
    for p in posicoes:
        direction, length, row, col = p
        col -= 1
        row -= 1

        if direction == 0:
            # horizontal
            if col + length > 10:
                return "N"

            for i in range(length):
                if grid[row][col + i]:
                    return "N"
            for i in range(length):
                grid[row][col + i] = "#"
        else:
            # vertical
            if row + length > 10:
                return "N"
            for i in range(length):
                if grid[row + i][col]:
                    return "N"
            for i in range(length):
                grid[row + i][col] = "#"

    return "Y"


print(add_ships_on_grid(grid, posicoes))
