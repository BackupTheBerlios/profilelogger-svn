from Dataset import Dataset

class Polygon(Dataset):
    def __init__(self, id=None, drawing=None,
                 posX=0, posY=0, 
                 polygonPoints = [],
                 pen=None, brush=None):
        Dataset.__init__(self, id)
        self.drawing = drawing
        self.posX = posX
        self.posY = posY
        self.polygonPoints = polygonPoints
        self.pen = pen
        self.brush = brush
        
