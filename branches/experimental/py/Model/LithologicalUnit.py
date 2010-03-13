from NamedDescribedDatasetWithSVGItemInProject import NamedDescribedDatasetWithSVGItemInProject

class LithologicalUnit(NamedDescribedDatasetWithSVGItemInProject):
    def __init__(self, project, id=None, name=None, svgItem=None, description=None, defaultGrainSize=None):
        super(LithologicalUnit, self).__init__(project, id, name, svgItem, description)
        self.project.registerLithologicalUnit(self)
