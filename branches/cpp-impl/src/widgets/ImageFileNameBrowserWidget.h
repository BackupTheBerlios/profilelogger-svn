/*
 * File:   ImageFileNameBrowserWidget.h
 * Author: jolo
 *
 * Created on 17. Dezember 2009, 13:40
 */

#ifndef _IMAGEFILENAMEBROWSERWIDGET_H
#define	_IMAGEFILENAMEBROWSERWIDGET_H

#include <QWidget>

class QLineEdit;
class QPushButton;
class QLabel;

class ImageFileNameBrowserWidget : public QWidget {
    Q_OBJECT
public:
    ImageFileNameBrowserWidget(QWidget* p, const QString& filter = QObject::tr("SVG Files *.svg *.SVG"));

    virtual ~ImageFileNameBrowserWidget();

signals:
    void fileNameChanged(const QString& s);

public slots:
    void setDefaultPath(const QString& s);
    void setImageFileName(const QString& s);

protected slots:
       void slotBrowse();
       void slotRemoveImageFileName();

private:
    QString _defaultPath;
    QString _filter;
    QLineEdit* _displayW;
    QPushButton* _browseW;
    QPushButton* _removeW;
    QLabel* _previewW;
};

#endif	/* _IMAGEFILENAMEBROWSERWIDGET_H */

