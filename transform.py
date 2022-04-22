def transform_perspective(self, x, y):
    linear_y = y * self.perspective_point_y / self.height
    if linear_y > self.perspective_point_y:
        linear_y = self.perspective_point_y

    diff_x = x - self.perspective_point_x
    diff_y = self.perspective_point_y - linear_y
    proportion_y = pow((diff_y / self.perspective_point_y), 2)

    tr_x = self.perspective_point_x + (diff_x * proportion_y)
    tr_y = (1 - proportion_y) * self.perspective_point_y

    return int(tr_x), int(tr_y)
