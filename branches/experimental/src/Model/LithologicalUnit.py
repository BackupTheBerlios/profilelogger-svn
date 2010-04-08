from NamedDescribedDatasetWithSvgItemInProject import NamedDescribedDatasetWithSvgItemInProject

class LithologicalUnit(NamedDescribedDatasetWithSvgItemInProject):
    def __init__(self, project, id=None, name=None, svgItem=None, description=None, defaultGrainSize=None):
        super(LithologicalUnit, self).__init__(project, id, name, svgItem, description)
