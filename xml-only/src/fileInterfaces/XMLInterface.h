/* 
 * File:   XMLInterface.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 19:50
 */

#ifndef _XMLINTERFACE_H
#define	_XMLINTERFACE_H

#include <QDomDocument>
#include <QObject>

class Project;
class Profile;
class ProfileCorrelation;
class Bed;
class BedCorrelation;
class Sample;
class Image;

class XMLInterface : public QObject {
    Q_OBJECT
public:
    XMLInterface(QObject* p = 0);
    virtual ~XMLInterface();

    bool save(Project* p);
    bool load(Project* p, const QString& path);

protected:
    bool getProjectPathFromUserAndSave();

    void saveMetadata();
    void saveOutcropQualities();
    void saveColors();
    void saveFacies();
    void saveLithologies();
    void saveLengthUnits();
    void saveClasticGrainSizes();
    void saveCarbonateGrainSizes();
    void saveBeddingTypes();
    void saveBoundaryTypes();
    void saveFossils();
    void saveSedimentStructures();
    void saveCustomSymbols();
    void saveLithologicalUnitTypes();
    void saveLithologicalUnits();
    
    void saveProfiles();
    void saveProfileCorrelations();
    void saveBedCorrelation(BedCorrelation* c, QDomElement& groupE);
    void saveProfile(Profile* p);
    void saveSample(Profile* p, Sample* s);
    void saveBed(Bed* bed, QDomElement& bedE);
    void saveFossilsInBed(Bed* bed, QDomElement& bedE);
    void saveSedimentStructuresInBed(Bed* bed, QDomElement& bedE);
    void saveCustomSymbolsInBed(Bed* bed, QDomElement& bedE);
    
    void loadMetadata();
    void loadOutcropQualities();
    void loadColors();
    void loadFacies();
    void loadLithologies();
    void loadBeddingTypes();
    void loadBoundaryTypes();
    void loadFossils();
    void loadSedimentStructures();
    void loadCustomSymbols();
    void loadLithologicalUnitTypes();
    void loadLithologicalUnits();

    void loadProfiles();
    void loadProfileCorrelations();
    void loadBedCorrelation(BedCorrelation* p, QDomElement& bedCorrelationE);
    void loadProfile(Profile* p, QDomElement& profileE);
    void loadBed(Bed* bed, QDomElement& bedE);
    void loadFossilsInBed(Bed* bed, QDomElement& bedE);
    void loadSedimentStructuresInBed(Bed* bed, QDomElement& bedE);
    void loadCustomSymbolsInBed(Bed* bed, QDomElement& bedE);
    void loadGrainSizeForBed(Bed* bed, QDomElement& bedE);

private:
    Project* _project;
    QDomDocument _doc;
    QDomElement _dataE;
    QDomElement _metaE;
    QDomElement _outcropQualitiesE;
    QDomElement _colorsE;
    QDomElement _lithologiesE;
    QDomElement _beddingTypesE;
    QDomElement _boundaryTypesE;
    QDomElement _clasticGrainSizesE;
    QDomElement _carbonateGrainSizesE;
    QDomElement _fossilsE;
    QDomElement _sedimentStructuresE;
    QDomElement _customSymbolsE;
    QDomElement _lengthUnitsE;
    QDomElement _faciesE;
    QDomElement _lithologicalUnitTypesE;
    QDomElement _lithologicalUnitsE;
};

#endif	/* _XMLINTERFACE_H */

