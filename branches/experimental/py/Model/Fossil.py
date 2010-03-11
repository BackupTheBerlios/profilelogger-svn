from NamedDescribedDatasetWithSVGItemInProject import NamedDescribedDatasetWithSVGItemInProject

class Fossil(NamedDescribedDatasetWithSVGItemInProject):
    def __init__(self, project, id=None, name=None, svgItem=None, description=None, defaultGrainSize=None):
        super(Fossil, self).__init__(project, id, name, svgItem, description)
        self.project.registerFossil(self)
