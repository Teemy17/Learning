import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def draw(self):
        plt.plot(self.x_coord, self.y_coord, 'ro', markersize=6)

    def get_position(self):
        return f"{self.x_coord}, {self.y_coord}"

class Rectangle2D(Point):
    def __init__(self, max_x, max_y, min_x, min_y):
        super().__init__((max_x + min_x) / 2, (max_y + min_y) / 2)
        self.max_x = max_x
        self.max_y = max_y
        self.min_x = min_x
        self.min_y = min_y

    def draw(self):
        plt.plot([self.min_x, self.max_x, self.max_x, self.min_x, self.min_x], 
                 [self.max_y, self.max_y, self.min_y, self.min_y, self.max_y], 'b-')

    def get_width(self):
        return self.max_x - self.min_x

    def get_height(self):
        return self.max_y - self.min_y

def get_rectangle(points):
    x_coords = [float(points[i]) for i in range(0, len(points), 2)]
    y_coords = [float(points[i]) for i in range(1, len(points), 2)]

    points_list = [Point(x_coords[i], y_coords[i]) for i in range(min(len(x_coords), len(y_coords)))]

    for point in points_list:
        point.draw()
        point.get_position()

    bounding_rectangle = Rectangle2D(max(x_coords), max(y_coords), min(x_coords), min(y_coords))
    bounding_rectangle.draw()
    
    print(f"The bounding rectangle is centered at ({bounding_rectangle.get_position()}) with width {bounding_rectangle.get_width()} and height {bounding_rectangle.get_height()}")

def main():
    user_input = input("Enter the points: ").split()
    get_rectangle(user_input)
    plt.show()

main()
