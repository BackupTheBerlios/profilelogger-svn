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
	cp templates/Logic/Finders/InProjectFinder.py generated/Logic/Finders
	cp templates/Logic/Finders/InProfileFinder.py generated/Logic/Finders
	cp templates/Logic/Finders/InBedFinder.py generated/Logic/Finders
	cp templates/Logic/Finders/InFieldBookFinder.py generated/Logic/Finders	

	cp templates/Gui/ComboBoxes/DataSelectionComboBox.py generated/Gui/ComboBoxes
	cp templates/Gui/ComboBoxes/GlobalComboBox.py generated/Gui/ComboBoxes
	cp templates/Gui/ComboBoxes/InProjectComboBox.py generated/Gui/ComboBoxes
	cp templates/Gui/ComboBoxes/InProfileComboBox.py generated/Gui/ComboBoxes
	cp templates/Gui/ComboBoxes/InBedComboBox.py generated/Gui/ComboBoxes
	cp templates/Gui/ComboBoxes/InFieldBookComboBox.py generated/Gui/ComboBoxes

	cp templates/Gui/ItemModels/ManagementItemModel.py generated/Gui/ItemModels
	cp templates/Gui/ItemModels/GlobalItemModel.py generated/Gui/ItemModels
	cp templates/Gui/ItemModels/InProjectItemModel.py generated/Gui/ItemModels
	cp templates/Gui/ItemModels/InProfileItemModel.py generated/Gui/ItemModels
	cp templates/Gui/ItemModels/InBedItemModel.py generated/Gui/ItemModels
	cp templates/Gui/ItemModels/InFieldBookItemModel.py generated/Gui/ItemModels

	cp templates/Gui/ManagementDialogs/ManagementDialog.py generated/Gui/ManagementDialogs
	cp templates/Gui/ManagementDialogs/GlobalManagementDialog.py generated/Gui/ManagementDialogs
	cp templates/Gui/ManagementDialogs/InProjectManagementDialog.py generated/Gui/ManagementDialogs
	cp templates/Gui/ManagementDialogs/InProfileManagementDialog.py generated/Gui/ManagementDialogs
	cp templates/Gui/ManagementDialogs/InBedManagementDialog.py generated/Gui/ManagementDialogs
	cp templates/Gui/ManagementDialogs/InFieldBookManagementDialog.py generated/Gui/ManagementDialogs

	cp templates/Gui/TreeViews/TreeView.py generated/Gui/TreeViews
	cp templates/Gui/TreeViews/ManagementTreeView.py generated/Gui/TreeViews
	cp templates/Gui/TreeViews/InProjectManagementTreeView.py generated/Gui/TreeViews
	cp templates/Gui/TreeViews/InProfileManagementTreeView.py generated/Gui/TreeViews
	cp templates/Gui/TreeViews/InBedManagementTreeView.py generated/Gui/TreeViews
	cp templates/Gui/TreeViews/InFieldBookManagementTreeView.py generated/Gui/TreeViews

	cp templates/runTest.py generated
clean:
	rm -rf generated
	rm -rf src/*.pyc
test: clean run copy-templates initdb
	python generated/runTest.py
refresh-project: clean run copy-templates
	rm -rf app/src/generated
	cp -Rv generated app/src
initdb: drop-schema create-schema
drop-schema:
	/usr/local/postgres/bin/psql -h 192.168.196.137 -d codegen -U jolo -c "DROP SCHEMA DATA CASCADE"
create-schema:
	/usr/local/postgres/bin/psql -h 192.168.196.137 -d codegen -U jolo -c "CREATE SCHEMA DATA"
run-test-app:
	python app/src/app.py