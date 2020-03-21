from main.utils import get_file_name


def photo_upload_to(instance, filename):
    path = f'services/{instance.slug}'
    return get_file_name(path, filename)
