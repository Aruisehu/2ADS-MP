class Box:
    def __init__(self, h, w, l):
        self.__height = h
        self.__width = w
        self.__length = l

    def dimensions(self):
        return [self.__height, self.__width, self.__length]

    def surface(self):
        return self.__width * self.__length

    def get_height(self):
        return self.__height

    def rotate(self):
        mem = self.__height
        self.__height = self.__width
        self.__width = self.__length
        self.__length = mem

if __name__ == "__main__":
    b = Box(10, 20, 30)
    print(b.dimensions())
    print(b.surface())
    print(b.get_height())
    b.rotate()
    print(b.surface())
    print(b.get_height())
    b.rotate()
    print(b.surface())
    print(b.get_height())
