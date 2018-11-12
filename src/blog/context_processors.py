from django.conf import settings


def site_info(request):
    return {
        'AUTHOR_NAME': settings.AUTHOR_NAME,
        'SITE_NAME': settings.SITE_NAME,
        'SITE_URL': settings.SITE_URL,
    }
