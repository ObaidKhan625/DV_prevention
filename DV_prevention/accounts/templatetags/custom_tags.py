from django import template

register = template.Library()

@register.simple_tag
def get_session_item(dictionary, key):
    return dictionary.get(key)