/*
 * File:   ImageEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#ifndef _IMAGEEDITORDIALOG_H
#define	_IMAGEEDITORDIALOG_H

#include "DatasetWithFileNameEditorDialog.h"

class Image;

class QtPatternSelectorWidget;

class ImageEditorDialog : public DatasetWithFileNameEditorDialog {
    Q_OBJECT
public:
    ImageEditorDialog(QWidget* parent, Image* p);
    virtual ~ImageEditorDialog();
    Image* getImage();
};

#endif	/* _IMAGEEDITORDIALOG_H */
