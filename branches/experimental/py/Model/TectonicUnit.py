from NamedDescribedDatasetWithDrawingInProject import NamedDescribedDatasetWithDrawingInProject

class TectonicUnit(NamedDescribedDatasetWithDrawingInProject):
    def __init__(self, project, id=None, name=None, drawing=None, description=None, defaultGrainSize=None):
        super(TectonicUnit, self).__init__(project, id, name, drawing, description)
        self.project.registerTectonicUnit(self)
