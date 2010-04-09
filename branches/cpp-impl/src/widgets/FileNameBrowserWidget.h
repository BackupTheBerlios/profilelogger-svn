/* 
 * File:   FileNameBrowserWidget.h
 * Author: jolo
 *
 * Created on 17. Dezember 2009, 13:40
 */

#ifndef _FILENAMEBROWSERWIDGET_H
#define	_FILENAMEBROWSERWIDGET_H

#include <QWidget>

class QLineEdit;
class QPushButton;
class QSvgWidget;

class FileNameBrowserWidget : public QWidget {
    Q_OBJECT
public:
    FileNameBrowserWidget(QWidget* p, const QString& filter = QObject::tr("SVG Files *.svg *.SVG"));
    
    virtual ~FileNameBrowserWidget();

signals:
    void fileNameChanged(const QString& s);

public slots:
    void setDefaultPath(const QString& s);
    void setFileName(const QString& s);

protected slots:
       void slotBrowse();
       void slotRemoveFileName();

private:
    QString _defaultPath;
    QString _filter;
    QLineEdit* _displayW;
    QPushButton* _browseW;
    QPushButton* _removeW;
    QSvgWidget* _previewW;
};

#endif	/* _FILENAMEBROWSERWIDGET_H */

