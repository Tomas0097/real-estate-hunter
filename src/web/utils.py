from django.conf import settings


def show_toolbar(request):
    # taken from the original package callback
    # see: debug_toolbar.middleware.show_toolbar
    if request.META.get("REMOTE_ADDR", None) not in settings.INTERNAL_IPS:
        return False

    SHOW_DJANGO_DEBUG_TOOLBAR = (
        settings.SHOW_DJANGO_DEBUG_TOOLBAR and settings.DEBUG
    )

    return SHOW_DJANGO_DEBUG_TOOLBAR
