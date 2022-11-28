import pytest
from flask.testing import FlaskClient
from app.posts.model import Post

API_PREFIX = '/api/v1'

post = Post(1, 'a', 'b', 'c', 'd',1, 1)

class TestApi:

    def test_get_posts(self, test_client: FlaskClient):
        response = test_client.get(API_PREFIX + '/posts/')

        data = response.json

        assert response.status_code == 200, 'Unexpected response status code'
        assert type(data) is list, 'Exptected list type'
        assert len(data), 'Unexpected empty list'

    def test_get_post(self, test_client: FlaskClient):
        response = test_client.get(API_PREFIX + "/posts/1/")

        data = response.json

        assert response.status_code == 200, 'Unexpected response status code'
        assert type(data) is dict, 'Exptected dict type'
        assert set(data.keys()) == post.get_keys(), 'Unexpected keys'

    def test_get_post_unexist(self, test_client: FlaskClient):
        response = test_client.get(API_PREFIX + '/posts/990000/')

        data = response.json
        
        assert response.status_code == 200, 'Unexpected response status code'
        assert type(data) is dict, 'Exptected dict type'
        assert set(data.keys()) == {"message"}, 'Unexpected data'

