from model.issue import Issue


def test_modify_issue(app):
    app.issue.fill_issue_form(Issue(name="",description="",product_id="1",day="1",month="2",year="4"))