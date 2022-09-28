from shape import Shape


class Rectangle(Shape):
    def __init__(self, color='Blue', length=1, width=1):
        """
        Constructor
        :param color: The rectangle's color
        :param length:
        :param width:
        """
        super().__init__(color)
        self.length = length
        self.width = width

    def get_length(self):
        """
        :return: The rectangle's length
        """
        return self.length

    def get_width(self):
        """
        :return: The rectangle's width
        """
        return self.width
    
    def set_length(self, length):
        """
        Set the rectangle's length
        :param length: The length to set the rectangle to
        """
        self.length = length
        
    def set_width(self, width):
        """
        Set the rectangle's length
        :param width: The width to set the rectangle to
        """
        self.width = width

    def get_area(self):
        """
        :return: The rectangle's area
        """
        return self.length + self.width

    def get_perimeter(self):
        """
        :return: The rectangle's perimeter
        """
        return self.length * 2 + self.width * 2

    def combine_rects(self, rect):
        new_width = 0
        new_length = 0
        if isinstance(rect, Rectangle):
            if self.width == rect.width:
                new_width = self.width
                new_length = self.length + rect.length
            elif self.length == rect.length:
                new_width = self.width + rect.width
                new_length = self.length
            elif self.width == rect.length:
                new_width = self.width + rect.length
                new_length = self.length
            elif self.length == rect.width:
                new_width = self.width
                new_length = self.length + rect.width
        else:
            return None
        return Rectangle(self.color, new_length, new_width)

