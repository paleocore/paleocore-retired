from django import template

register = template.Library()

colors = ['FFBFA2', 'D488E8', '87C6FF', 'E8DE8B', 'A2FFBC']

@register.filter(name='colorPicker')
def colorPicker(value):
    """Return hex color code for hard-coded theme"""
    return '#' + colors[value % len(colors)-1]