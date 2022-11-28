import pytest

from comments.dao.commnets_dao import CommentsDao
from comments.model import Comment
from utils.main import get_comment_path

@pytest.fixture(scope='module')
def comments_dao():
    return CommentsDao('.' + get_comment_path())


class TestCommentsDao:

    def test_get_all(self, comments_dao: CommentsDao):
        comments  = comments_dao.get_all()

        assert type(comments) is list, "uncorrect return type"
        assert len(comments), 'Unexpected empty array'
        assert all([type(c) is Comment for c in comments]), 'commnets element not instance of Comment model'
        
    def test_get_post_by_id(self, comments_dao: CommentsDao):
        comments = comments_dao.get_comments_by_post_id(1)

        assert type(comments) is list, 'uncorrect return type'
        assert len(comments), 'Unexpected empty array'

    def test_get_post_by_id_with_unexist_id(self, comments_dao: CommentsDao):
        comments = comments_dao.get_comments_by_post_id(-1)
        
        assert type(comments) is list, 'uncorrect return type'
        assert len(comments) == 0, 'Unexpected length of array'
    
    def test_get_post_by_id_typerror(self, comments_dao: CommentsDao):
        with pytest.raises(TypeError):
            comments_dao.get_comments_by_post_id('asdasd') #type: ignore