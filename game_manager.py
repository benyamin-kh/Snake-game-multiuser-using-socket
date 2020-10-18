import sys
import pygame
import consts

from cell import Cell


class GameManager:

    def __init__(self, size, screen, sx, sy, block_cells):
        self.screen = screen
        self.size = size
        self.cells = []
        self.sx = sx
        self.sy = sy
        self.snakes = list()
        self.turn = 0
        for i in range(self.size):
            tmp = []
            for j in range(self.size):
                tmp.append(Cell(screen, sx + i * consts.cell_size, sy + j * consts.cell_size))
            self.cells.append(tmp)
        for cell in block_cells:
            self.get_cell(cell).set_color(consts.block_color)

    def add_snake(self, snake):
        self.snakes.append(snake)

    def get_cell(self, pos):
        try:
            return self.cells[pos[0]][pos[1]]
        except:
            return None

    def kill(self, killed_snake):
        self.snakes.remove(killed_snake)

    def handle(self, keys):
        for snake in self.snakes:
            snake.handle(keys)
        for snake in self.snakes:
            snake.next_move()

        self.turn += 1
        if self.turn % 10 == 0:
            mx = -1
            pos = (0, 0)
            for i in range(self.size):
                for j in range(self.size):
                    mn = self.size * 3
                    for x in range(self.size):
                        for y in range(self.size):
                            if not self.get_cell((x, y)).is_empty():
                                mn = min(mn, abs(j - y) + abs(i - x))
                    if mn > mx and self.get_cell((i, j)).is_empty():
                        mx = mn
                        pos = (i, j)

            self.get_cell(pos).set_color(consts.fruit_color)
