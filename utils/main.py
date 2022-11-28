from os import environ


def get_post_path():
    return environ.get('POST_PATH', '')


def get_comment_path():
    return environ.get('COMMENT_PATH', '')


def get_bookmark_path():
    return environ.get('BOOKMARK_PATH', '')
