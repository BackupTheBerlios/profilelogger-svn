from DatasetInBed import DatasetInBed

class CustomSymbolInBed(DatasetInBed):
    def __init__(self, bed, id=None, customSymbol=None, begin=0, end=100, 
                 name=None, description=None):
        super(CustomSymbolInBed, self).__init__(bed, id, begin, end, name, description)
        self.customSymbol = customSymbol
    def __str__(self):
        return u'Custom Symbol %s from %i to %i Percent of bed' % (self.customSymbol,
                                                                   self.begin,
                                                                   self.end)
