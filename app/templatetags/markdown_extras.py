# markdown_extras.py

import markdown as md  # Import the Markdown library
from django import template
from django.utils.safestring import mark_safe  # Important for security/rendering HTML

register = template.Library()


@register.filter(name="markdownify")  # Register the filter with the name 'markdownify'
def markdown_filter(value):
    """
    Converts Markdown text to HTML.
    Usage: {{ my_markdown_variable|markdownify }}
    """
    # Convert markdown text to HTML
    html = md.markdown(
        value, extensions=["fenced_code", "codehilite", "tables", "nl2br"]
    )  # Added common extensions

    # Mark the output as safe to prevent Django's auto-escaping
    return mark_safe(html)


# --- Optional: Add Sanitization for User-Generated Content (HIGHLY Recommended) ---
# If the Markdown comes from untrusted users, you MUST sanitize the HTML
# to prevent Cross-Site Scripting (XSS) attacks. Install bleach: pip install bleach
#
# import bleach
#
# @register.filter(name='safe_markdownify')
# def safe_markdown_filter(value):
#     """
#     Converts Markdown text to HTML and sanitizes it using Bleach.
#     Usage: {{ user_generated_markdown|safe_markdownify }}
#     """
#     # Define allowed tags, attributes, etc. (customize as needed)
#     allowed_tags = ['p', 'strong', 'em', 'h1', 'h2', 'h3', 'ul', 'ol', 'li',
#                     'code', 'pre', 'blockquote', 'a', 'img', 'table', 'thead',
#                     'tbody', 'tr', 'th', 'td']
#     allowed_attrs = {
#         '*': ['class'], # Allow class attribute on any tag
#         'a': ['href', 'title'],
#         'img': ['src', 'alt', 'title', 'width', 'height'],
#     }
#
#     # Convert markdown to HTML
#     html = md.markdown(value, extensions=['fenced_code', 'codehilite', 'tables', 'nl2br'])
#
#     # Sanitize the generated HTML
#     clean_html = bleach.clean(html, tags=allowed_tags, attributes=allowed_attrs, strip=True)
#
#     return mark_safe(clean_html)
