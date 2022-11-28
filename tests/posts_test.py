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