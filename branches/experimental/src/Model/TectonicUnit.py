from NamedDescribedDatasetWithSvgItemInProject import NamedDescribedDatasetWithSvgItemInProject

class TectonicUnit(NamedDescribedDatasetWithSvgItemInProject):
    def __init__(self, project, id=None, name=None, svgItem=None, description=None, defaultGrainSize=None):
        super(TectonicUnit, self).__init__(project, id, name, svgItem, description)
