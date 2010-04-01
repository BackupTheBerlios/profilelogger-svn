clean:
	rm -f `find . -name "*.pyc"`
run:
	python ProfileLogger.py
status: clean
	svn status
dbclean:
	psql -h 192.168.196.134 -U jolo profilelogger -f tools/sqlscripts/drop_schema.sql
dbcreate:
	psql -h 192.168.196.134 -U jolo profilelogger -f tools/sqlscripts/create_schema.sql
dbinit:
	psql -h 192.168.196.134 -U jolo profilelogger -f tools/sqlscripts/drop_create_schema.sql