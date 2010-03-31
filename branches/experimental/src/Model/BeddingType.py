from NamedDescribedDatasetWithSvgItemInProject import NamedDescribedDatasetWithSvgItemInProject

class BeddingType(NamedDescribedDatasetWithSvgItemInProject):
    def __init__(self, project, id=None, name=None, svgItem=None, description=None, defaultGrainSize=None):
        super(BeddingType, self).__init__(project, id, name, svgItem, description)
        self.project.registerBeddingType(self)
