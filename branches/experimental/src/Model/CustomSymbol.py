from NamedDescribedDatasetWithSvgItemInProject import NamedDescribedDatasetWithSvgItemInProject

class CustomSymbol(NamedDescribedDatasetWithSvgItemInProject):
    def __init__(self, project, id=None, name=None, svgItem=None, description=None, defaultGrainSize=None):
        super(CustomSymbol, self).__init__(project, id, name, svgItem, description)
