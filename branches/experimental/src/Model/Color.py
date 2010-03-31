from NamedDescribedDatasetWithSvgItemInProject import NamedDescribedDatasetWithSvgItemInProject

class Color(NamedDescribedDatasetWithSvgItemInProject):
    def __init__(self, project, id=None, name=None, svgItem=None, description=None, defaultGrainSize=None):
        super(Color, self).__init__(project, id, name, svgItem, description)
        self.project.registerColor(self)
