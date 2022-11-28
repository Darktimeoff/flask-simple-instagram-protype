import pytest
from flask.testing import FlaskClient


class TestPosts:
    def test_page_index(self, test_client: FlaskClient):
        response = test_client.get("/")

        assert response.status_code == 200, 'Unexpected status code'
