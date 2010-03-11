from NamedDescribedDatasetWithSVGItemInProject import NamedDescribedDatasetWithSVGItemInProject

class SedimentStructure(NamedDescribedDatasetWithSVGItemInProject):
    def __init__(self, project, id=None, name=None, svgItem=None, description=None, defaultGrainSize=None):
        super(SedimentStructure, self).__init__(project, id, name, svgItem, description)
        self.project.registerSedimentStructure(self)
