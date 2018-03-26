from __future__ import absolute_import
import rules


@rules.predicate
def is_author(user, authored_object):
    print("Testing {} for authorship of {}".format(user, authored_object))
    if authored_object is None:
        return None

    return user.pk == authored_object.author.pk


is_manager = rules.is_group_member('manager')
is_editor = rules.is_group_member('editor') | is_manager
is_author_group = rules.is_group_member('author') | is_editor
