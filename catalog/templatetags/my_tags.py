from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    #/products/Без_названия.jpg
    if path:
        return f"/media/{path}"
    else:
        return f"#"
