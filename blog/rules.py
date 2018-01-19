import rules
from insaction.rules import is_author, is_author_group, is_editor, is_manager

rules.add_perm('blog', rules.always_allow)
rules.add_perm('blog.create_article',
               is_author_group |
               rules.is_superuser)
rules.add_perm('blog.change_article',
               is_author | is_editor |
               rules.is_superuser)
rules.add_perm('blog.delete_article',
               is_author | is_manager |
               rules.is_superuser)

rules.add_perm('blog.create_category',
               is_manager | rules.is_superuser)
rules.add_perm('blog.change_category',
               is_manager | rules.is_superuser)
rules.add_perm('blog.delete_category',
               is_manager | rules.is_superuser)
