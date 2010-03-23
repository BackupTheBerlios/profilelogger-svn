from Dataset import Dataset

class PainterPath(Dataset):
    def __init__(self, id=None, drawing=None,
                 posX=0, posY=0, 
                 painterPathPoints = [],
                 pen=None, brush=None):
        Dataset.__init__(self, id)
        self.drawing = drawing
        self.posX = posX
        self.posY = posY
        self.painterPathPoints = painterPathPoints
        self.pen = pen
        self.brush = brush
        
