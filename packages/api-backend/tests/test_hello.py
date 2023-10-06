"""Hello unit test module."""

from api_backend.hello import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello api-backend"
