from Point import Point

class PolygonPoint(Point):
    def __init__(self, id=None, polygon=None, x=0, y=0, position=0):
        Point.__init__(self, id, x, y)
        self.polygon = polygon
        self.position = position
