status: clean
	rm -rf `find . -type f -name "*.pyc"`
	svn status
first: run
run: 
	python src/mbuilder.py
gen: run copy-templates
copy-templates:
	cp templates/Logic/Persistance/ConnectionData.py generated/Logic/Persistance/
	cp templates/Logic/Finders/Finder.py generated/Logic/Finders
	cp templates/Logic/Finders/InProjectFinderBase.py generated/Logic/Finders
	cp templates/Logic/Finders/InProfileFinderBase.py generated/Logic/Finders
	cp templates/Logic/Finders/InBedFinderBase.py generated/Logic/Finders
	cp templates/Logic/Finders/InFieldBookFinderBase.py generated/Logic/Finders
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