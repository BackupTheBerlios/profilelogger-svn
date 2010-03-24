from NamedDescribedDatasetWithDrawingInProject import NamedDescribedDatasetWithDrawingInProject

class BeddingType(NamedDescribedDatasetWithDrawingInProject):
    def __init__(self, project, id=None, name=None, drawing=None, description=None, defaultGrainSize=None):
        super(BeddingType, self).__init__(project, id, name, drawing, description)
        self.project.registerBeddingType(self)
