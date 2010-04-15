class Dataset(object):
    id = None
    def __init__(self, id=None):
        object.__init__(self)
        self.id = id
    def hasId(self):
        return self.id is not None
    def __str__(self):
        return u"<%1s: ID: %i>" % (self.__class__.__name__, self.id)
    def makeToolTip(self):
        return u'ID: %i' % self.id
