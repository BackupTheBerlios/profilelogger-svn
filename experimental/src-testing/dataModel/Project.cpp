#include "Project.h"

Project::Project(int id, const QString& n, const QString& d)
  : Dataset(id),
    _name(n),
    _description(d)
{}
