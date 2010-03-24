from NamedDescribedDatasetWithDrawingInProject import NamedDescribedDatasetWithDrawingInProject

class CustomSymbol(NamedDescribedDatasetWithDrawingInProject):
    def __init__(self, project, id=None, name=None, drawing=None, description=None, defaultGrainSize=None):
        super(CustomSymbol, self).__init__(project, id, name, drawing, description)
        self.project.registerCustomSymbol(self)
