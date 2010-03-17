from GraphicsTextLabel import GraphicsTextLabel

class HeightMarkLabel(GraphicsTextLabel):
    def __init__(self, parent, scene, height):
        GraphicsTextLabel.__init__(self, parent, scene, '')
        self.setText(QString(height))
