from NamedDescribedDatasetWithDrawingInProject import NamedDescribedDatasetWithDrawingInProject

class SedimentStructure(NamedDescribedDatasetWithDrawingInProject):
    def __init__(self, project, id=None, name=None, drawing=None, description=None, defaultGrainSize=None):
        super(SedimentStructure, self).__init__(project, id, name, drawing, description)
        self.project.registerSedimentStructure(self)
