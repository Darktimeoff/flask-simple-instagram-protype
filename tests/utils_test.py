import pytest
from utils.main import get_post_path, get_comment_path, get_bookmark_path

class TestMainUtils:
    def test_get_post_path_value(self):
        path = get_post_path()

        assert (type(path) is str and len(path) > 1), 'Path for post data not defined'

    def test_get_comment_path_value(self):
        path = get_comment_path()

        assert (type(path) is str and len(path) > 1), 'Path for comment data not defined'

    def test_get_bookmark_path_value(self):
        path = get_bookmark_path()

        assert (type(path) is str and len(path) > 1), 'Path for bookmark data not defined'