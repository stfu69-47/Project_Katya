from django import template
import places.utils
from places.models import *
from places.utils import mainmenu
import places.views as views


register = template.Library()


@register.simple_tag()
def get_mainmenu():
    return mainmenu