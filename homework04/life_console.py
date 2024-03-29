import curses

from homework04.tests.life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        screen.border("|", "|", "-", "-", "+", "+", "+", "+")
        pass

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        colors = [
            curses.COLOR_RED,
            curses.COLOR_YELLOW,
            curses.COLOR_GREEN,
            curses.COLOR_BLUE,
            curses.COLOR_CYAN,
        ]
        grid = self.life.curr_generation

        for i in colors:
            curses.init_pair((i + 1) % 5, i % 5, -1)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                try:
                    screen.scrollok(0)
                    screen.move(row + 2, col + 2)
                    screen.addch(ord("*") if grid[row][col] else " ", curses.color_pair((row + col) % 5))
                except curses.error:
                    pass
        pass

    def run(self) -> None:
        screen = curses.initscr()
        curses.noecho()
        self.draw_borders(screen)
        self.draw_grid(screen)
        screen.refresh()
        UI.run(self)

        while self.life.is_changing and not self.life.is_max_generations_exceeded:
            self.life.step()
            self.draw_grid(screen)
            screen.refresh()
            UI.run(self)

        curses.endwin()

