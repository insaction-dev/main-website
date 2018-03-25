from django import template
from django.utils import safestring
import markdown
import bleach

register = template.Library()


@register.filter(name='markdownify')
def markdownify(value):
    return markdown.markdown(
        value,
        extensions=[
            'markdown.extensions.nl2br',
            'markdown.extensions.smarty'
        ]
    )


@register.filter(name='clean')
def clean(value):
    return safestring.mark_safe(bleach.clean(
        value,
        tags=['p', 'blockquote', 'i', 'b', 'img', 'a']
    ))


@register.simple_tag
def has_perm(perm, user, obj=None):
    return user.has_perm(perm, obj)
