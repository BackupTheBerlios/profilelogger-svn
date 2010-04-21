class PythonEntity(object):
    def __init__(self, parent, name, setter=None, getter=None):
        self.parent = parent
        self.name = name
        self.setter = setter
        self.getter = getter
