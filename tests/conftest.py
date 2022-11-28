import pytest

from run import app

@pytest.fixture()
def test_client():
    app.testing = True
    return app.test_client()