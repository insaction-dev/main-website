from django import template
from django.template.defaultfilters import stringfilter
from django.utils import safestring
import markdown
import bleach
from bleach_whitelist.bleach_whitelist import markdown_tags, markdown_attrs
from markdown import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree

register = template.Library()


class HTMLRendererMixin:
    def render(self, *args, **kwargs):
        pass


class IFrameRendererMixin(HTMLRendererMixin):
    def render(self, url, width, height):
        iframe = etree.Element('iframe')
        iframe.set('width', width)
        iframe.set('height', height)
        iframe.set('src', url)
        iframe.set('allowfullscreen', 'true')
        iframe.set('frameborder', '0')

        container = etree.Element('div')
        container.set('class', 'video-container')
        container.insert(0, iframe)
        return container


class Vimeo(Pattern, IFrameRendererMixin):
    def handleMatch(self, m):
        url = '//player.vimeo.com/video/%s' % m.group('vimeoid')
        return self.render(url, '1280', '720')


class Youtube(Pattern, IFrameRendererMixin):
    def handleMatch(self, m):
        url = '//www.youtube.com/embed/%s' % m.group('youtubeid')
        return self.render(url, '1280', '720')


class LinksToEmbedExtension(Extension):
    def add_inline(self, md, name, klass, re):
        pattern = klass(re)
        pattern.md = md
        pattern.ext = self
        md.inlinePatterns.add(name, pattern, "<reference")

    def extendMarkdown(self, md, md_globals):
        self.add_inline(md, 'vimeo', Vimeo,
                        r'([^(]|^)http://(www.|)vimeo\.com/(?P<vimeoid>\d+)\S*')
        self.add_inline(md, 'youtube', Youtube,
                        r'([^(]|^)https?://www\.youtube\.com/watch\?\S*v=(?P<youtubeid>\S[^&/]+)')
        self.add_inline(md, 'youtube_short', Youtube,
                        r'([^(]|^)https?://youtu\.be/(?P<youtubeid>\S[^?&/]+)?')


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
            '*': ['class'],
            'iframe': ['width', 'height', 'src', 'allowFullscreen', 'frameborder']
        }
    )
    
    return safestring.mark_safe(cleaned_html)


@register.simple_tag
def has_perm(perm, user, obj=None):
    return user.has_perm(perm, obj)
