from django import template
import markdown


register = template.Library()

@register.filter
def md_to_html(value):
    """Converts markdown text to HTML."""
    return markdown.markdown(value)