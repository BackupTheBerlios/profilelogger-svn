from NamedDescribedDatasetInProject import NamedDescribedDatasetInProject

class NamedDescribedDatasetWithSVGItemInProject(NamedDescribedDatasetInProject):
    def __init__(self, project, id=None, name=None, svgItem=None, description=None):
        NamedDescribedDatasetInProject.__init__(self, project, id, name, description)
        self.svgItem = svgItem
    def hasSVGItem(self):
        return self.svgItem is not None
