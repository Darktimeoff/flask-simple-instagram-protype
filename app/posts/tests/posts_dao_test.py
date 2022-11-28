import pytest
from app.posts.dao.posts_dao import PostsDao
from app.posts.model import Post
from utils.main import get_post_path


@pytest.fixture(scope='module')
def posts_dao():
    return PostsDao(get_post_path())


class TestPostsDao:
    def test_get_all(self, posts_dao: PostsDao):
        posts = posts_dao.get_all()

        assert type(posts) is list, "Posts is uncorrect type"
        assert len(posts), "Posts data is empty"

    def test_get_post(self, posts_dao: PostsDao):
        post = posts_dao.get_all()[0]

        assert type(post) is Post, "Post is uncorrect type"
        assert all(post.__dict__.values()), "Post field are empty"

    def test_get_by_user(self, posts_dao: PostsDao):
        posts = posts_dao.get_by_user('leo')

        assert type(posts) is list, "Posts is uncorrect type"
        assert len(posts), "Posts data is empty"

    def test_get_by_user_unexist(self, posts_dao: PostsDao):
        posts = posts_dao.get_by_user('12312312312')

        assert type(posts) is list, "Posts is uncorrect type"
        assert len(posts) == 0, "Posts data is empty"

    def test_get_by_user_typerror(self, posts_dao: PostsDao):
        with pytest.raises(TypeError):
            posts_dao.get_by_user(1)  # type: ignore

    def test_by_pk(self, posts_dao: PostsDao):
        post = posts_dao.get_by_id(1)

        assert type(post) is Post, 'Post is not defined with id 1'

    def test_by_pk_unexist(self, posts_dao: PostsDao):
        post = posts_dao.get_by_id(-1)

        assert post == None, 'Post return uncorrect type with unexist id'

    def test_by_pk_typerror(self, posts_dao: PostsDao):
        with pytest.raises(TypeError):
            posts_dao.get_by_id('sad')  # type: ignore

    def test_search_by_word(self, posts_dao: PostsDao):
        posts = posts_dao.search_by_word('Вышел погулять')

        assert type(posts) is list, 'uncorrect type must be list'
        assert len(posts), 'doesn`t find posts'

    def test_search_by_word_typerror(self, posts_dao: PostsDao):
        with pytest.raises(TypeError):
            posts_dao.search_by_word(1)  # type: ignore
