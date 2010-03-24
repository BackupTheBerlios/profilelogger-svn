from NamedDescribedDatasetWithDrawingInProject import NamedDescribedDatasetWithDrawingInProject

class BoundaryType(NamedDescribedDatasetWithDrawingInProject):
    def __init__(self, project, id=None, name=None, drawing=None, description=None, defaultGrainSize=None):
        super(BoundaryType, self).__init__(project, id, name, drawing, description)
        self.project.registerBoundaryType(self)
