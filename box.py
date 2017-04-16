class Box:
    def __init__(self, dimensions):
        self.__height = dimensions[0]
        self.__width = dimensions[1]
        self.__length = dimensions[2]

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
    
    def min_surface(self):
        h = self.__height 
        w = self.__width 
        l = self.__length
        return min(h*w, h*l, l*w)
        

if __name__ == "__main__":
    b = Box([10, 20, 30])
    print(b.dimensions())
    print(b.surface())
    print(b.get_height())
    b.rotate()
    print(b.surface())
    print(b.get_height())
    b.rotate()
    print(b.surface())
    print(b.get_height())
