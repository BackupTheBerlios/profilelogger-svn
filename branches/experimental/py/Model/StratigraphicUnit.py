from NamedDescribedDatasetWithDrawingInProject import NamedDescribedDatasetWithDrawingInProject

class StratigraphicUnit(NamedDescribedDatasetWithDrawingInProject):
    def __init__(self, project, id=None, name=None, drawing=None, description=None, defaultGrainSize=None):
        super(StratigraphicUnit, self).__init__(project, id, name, drawing, description)
        self.project.registerStratigraphicUnit(self)
