import os

class PythonModelBuilder:
    def __init__(self):
        pass
    def makeParameterList(self, cl):
        fnames = []
        for f in cl.fields:
            fnames.append(f.fieldName)
        print "parameters: ",', '.join(fnames)

        lst = []
        lst.append('self')
        for field in cl.fields:
            param=None
            if field.tableColumn.hasDefaultText():
                param = "%s='%s'" % (field.fieldName, field.tableColumn.defaultText)
            elif field.tableColumn.hasDefaultValue():
                param = "%s=%s" % (field.fieldName, field.tableColumn.defaultValue)
            if param is None:
                param = '%s=None' % field.fieldName
            lst.append(param)
        return ', '.join(lst)
    def indent(self, level, str):
        return '%s%s' % ('    ' * level, str)
    def buildClasses(self, path, classes):
        for c in classes:
            buf = []
            i = 0
            buf.append(self.indent(i, '# generated from class definition'))
            if c.hasParentClass():
                pc = c.parentClass
                buf.append(self.indent(i, 'from %s import *\n' % pc.name))
                buf.append(self.indent(i, 'class %s(%s):' % (c.name, pc.name)))
                i += 1
                buf.append(self.indent(i, 'def __init__(%s):' % self.makeParameterList(c)))
                i += 1
                buf.append(self.indent(i, '%s.__init__(self)' % pc.name))
                i -= 2
            else:
                buf.append(self.indent(i, 'class %s(object):' % c.name))
                i += 1
                buf.append(self.indent(i, 'def __init__(%s):' % self.makeParameterList(c)))
                i += 1
                buf.append(self.indent(i, 'object.__init__(self)'))
                i -= 2
            i += 2
            for f in c.fields:
                buf.append(self.indent(i, 'self.%s = %s' % (f.fieldName, f.fieldName)))
            i -= 2
            print '\n'.join(buf),'\n---'
            fn = '%s/%s.py' % (path, c.name)
            f = open(fn, 'w')
            f.write('\n'.join(buf))
            f.close()
    def makePathToModule(self, path):
        f = open('%s/__init__.py' % path, 'w')
        f.write('# nothing')
        f.close()
    def buildModules(self, path, modules):
        for m in modules:
            p = '%s/%s' % (path, m.name)
            os.mkdir(p)
            self.makePathToModule(p)
            self.buildClasses(p, m.classes.values())
            self.buildModules(p, m.pythonModules.values())
    def build(self, model):
        os.mkdir('generated')
        self.buildModules('generated', model.pythonModules.values())
        self.setupSqlAlchemy('generated', model.pythonModules.values())
    def setupSqlAlchemy(self, path, modules):
        p = '%s/Persistance' % path
        os.mkdir(p)
        self.makePathToModule(p)
        buf = []
        i = 0
        self.appendIndented(i, '# Generated Persistance Layer for SQLAlchemy', buf)
        self.appendIndented(i, 'from sqlalchemy import *', buf)
        self.appendIndented(i, 'from sqlalchemy.orm import *', buf)
        for module in modules:
            for cl in module.classes.values():
                self.appendIndented(i, 'from %s.%s import *' % (module.name, cl.name), buf)
        self.appendIndented(i, 'class Database:', buf)
        i += 1
        self.appendIndented(i, 'def __init__(self):', buf)
        i += 1
        self.appendIndented(i, 'self.engine = None', buf)
        self.appendIndented(i, 'self.metadata = None', buf)
        self.appendIndented(i, 'self.session = None', buf)
        i -= 1
        self.setupTables(modules, buf, i)
        self.setupMappers(modules, buf, i)
        self.appendIndented(i, 'def open(self, connectionData):', buf)
        i += 1
        self.appendIndented(i, 'self.setupTables()', buf)
        self.appendIndented(i, 'self.setupMappers()', buf)
        self.appendIndented(i, 'self.engine = create_engine(connectionData.makeConnectionString(), echo=True)', buf)
        self.appendIndented(i, 'self.engine.connect()', buf)
        self.appendIndented(i, 'self.session = create_session(bind=self.engine, autocommit=False, autoflush=False)', buf)
        self.appendIndented(i, 'self.metadata.bind = self.engine', buf)
        self.appendIndented(i, 'if connectionData.createSchema:', buf)
        i += 1
        self.appendIndented(i, 'self.metadata.create_all()', buf)
        i -= 1
        i -= 1
        self.appendIndented(i, 'def begin(self):', buf)
        i += 1
        self.appendIndented(i, 'return self.session.begin()', buf)
        i -= 1
        self.appendIndented(i, 'def commit(self):', buf)
        i += 1
        self.appendIndented(i, 'self.session.commit()', buf)
        i -= 1
        self.appendIndented(i, 'def rollback(self):', buf)
        i += 1
        self.appendIndented(i, 'self.session.rollback()', buf)
        i -= 1
        
        f = open('%s/Database.py' % p, 'w')
        f.write('\n'.join(buf))
        f.close()

    def setupMappers(self, modules, buf, i):
        self.appendIndented(i, 'def setupMappers(self):', buf)
        i += 1
        self.appendIndented(i, 'clear_mappers()', buf)
        for module in modules:
            for c in module.classes.values():
                if c.hasTable():
                    colMappings = []
                    sorting = None
                    if len(c.sorting) > 0:
                        sortingCols = []
                        for s in c.sorting:
                            t = "self.tables['%s.%s'].c.%s" % (s.pythonField.tableColumn.table.schema.name,
                                                               s.pythonField.tableColumn.table.name,
                                                               s.pythonField.tableColumn.name)
                            if s.ascending:
                                t += '.asc()'
                            else:
                                t += '.desc()'
                            sortingCols.append(t)
                        sorting = 'order_by=[%s]' % ', '.join(sortingCols)
                    for field in c.fields:
                        if field.tableColumn.referencedColumn is None:
                            colMappings.append("'%s': self.tables['%s.%s'].c.%s" % (field.fieldName,
                                                                                    field.tableColumn.table.schema.name,
                                                                                    field.tableColumn.table.name,
                                                                                    field.tableColumn.name))

                        else:
                            relconf = "'%s': relation(%s" % (field.fieldName,
                                                             field.relationClass)
                            if field.hasBackrefName():
                                relconf += ", backref='%s'" % field.backrefName
                            if field.hasCascadeRule():
                                relconf += ", cascade='%s'" % field.cascade
                            relconf += ')'
                            colMappings.append(relconf)
                        tmp = "mapper(%s, self.tables['%s.%s'], properties={" % (c.name, 
                                                                                 c.table.schema.name, c.table.name)
                    tmp += ', '.join(colMappings)
                    tmp += '}'
                    if sorting is not None:
                        tmp += ', %s' % sorting
                    tmp += ')'
                    
                    self.appendIndented(i, tmp, buf)

    def setupTables(self, modules, buf, i):
        self.appendIndented(i, 'def setupTables(self):', buf)
        i += 1
        self.appendIndented(i, 'self.metadata = MetaData()', buf)
        self.appendIndented(i, 'self.tables = {}', buf)
        for module in modules:
            for c in module.classes.values():
                if c.table is not None:
                    tdef = "self.tables['%s.%s'] = Table('%s'" % (c.table.schema.name,
                                                                  c.table.name,
                                                                  c.table.name)
                    tdef += ', self.metadata'
                    colDefs = []
                    for col in c.table.columns.values():
                        self.appendTableColumnDefinition(col, colDefs)
                    tdef += ', %s' % ', '.join(colDefs)
                    if len(c.table.uniqueConstraints) > 0:
                        for uc in c.table.uniqueConstraints.values():
                            colnames = []
                            for cc in uc.columns:
                                colnames.append("'%s'" % cc.name)
                            tdef += ", UniqueConstraint(%s, name='%s')" % (', '.join(colnames), uc.name)
                    if len(c.table.notEmptyConstraints) > 0:
                        for uc in c.table.notEmptyConstraints.values():
                            tdef += ", CheckConstraint(\"%s <> ''\", name='%s')" % (uc.column.name, uc.name)
                    if len(c.table.rangeCheckConstraints) > 0:
                        for rc in c.table.rangeCheckConstraints.values():
                            tdef += ", CheckConstraint(\"%s BETWEEN %s and %s\", name='%s')" % (rc.column.name, rc.min, rc.max, rc.name)
                    tdef += ", schema='%s'" % col.table.schema.name
                    tdef += ')'
                    self.appendIndented(i, tdef, buf)

    def appendTableColumnDefinition(self, col, buf):
        colName = col.name
        typeName = col.dataType.sqlAlchemyName()
        tmp = "Column('%s', %s" % (colName, typeName)
        if col.hasSequence():
            tmp += ", Sequence('%s', schema='%s')" % (col.sequence.name, col.sequence.schema.name)
        for fk in col.table.foreignKeys.values():
            if fk.localColumn == col:
                tmp += ", ForeignKey('%s.%s.%s')" % (fk.referencedColumn.table.schema.name,
                                                     fk.referencedColumn.table.name,
                                                     fk.referencedColumn.name)
        if col.nullable:
            tmp += ', nullable=False'
        else:
            tmp += ', nullable=True'
        if col.hasDefaultText():
            tmp += ", server_default='%s'" % col.defaultText
        if col.hasDefaultValue():
            tmp += ", server_default='%s'" % col.defaultValue
        if col.table.hasPrimaryKey():
            if col == col.table.primaryKey.column:
                tmp += ", primary_key=True"
        tmp += ")"
        buf.append(tmp)
    def appendIndented(self, i, code, buffer):
        buffer.append(self.indent(i, code))
