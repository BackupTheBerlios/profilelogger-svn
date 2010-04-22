status: clean
	rm -rf `find . -type f -name "*.pyc"`
	svn status
first: run
run: 
	python src/mbuilder.py
gen: run copy-templates
copy-templates:
	cp templates/Persistance/ConnectionData.py generated/Persistance/
	cp templates/Finders/Finder.py generated/Finders
	cp templates/Finders/InProjectFinderBase.py generated/Finders
	cp templates/Finders/InProfileFinderBase.py generated/Finders
	cp templates/Finders/InBedFinderBase.py generated/Finders
	cp templates/Finders/InFieldBookFinderBase.py generated/Finders
	cp templates/runTest.py generated
clean:
	rm -rf generated
	rm -rf src/*.pyc
test: clean run copy-templates initdb
	python generated/runTest.py
initdb: drop-schema create-schema
drop-schema:
	/usr/local/postgres/bin/psql -h 192.168.196.137 -d codegen -U jolo -c "DROP SCHEMA DATA CASCADE"
create-schema:
	/usr/local/postgres/bin/psql -h 192.168.196.137 -d codegen -U jolo -c "CREATE SCHEMA DATA"