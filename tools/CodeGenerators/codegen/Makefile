status: clean
	rm -rf `find . -type f -name "*.pyc"`
	svn status
first: run
run: clean 
	python src/mbuilder.py
copy-templates:
	cp templates/Persistance/ConnectionData.py generated/Persistance/
	cp templates/runTest.py generated
clean:
	rm -rf generated
	rm -rf src/*.pyc
test: run copy-templates initdb
	python generated/runTest.py
initdb: drop-schema create-schema
drop-schema:
	/usr/local/postgres/bin/psql -h 192.168.196.137 -d codegen -U jolo -c "DROP SCHEMA DATA CASCADE"
create-schema:
	/usr/local/postgres/bin/psql -h 192.168.196.137 -d codegen -U jolo -c "CREATE SCHEMA DATA"