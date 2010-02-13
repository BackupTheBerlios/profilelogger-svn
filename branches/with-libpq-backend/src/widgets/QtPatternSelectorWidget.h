/* 
 * File:   QtPatternSelectorWidget.h
 * Author: jolo
 *
 * Created on 19. Dezember 2009, 11:36
 */

#ifndef _QTPATTERNSELECTORWIDGET_H
#define	_QTPATTERNSELECTORWIDGET_H

#include <QComboBox>
#include <QMap>
#include <QBrush>
#include <QPixmap>

class QtPatternSelectorWidget : public QComboBox {
    Q_OBJECT
public:
    QtPatternSelectorWidget(QWidget* p);
    virtual ~QtPatternSelectorWidget();
    virtual void setPattern(Qt::BrushStyle s);
    
signals:
    void patternChanged(Qt::BrushStyle s);

public slots:
    virtual void slotCurrentIndexChanged(int idx);

private:
    void setupPatterns();
    QMap<int, Qt::BrushStyle> _brushes;
};

#endif	/* _QTPATTERNSELECTORWIDGET_H */

