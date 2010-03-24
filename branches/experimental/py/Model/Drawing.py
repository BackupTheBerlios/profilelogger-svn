from NamedDescribedDataset import *

from StraightLine import *

class Drawing(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None):
        NamedDescribedDataset.__init__(self, id, name, description)
