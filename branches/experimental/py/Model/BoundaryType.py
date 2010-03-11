from NamedDescribedDatasetWithSVGItemInProject import NamedDescribedDatasetWithSVGItemInProject

class BoundaryType(NamedDescribedDatasetWithSVGItemInProject):
    def __init__(self, project, id=None, name=None, svgItem=None, description=None, defaultGrainSize=None):
        super(BoundaryType, self).__init__(project, id, name, svgItem, description)
        self.project.registerBoundaryType(self)
