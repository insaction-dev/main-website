from django import template
from django.utils import safestring
import markdown
import bleach

register = template.Library()


@register.filter(is_safe="True")
def parse_markdown(value):
    return markdown.markdown(
        value,
        extensions=[
            'markdown.extensions.nl2br',
            'markdown.extensions.smarty'
        ]
    )


@register.filter(is_safe=True)
def clean(value):
    return safestring.mark_safe(bleach.clean(
        value,
        tags=['p', 'blockquote', 'i', 'b', 'img', 'a', 'em', 'strong']
    ))


@register.simple_tag
def has_perm(perm, user, obj=None):
    return user.has_perm(perm, obj)
