from graphics import Line, Point  # Assuming `graphics` module contains `Line` and `Point`

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2, color="white"):
        if self._win is None:
            return

        # Ensure the coordinates are integers
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        # We'll draw the lines that form the cell and fill optionally
        fill_lines = []
        step = 1  # Define how fine the fill lines should be
        for y in range(y1, y2, step):
            fill_lines.append(Line(Point(x1, y), Point(x2, y)))

        for line in fill_lines:
            self._win.draw_line(line, color)

        # Draw the walls if they are intact
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False, color="blue"):
        half_length_x = abs(self._x2 - self._x1) // 2
        half_length_y = abs(self._y2 - self._y1) // 2
        x_center = half_length_x + self._x1
        y_center = half_length_y + self._y1

        half_length2_x = abs(to_cell._x2 - to_cell._x1) // 2
        half_length2_y = abs(to_cell._y2 - to_cell._y1) // 2
        x_center2 = half_length2_x + to_cell._x1
        y_center2 = half_length2_y + to_cell._y1

        # Choose the color based on whether we're undoing a move
        if undo:
            color = "grey"

        # Draw the line representing the move
        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, color)

        # Optional: logging the move for debugging purposes
        print(f"Drawing move {'undo' if undo else 'to'} ({to_cell._x1}, {to_cell._y1}) with color {color}")