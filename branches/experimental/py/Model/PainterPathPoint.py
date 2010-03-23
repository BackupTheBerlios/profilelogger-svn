from Point import Point

class PainterPathPoint(Point):
    def __init__(self, id=None, painterPath=None, x=0, y=0, position=0):
        Point.__init__(self, id, x, y)
        self.painterPath = painterPath
        self.position = position
