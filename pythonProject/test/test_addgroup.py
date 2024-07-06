from model.group import Group

def test_addgroup(app):
    app.session.Login("admin", "secret")
    app.group.Creat(Group("sdf", "sdf", "sdf"))
    app.session.Logout()


def test_empty_addgroup(app):
    app.session.Login("admin", "secret")
    app.group.Creat(Group("","",""))
    app.session.Logout()