import random
from kivy.graphics import Color, Quad


def draw_tiles(self):
    with self.canvas:
        Color(1, .69, .22)
        for i in range(0, self.NB_TILES):
            self.tiles.append(Quad())


def update_tiles(self):
    for i in range(0, self.NB_TILES):
        tile = self.tiles[i]
        tile_coordinates = self.tiles_coordinates[i]
        ti_x_min, ti_y_min = self.get_tile_coordinates(tile_coordinates[0], tile_coordinates[1])
        ti_x_max, ti_y_max = self.get_tile_coordinates(tile_coordinates[0] + 1, tile_coordinates[1] + 1)

        x1, y1 = self.transform_perspective(ti_x_min, ti_y_min)
        x2, y2 = self.transform_perspective(ti_x_min, ti_y_max)
        x3, y3 = self.transform_perspective(ti_x_max, ti_y_max)
        x4, y4 = self.transform_perspective(ti_x_max, ti_y_min)

        tile.points = [x1, y1, x2, y2, x3, y3, x4, y4]


def get_tile_coordinates(self, ti_x, ti_y):
    ti_y -= self.current_loop_y
    x = self.get_line_x_from_index(ti_x)
    y = self.get_line_y_from_index(ti_y)
    return x, y


def pre_filled_tiles(self):
    for i in range(0, 10):
        self.tiles_coordinates.append((0, i))


def generate_tiles_coordinates(self):
    last_x = 0
    last_y = 0

    for i in range(len(self.tiles_coordinates) - 1, -1, -1):
        if self.tiles_coordinates[i][1] < self.current_loop_y:
            del self.tiles_coordinates[i]

    if len(self.tiles_coordinates) > 0:
        last_coordinates = self.tiles_coordinates[-1]
        last_x = last_coordinates[0]
        last_y = last_coordinates[1] + 1

    for i in range(len(self.tiles_coordinates), self.NB_TILES):

        x_land_gen = random.randint(-1, 1)

        if last_x <= self.hl_start_index:
            x_land_gen = 1
        if last_x >= self.hl_end_index - 1:
            x_land_gen = -1

        self.tiles_coordinates.append((last_x, last_y))

        if x_land_gen == 1:
            last_x += 1
            self.tiles_coordinates.append((last_x, last_y))
            last_y += 1
            self.tiles_coordinates.append((last_x, last_y))
        if x_land_gen == -1:
            last_x -= 1
            self.tiles_coordinates.append((last_x, last_y))
            last_y += 1
            self.tiles_coordinates.append((last_x, last_y))

        last_y += 1
