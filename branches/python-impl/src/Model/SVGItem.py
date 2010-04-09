from NamedDescribedDataset import NamedDescribedDataset

class SVGItem(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None, 
                 svgData=None, originalPath=None):
        NamedDescribedDataset.__init__(self, id, name, description)
        self.svgData = svgData
        self.originalPath = originalPath
    def hasSVGData(self):
        return self.svgData is not None
    def hasOriginalPath(self):
        return self.originalPath is not None
