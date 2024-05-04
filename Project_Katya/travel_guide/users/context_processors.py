from places.utils import mainmenu


def get_places_context(request):
    return {'menu': mainmenu}