class ConnectionData:
    def __init__(self, host=None, port=None, dbName=None, schema=None, 
                 user=None, password=None,
                 dropSchema=False, createSchema=False):
        self.host = host
        self.port = port
        self.dbName = dbName
        self.schema = schema
        self.user = user
        self.password = password
        self.dropSchema = dropSchema
        self.createSchema = createSchema
        
    def makeConnectionString(self):
        return u'postgresql://%s:%s@%s:%i/%s' % (
            self.user,
            self.password,
            self.host,
            self.port,
            self.dbName)
