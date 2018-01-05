import rules


@rules.predicate(bind=True)
def is_author(self, user, authored_object):
    print("Testing {} for authorship of {}".format(user, authored_object))
    if authored_object is None:
        return None

    return user == authored_object.user


is_author_group = rules.is_group_member('author')
is_editor = rules.is_group_member('editor')
is_manager = rules.is_group_member('manager')
