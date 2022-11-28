import pytest
from flask.testing import FlaskClient


class TestPosts:
    def test_page_index(self, test_client: FlaskClient):
        response = test_client.get("/")

        assert response.status_code == 200, 'Unexpected status code'

    def test_page_post(self, test_client: FlaskClient):
        response = test_client.get("/posts/1/")

        assert response.status_code == 200, 'Unexpected status code'
    
    def test_page_post_unexisted(self, test_client: FlaskClient):
        response = test_client.get("/posts/99999999999/")

        assert response.status_code == 200, 'Unexpected status code'

    def test_page_post_uncorrect_id_type(self, test_client: FlaskClient):
        response = test_client.get("/posts/asda/")

        assert response.status_code == 404, 'Unexpected status code'
    
    def test_page_search(self, test_client: FlaskClient):
        response = test_client.get("/search/?s=Утром")

        assert response.status_code == 200, 'Unexpected status code'
    
    def test_page_search_empty_result(self, test_client: FlaskClient):
        response = test_client.get("/search/?s=123123123123")

        assert response.status_code == 200, 'Unexpected status code'
    
    def test_page_search_empty_search(self, test_client: FlaskClient):
        response = test_client.get("/search/")

        assert response.status_code == 200, 'Unexpected status code'

    def test_user_feed(self, test_client):
        response = test_client.get("/users/leo/")

        assert response.status_code == 200, 'Unexpected status code'

    def test_user_feed_unexist(self, test_client):
        response = test_client.get("/users/asdasdasdasd/")

        assert response.status_code == 200, 'Unexpected status code'