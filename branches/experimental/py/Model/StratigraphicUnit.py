from NamedDescribedDatasetWithSvgItemInProject import NamedDescribedDatasetWithSvgItemInProject

class StratigraphicUnit(NamedDescribedDatasetWithSvgItemInProject):
    def __init__(self, project, id=None, name=None, svgItem=None, description=None, defaultGrainSize=None):
        super(StratigraphicUnit, self).__init__(project, id, name, svgItem, description)
        self.project.registerStratigraphicUnit(self)
