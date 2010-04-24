from Logic.Persistance.Database import *
from Logic.Persistance.ConnectionData import *

def run():
  db = Database()
  print 'setting up tables...'
  cd = ConnectionData(host='192.168.196.137',
                      port='5432',
                      dbName='codegen',
                      user='jolo',
                      password='nix',
                      createSchema=True)
  db.open(cd)
  print 'done.'
if __name__ == '__main__':
  run()
