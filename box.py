class Box:
    def __init__(self, dimensions):
        self.__set_dimensions(dimensions)

    def dimensions(self):
        return [self.__height, self.__width, self.__length]

    def surface(self):
        return self.__width * self.__length

    def get_height(self):
        return self.__height

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def __set_dimensions(self, dims):
        self.__height = dims[0]
        self.__width = dims[1]
        self.__length = dims[2]

    def rotate(self):
        mem = self.__height
        self.__height = self.__width
        self.__width = self.__length
        self.__length = mem
        return Box(self.dimensions())

    def base_rotate(self):
        self.__width, self.__length =  self.__length, self.__width

    def set_max_height_state(self):
        max_height = 0
        for i in range(3):
            if max_height < self.__height:
                max_height = self.__height
                dimensions = self.dimensions()
            self.rotate()
        self.__set_dimensions(dimensions)


    def min_surface(self):
        h = self.__height
        w = self.__width
        l = self.__length
        return min(h*w, h*l, l*w)

    def __lt__(self, other):
        return (self.__length < other.get_length()) and (self.__width < other.get_width())

    def __repr__(self):
        return "{}\n".format(self.dimensions())


if __name__ == "__main__":
    b = Box([10, 20, 30])
    print(b.surface())
    print(b.get_height())
    b.rotate()
    print(b.surface())
    print(b.get_height())
    b.rotate()
    print(b.surface())
    print(b.get_height())
