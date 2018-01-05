import rules
from insaction.rules import is_author, is_author_group, is_editor, is_manager


rules.add_perm('website.add_news',
               is_author_group | is_editor | is_manager |
               rules.is_superuser)
rules.add_perm('website.change_news',
               is_author | is_editor | is_manager |
               rules.is_superuser)
rules.add_perm('website.delete_news',
               is_author | is_editor | is_manager |
               rules.is_superuser)
