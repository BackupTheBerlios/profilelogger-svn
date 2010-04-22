class PythonEntity(object):
    def __init__(self, parent, name, setter=None, getter=None):
        object.__init__(self)
        self.parent = parent
        self.name = name
        self.setter = setter
        self.getter = getter
    def hasParent(self):
        return self.parent is not None
