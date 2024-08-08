from pwn import *
import numpy as np
import sys
from copy import deepcopy


class GameOfLife:

    def __init__(self, cells=[], generations=1):
        """
        initialize all variables and calculate the dimensions
        """

        self.cells = cells.copy()
        self.generations = generations
        self.dim_y = len(cells)
        self.dim_x = len(cells[0])
        self.cur_dim_y = 0
        self.cur_dim_x = 0

    def get_neighbors(self, y, x):
        """
        gets all neighbors around current cell and returns them in a list
        """
        neighbor_list = []

        for i in range(y - 1, y + 2):
            if i < 0 or i > (self.cur_dim_y - 1):
                continue
            else:
                for j in range(x - 1, x + 2):
                    if j < 0 or j > (self.cur_dim_x - 1):
                        continue
                    elif i == y and j == x:
                        continue
                    else:
                        neighbor_list.append(self.cells[i][j])

        return neighbor_list

    def check_neighbors(self, cur_cell, neighbor_list):
        """
        checks cur_cell if living or dead and returns status of next generation cell by
        comparing next generation by evaluating the neighborlist
        """
        next_gen_cell = cur_cell
        alive_count = neighbor_list.count(1)

        if cur_cell == 1:
            if alive_count == 2 or alive_count == 3:
                next_gen_cell = 1
            else:
                next_gen_cell = 0
        else:
            if alive_count == 3:
                next_gen_cell = 1

        return next_gen_cell

    def add_empty_boarder(self, cur_field, cur_dim_y, cur_dim_x):
        """
        adds around the current field a boarder with dead cells
        """
        new_field = np.zeros((cur_dim_y + 2, cur_dim_x + 2))
        for y, row in enumerate(cur_field):
            for x, cur_cell in enumerate(row):
                new_field[y + 1, x + 1] = cur_cell

        return new_field

    def remove_empty_boarder(self, new_cells):
        """
        removes the every empty column and row of the field
        """
        new_cells = np.array(new_cells)
        removing = True

        while removing == True:
            if len(new_cells) == 0:
                return [[]]
            elif np.count_nonzero(new_cells[0]) == 0:
                new_cells = np.delete(new_cells, 0, 0)
            elif np.count_nonzero(new_cells[::-1][0]) == 0:
                new_cells = np.delete(new_cells, -1, 0)
            elif np.count_nonzero(new_cells.T[0]) == 0:
                new_cells = np.delete(new_cells, 0, 1)
            elif np.count_nonzero(new_cells.T[::-1][0]) == 0:
                new_cells = np.delete(new_cells, -1, 1)
            else:
                removing = False

        return new_cells

    def evaluate_generations(self):
        """
        visits every element of the field, gets neighbors, checks neighbors and updates
        cells.
        """
        self.cells = deepcopy(self.add_empty_boarder(self.cells, self.dim_y, self.dim_x))
        new_cells = deepcopy(self.cells)

        for generation in range(0, self.generations):
            self.cur_dim_y = len(self.cells)
            self.cur_dim_x = len(self.cells[0])
            new_cells = deepcopy(self.add_empty_boarder(new_cells, self.cur_dim_y, self.cur_dim_x))
            self.cells = deepcopy(new_cells)
            for y, row in enumerate(self.cells):
                for x, cur_cell in enumerate(row):
                    neighbor_list = self.get_neighbors(y, x)
                    new_cells[y][x] = self.check_neighbors(cur_cell, neighbor_list)

        new_cells = self.remove_empty_boarder(new_cells)
        return new_cells.tolist()


conn = remote('34.31.85.60', 32431)
conn.recvuntil(b"Game On :D\x1b[m\n\n")
while True:
    try:
        board = conn.recvuntil(b"generations: ").decode().split("\n")
    except:
        print(conn.recvall())
        break
    generations = int(board[-1].split()[-2])
    print("\n".join(board[0:-2]))
    print(board[-1])
    cells = [[0 if i == '.' else 1 for i in row] for row in board[0:-2]]
    result = GameOfLife(cells, generations).evaluate_generations()
    living_lives = sum([row.count(1) for row in result])
    print(living_lives)
    conn.sendline(str(living_lives).encode())
    print(conn.recvline())