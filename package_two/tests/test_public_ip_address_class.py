import json
import pytest

from unittest.mock import patch

from package_two.module_two import PublicIPAddress
from package_two.module_two import PublicIPAddressError


class Response():
    def __init__(self, status_code=200, text=None):
        self.status_code = status_code
        self.text = text


@pytest.fixture
def public_ip_address_getter():
    yield PublicIPAddress()

@patch('requests.get')
def test_successful_case(mocked_get_method, public_ip_address_getter):
    mock_response = Response(200)
    mock_response.text = json.dumps({
        "ip": "12.12.12.12"
    })

    mocked_get_method.return_value = mock_response

    public_ip_address_getter = PublicIPAddress()
    public_ip_address_getter.get_public_ip_address()
    assert public_ip_address_getter.ip_address == "12.12.12.12"
