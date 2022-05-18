from django import template

register = template.Library()

@register.filter
def email_to_link(email_string):
    return f"<a href='mailto:{email_string}'>{email_string}</a>"

