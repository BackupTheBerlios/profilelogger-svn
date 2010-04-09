/* 
 * File:   Profile.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 19:44
 */

#ifndef _PROFILE_H
#define	_PROFILE_H

#include "Dataset.h"
#include "Project.h"

#include <QList>
#include <QMap>

class Bed;
class Sample;
class Image;
class LengthMeasurement;
class LengthUnit;

class Profile : public Dataset {
public:
    Profile(int id = 0,
            const QString& name = QString::null,
            const QString& description = QString::null,
            int scale = 1,
            int legendColumns = 16,
            bool showHeight = true,
            bool showBedNumbers = true,
            bool showLithology = true,
            bool showBeddingType = true,
            bool showTopBoundaryType = true,
            bool showFossils = true,
            bool showSedimentStructures = true,
            bool showGrainSize = true,
            bool showCustomSymbols = true,
            bool showNotes = false,
            bool showColor = true,
            bool showFacies = false,
            bool showLithologicalUnit = false,
            bool showOutcropQuality = false,
            bool showHeightMarks = true,
            LengthUnit* defaultUnit = 0);

    virtual ~Profile();

    void copyData(Profile* other);
    Bed* createBed(int id = 0, int position = 0);
    Bed* copyBed(Bed* other, int newId = 0, int newPosition = 0);
    Bed* getBedById(int id);
    Bed* getBedByPosition(int position);

    qreal getScaleFactor();
    qreal getScaledHeight();

    int getBedCount() {
        return _beds.size();
    }
    void moveBedUp(Bed* b);
    void moveBedDown(Bed* b);
    void deleteBed(Bed* b);
    void deleteBedsAbove(Bed* b);
    void deleteBedsBelow(Bed* b);
    void splitAtBed(Bed* b);

    QList<Bed*>::iterator getFirstBed() {
        return _beds.begin();
    }

    QList<Bed*>::iterator getLastBed() {
        return _beds.end();
    }

    QString makeToolTipText(const bool withDatasetName = false);

    int getHeightInMillimetres();

    void setMaxSymbolSize(int s) {
        _maxSymbolSize = s;
    }

    int getMaxSymbolSize() {
        return _maxSymbolSize;
    }

    void setScale(int s) {
        _scale = s;
    }

    int getScale() const {
        return _scale;
    }

    void setCellSize(int s) {
        _cellSize = s;
    }

    int getCellSize() const {
        return _cellSize;
    }

    LengthMeasurement* getBigMarksDistance() {
        return _bigMarksDistance;
    }

    LengthMeasurement* getSmallMarksDistance() {
        return _smallMarksDistance;
    }

    void setLegendColumns(int c) {
        _legendColumns = c;
    }

    int getLegendColumns() {
        return _legendColumns;
    }

    Sample* createSample(int id = 0);
    Sample* getSample(int id);
    QList<Sample*>::iterator getFirstSample();
    QList<Sample*>::iterator getLastSample();
    void deleteSample(Sample* s);
    int getSampleCount();

    Image* createImage(int id = 0);
    Image* getImage(int id);
    QList<Image*>::iterator getFirstImage();
    QList<Image*>::iterator getLastImage();
    void deleteImage(Image* s);
    int getImageCount();

    void importBedsFromCsvFile();

    void setShowCustomSymbols(bool b) {
        _showCustomSymbols = b;
    }

    void setShowHeight(bool b) {
        _showHeight = b;
    }

    void setShowBedNumbers(bool b) {
        _showBedNumbers = b;
    }

    void setShowLithology(bool b) {
        _showLithology = b;
    }

    void setShowBeddingType(bool b) {
        _showBeddingType = b;
    }

    void setShowTopBoundaryType(bool b) {
        _showTopBoundaryType = b;
    }

    void setShowFossils(bool b) {
        _showFossils = b;
    }

    void setShowSedimentStructures(bool b) {
        _showSedimentStructures = b;
    }

    void setShowGrainSize(bool b) {
        _showGrainSize = b;
    }

    void setShowNotes(bool b) {
        _showNotes = b;
    }

    void setShowColor(bool b) {
        _showColor = b;
    }

    void setShowFacies(bool b) {
        _showFacies = b;
    }

    void setShowLithologicalUnit(bool b) {
        _showLithologicalUnit = b;
    }

    void setShowOutcropQuality(bool b) {
        _showOutcropQuality = b;
    }

    void setShowHeightMarks(bool b) {
        _showHeightMarks = b;
    }

    bool getShowHeight() const {
        return _showHeight;
    }

    bool getShowBedNumbers() const {
        return _showBedNumbers;
    }

    bool getShowLithology() const {
        return _showLithology;
    }

    bool getShowBeddingType() const {
        return _showBeddingType;
    }

    bool getShowTopBoundaryType() const {
        return _showTopBoundaryType;
    }

    bool getShowFossils() const {
        return _showFossils;
    }

    bool getShowSedimentStructures() const {
        return _showSedimentStructures;
    }

    bool getShowGrainSize() const {
        return _showGrainSize;
    }

    bool getShowCustomSymbols() const {
        return _showCustomSymbols;
    }

    bool getShowNotes() const {
        return _showNotes;
    }

    bool getShowColor() const {
        return _showColor;
    }

    bool getShowFacies() const {
        return _showFacies;
    }

    bool getShowLithologicalUnit() const {
        return _showLithologicalUnit;
    }

    bool getShowOutcropQuality() const {
        return _showOutcropQuality;
    }

    bool getShowHeightMarks() const {
        return _showHeightMarks;
    }

    bool hasDefaultUnit() {
        return 0 != _defaultUnit;
    }

    void setDefaultUnit(LengthUnit* u) {
        _defaultUnit = u;
    }

    LengthUnit* getDefaultUnit() const {
        return _defaultUnit;
    }

private:
    void renumberBeds();

    int _lastBedId;
    int _lastSampleId;
    int _lastImageId;

    int _maxSymbolSize;
    int _scale;
    int _cellSize;
    LengthMeasurement* _bigMarksDistance;
    LengthMeasurement* _smallMarksDistance;
    int _legendColumns;
    LengthUnit* _defaultUnit;

    bool _showHeight;
    bool _showBedNumbers;
    bool _showLithology;
    bool _showBeddingType;
    bool _showTopBoundaryType;
    bool _showFossils;
    bool _showSedimentStructures;
    bool _showGrainSize;
    bool _showCustomSymbols;
    bool _showNotes;
    bool _showColor;
    bool _showFacies;
    bool _showLithologicalUnit;
    bool _showOutcropQuality;
    bool _showHeightMarks;

    QList<Bed*> _beds;
    QList<Sample*> _samples;
    QList<Image*> _images;
};

#endif	/* _PROFILE_H */

