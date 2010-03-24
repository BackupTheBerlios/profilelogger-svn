from NamedDescribedDatasetWithDrawingInProject import NamedDescribedDatasetWithDrawingInProject

class Color(NamedDescribedDatasetWithDrawingInProject):
    def __init__(self, project, id=None, name=None, drawing=None, description=None, defaultGrainSize=None):
        super(Color, self).__init__(project, id, name, drawing, description)
        self.project.registerColor(self)
