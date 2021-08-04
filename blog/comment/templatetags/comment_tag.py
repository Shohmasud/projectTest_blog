from django import template
from django.template import Library
from comment.models import Comments
register = template.Library()
@register.filter(name='text')
def text(num):
        pk2 = Comments.objects.get(pk=num).parent
        if pk2 is None:
            return True
        return False

@register.filter(name='pk_obj')
def pk_obj(object):
        result = Comments.objects.get(pk=object)
        return result