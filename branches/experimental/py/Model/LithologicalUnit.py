from NamedDescribedDatasetWithDrawingInProject import NamedDescribedDatasetWithDrawingInProject

class LithologicalUnit(NamedDescribedDatasetWithDrawingInProject):
    def __init__(self, project, id=None, name=None, drawing=None, description=None, defaultGrainSize=None):
        super(LithologicalUnit, self).__init__(project, id, name, drawing, description)
        self.project.registerLithologicalUnit(self)
