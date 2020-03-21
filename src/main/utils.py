import os


def get_file_extension(filename):
    filename, file_extension = os.path.splitext(filename)
    return file_extension


def get_file_name(path, filename):
    extension = get_file_extension(filename)
    return f'{path}{extension}'
