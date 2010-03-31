from NamedDescribedDatasetWithDrawingInProject import NamedDescribedDatasetWithDrawingInProject

class PointOfInterest(NamedDescribedDatasetWithDrawingInProject):
    def __init__(self, project, id=None, name=None, drawing=None, description=None, defaultGrainSize=None):
        super(PointOfInterest, self).__init__(project, id, name, drawing, description)
        self.project.registerPointOfInterest(self)
