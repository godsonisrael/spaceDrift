from kivy.graphics import Triangle, Color


def draw_ship(self):
    with self.canvas:
        Color(0, 0, 0)
        self.ship = Triangle()


def update_ship(self):
    center_x = self.width / 2
    base_y = self.SHIP_BASE_Y * self.height
    ship_half_width = self.SHIP_WIDTH * self.width / 2
    ship_height = self.SHIP_HEIGHT * self.height

    self.ship_coordinates[0] = (center_x - ship_half_width, base_y)
    self.ship_coordinates[1] = (center_x, base_y + ship_height)
    self.ship_coordinates[2] = (center_x + ship_half_width, base_y)

    x1, y1 = self.transform_perspective(*self.ship_coordinates[0])
    x2, y2 = self.transform_perspective(*self.ship_coordinates[1])
    x3, y3 = self.transform_perspective(*self.ship_coordinates[2])

    self.ship.points = [x1, y1, x2, y2, x3, y3]


def is_ship_inside_tile(self, ti_x, ti_y):
    x_min, y_min = self.get_tile_coordinates(ti_x, ti_y)
    x_max, y_max = self.get_tile_coordinates(ti_x + 1, ti_y + 1)

    for i in range(0, 3):
        px, py = self.ship_coordinates[i]
        if x_min <= px <= x_max and y_min <= py <= y_max:
            return True
    return False


def is_ship_collide(self):
    for i in range(0, len(self.tiles_coordinates)):
        ti_x, ti_y = self.tiles_coordinates[i]
        if ti_y > self.current_loop_y + 1:
            return False
        if self.is_ship_inside_tile(ti_x, ti_y):
            return True
    return False
