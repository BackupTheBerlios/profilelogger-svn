from NamedDescribedDatasetWithSvgItemInProject import NamedDescribedDatasetWithSvgItemInProject

class PointOfInterest(NamedDescribedDatasetWithSvgItemInProject):
    def __init__(self, project, id=None, name=None, svgItem=None, description=None, defaultGrainSize=None):
        super(PointOfInterest, self).__init__(project, id, name, svgItem, description)
        self.project.registerPointOfInterest(self)
