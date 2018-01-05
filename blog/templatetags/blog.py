from django import template
from django.utils import safestring
import markdown
import bleach

register = template.Library()


@register.filter(name='markdownify')
def markdownify(value):
    return safestring.mark_safe(markdown.markdown(value, extensions=['markdown.extensions.nl2br', 'markdown.extensions.smarty']))


@register.filter(name='clean')
def clean(value):
    return bleach.clean(value)
