from model.project import Project


def test_add_project(app, db):
    old_projects = db.get_project_list()
    project = Project(name=app.project.random_name(10),
                               description="text")
    app.project.create(project)
    new_projects = db.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)