#!/usr/bin/python3
'''A class inherited from models rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''This is the definition of a square

       args:
       x(int): x value
       y(int)
       id: Bool:
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''Superclass args width and height must replace size'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''overloding the method'''

        return "[square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.height)

    @property
    def size(self):
        '''size getter'''

        return self.width

    @size.setter
    def size(self, value):
        '''size setter'''

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if len(args) > 0 and args:
            idx = 0
            for i in args:
                if idx == 0:
                    self.id = i
                elif idx == 1:
                    self.size = i
                elif idx == 2:
                    self.x = i
                elif idx == 3:
                    self.y = i
                idx += 1
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.id = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
