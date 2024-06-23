from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f"/media/{path}"
    else:
        return f"#"


@register.filter()
def name_filter(name):
    if len(name) > 100:
        return f"{name[0:99]}..."
    else:
        return name
