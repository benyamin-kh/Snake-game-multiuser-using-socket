import pygame, consts, sys


class Snake:

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    dx = {"UP": -1, "DOWN": 1, "LEFT": 0, "RIGHT": 0}
    dy = {"UP": 0, "DOWN": 0, "LEFT": -1, "RIGHT": 1}

    def modify(self, x):
        if x < 0:
            x += self.game.size
        if x >= self.game.size:
            x -= self.game.size
        return x

    def next_move(self):
        head = self.get_head()
        new_head = (self.modify(head[0] + Snake.dy[self.direction]), self.modify(head[1] + Snake.dx[self.direction]))
        self.cells.append(new_head)
        cell = self.game.get_cell(new_head)
        if cell is None or not cell.is_empty() and not cell.is_fruit():
            print("You lose!")
            self.game.kill(self)
            return
        flag = False
        if cell.is_fruit():
            flag = True
        cell.set_color(self.color)
        if not flag:
            cell = self.game.get_cell(self.cells[0])
            cell.set_color(consts.back_color)
            del self.cells[0]

    def handle(self, keys):
        for key in keys:
            direction = self.keys.get(key)

            if direction is None:
                continue
            if Snake.dy[direction] == -Snake.dy[self.direction] and Snake.dx[direction] == -Snake.dx[self.direction]:
                continue

            self.direction = direction
            break
