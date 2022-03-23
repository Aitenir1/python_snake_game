class Snake:
    def __init__(self, body_coords: list):
        # self.body_length = []
        self.allowed_length = 100
        self.body_coords = body_coords

    @staticmethod
    def distance(a, b):
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

    def compute_body_length(self):
        length = 0
        for i in range(1, len(self.body_coords)):
            d = self.distance(
                a=self.body_coords[i],
                b=self.body_coords[i - 1]
            )

            if length + d > self.allowed_length:
                self.__body_coords = self.__body_coords[:len(self.body_length) + 1]
                break

            self.body_length.append(d)
            length += d

    def move_to(self, a):
        self.body_coords = [a] + self.__body_coords

    @property
    def body_coords(self):
        return self.__body_coords

    @body_coords.setter
    def body_coords(self, body_coords):
        self.__body_coords = body_coords
        self.body_length = []
        self.compute_body_length()

