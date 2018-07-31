from django import template
from django.template.defaultfilters import stringfilter
from django.utils import safestring
import markdown
import bleach
from bleach_whitelist.bleach_whitelist import markdown_tags, markdown_attrs
from blog_embed.extensions import LinksToEmbedExtension

register = template.Library()


@register.filter
def parse_markdown(value):
    return markdown.markdown(
        value,
        extensions=[
            'markdown.extensions.nl2br',
            'markdown.extensions.smarty',
            LinksToEmbedExtension()
        ],
        safe_mode='replace'
    )


@register.filter
@stringfilter
def clean(value):
    cleaned_html = bleach.clean(
        value,
        tags=['iframe', *markdown_attrs, *markdown_tags],
        attributes={
            '*': ['class', 'style'],
            'img': ['alt', 'width', 'height'],
            'iframe': ['width', 'height', 'src', 'allowFullscreen', 'frameborder']
        }
    )
    
    return safestring.mark_safe(cleaned_html)


@register.simple_tag
def has_perm(perm, user, obj=None):
    return user.has_perm(perm, obj)
