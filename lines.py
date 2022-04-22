from kivy.graphics import Color, Line


def draw_lines(self):
    with self.canvas:
        Color(1, 1, 1, 0.2)
        for i in range(0, self.V_NB_LINES):
            self.vertical_lines.append(Line())

        for i in range(0, self.H_NB_LINES):
            self.horizontal_lines.append(Line())


def update_lines(self):
    # Vertical Lines
    vl_start_index = -int(self.V_NB_LINES / 2) + 1

    for i in range(vl_start_index, self.V_NB_LINES + vl_start_index):
        line_x = self.get_line_x_from_index(i)
        x1, y1 = self.transform_perspective(line_x, 0)
        x2, y2 = self.transform_perspective(line_x, self.height)
        self.vertical_lines[i].points = [x1, y1, x2, y2]

    # Horizontal Lines
    x_min = self.get_line_x_from_index(self.hl_start_index)
    x_max = self.get_line_x_from_index(self.hl_end_index)

    for i in range(0, self.H_NB_LINES):
        line_y = self.get_line_y_from_index(i)
        x1, y1 = self.transform_perspective(x_min, line_y)
        x2, y2 = self.transform_perspective(x_max, line_y)
        self.horizontal_lines[i].points = [x1, y1, x2, y2]


def get_line_x_from_index(self, index):
    central_line_x = int(self.perspective_point_x)
    spacing = self.V_LINES_SPACING * self.width
    offset = index - 0.5
    line_x = central_line_x + (offset * spacing) - self.current_offset_x
    return line_x


def get_line_y_from_index(self, index):
    line_y = (index * self.H_LINES_SPACING * self.height) - self.current_offset_y
    return line_y
