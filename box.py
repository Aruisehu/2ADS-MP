class Box:
    def __init__(self, dimensions):
        self.__height = dimensions[0]
        self.__width = dimensions[1]
        self.__length = dimensions[2]

    def dimensions(self):
        return [self.__height, self.__width, self.__length]

    def surface(self):
        return self.__width * self.__length

    def volume(self):
        return self.surface() * self.__height

    def get_height(self):
        return self.__height

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def rotate(self):
        mem = self.__height
        self.__height = self.__width
        self.__width = self.__length
        self.__length = mem

    def base_rotate(self):
        self.__width, self.__length =  self.__length, self.__width
    
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
