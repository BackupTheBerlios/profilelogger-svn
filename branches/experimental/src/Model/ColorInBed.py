from DatasetInBed import DatasetInBed

class ColorInBed(DatasetInBed):
    def __init__(self, bed, id=None, color=None, begin=0, end=100, 
                 name=None, description=None):
        super(ColorInBed, self).__init__(bed, id, begin, end, name, description)
        self.color = color
        self.bed.registerColor(self)
    def __str__(self):
        return u'Color %s from %i to %i Percent of bed' % (self.color,
                                                       self.begin,
                                                       self.end)
    def hasColor(self):
        return self.color is not None
