import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        grid = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                cell = []
                if randomize:
                    cell = random.randint(0, 1)
                row.append(cell)
            grind.append(row)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        neighbours = []
        positions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

        for pos in positions:
            _x = cell[1] + pos[0]
            _y = cell[0] + pos[1]
            if _x < 0 or _y < 0:
                continue
            if _x > self.cols - 1 or _y > self.rows - 1:
                continue
            val = self.curr_generation[_y][_x]
            neighbours.append(val)
        return neighbours


    def get_next_generation(self) -> Grid:
        grid = self.curr_generation.copy()

        changes = []

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                neighbours = self.get_neighbours((row, col))
                n = sum(neighbours)
                cell = grid[row][col]
                if n not in [2, 3] and cell == 1:
                    changes.append(((row, col), 0))
                elif n == 3 and cell == 0:
                    changes.append(((row, col), 1))

        for case in changes:
            (row, col), a = case[0], case[1]
            grid[row][col] = a

        return grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        if not self.is_max_generations_exceeded and self.is_changing:
            self.prev_generation, self.curr_generation = (
                self.curr_generation,
                self.get_next_generation(),
            )
            self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.generations >= self.max_generations

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return str(self.curr_generation) != str(self.prev_generation) or str(
            self.curr_generation
        ) != str(self.get_next_generation())

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        return GameOfLife([10, 10], True)

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        return
