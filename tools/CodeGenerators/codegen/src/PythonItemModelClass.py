class PythonItemModelClass(object):
    def __init__(self, module, name, dataClassName, template, headerStrings=[]):
        self.module = module
        self.name = name
        self.dataClassName = dataClassName
        self.template = template
        self.headerStrings = headerStrings
