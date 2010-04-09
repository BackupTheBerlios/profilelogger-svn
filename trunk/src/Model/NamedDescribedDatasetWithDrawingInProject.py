from NamedDescribedDatasetInProject import NamedDescribedDatasetInProject

class NamedDescribedDatasetWithDrawingInProject(NamedDescribedDatasetInProject):
    def __init__(self, project, id=None, name=None, drawing=None, description=None):
        NamedDescribedDatasetInProject.__init__(self, project, id, name, description)
        self.drawing = drawing
    def hasDrawing(self):
        return self.drawing is not None
