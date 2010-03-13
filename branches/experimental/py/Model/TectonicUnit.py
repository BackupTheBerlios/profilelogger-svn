from NamedDescribedDatasetWithSVGItemInProject import NamedDescribedDatasetWithSVGItemInProject

class TectonicUnit(NamedDescribedDatasetWithSVGItemInProject):
    def __init__(self, project, id=None, name=None, svgItem=None, description=None, defaultGrainSize=None):
        super(TectonicUnit, self).__init__(project, id, name, svgItem, description)
        self.project.registerTectonicUnit(self)
