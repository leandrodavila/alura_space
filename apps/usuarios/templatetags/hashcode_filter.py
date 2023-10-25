from django import template
from django.contrib.auth.hashers import make_password
from framework.security import UrlSecutity

register = template.Library()

@register.filter(is_safe=True)
def secure_url(url):
    
    hashcode = UrlSecutity.get_url_hashcode(url)
    
    if ("?" in url):
        return f"{url}&{hashcode}"
    else:
        return f"{url}?{hashcode}"