import pytest

from views.py import AddressParse
from urls.py import address-parse

@pytest.mark.django_db
def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    
    test-address = AddressParse.get(self, client)
    address_string = '123 main st chicago il'
    assert test-address == address_string
    


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    test = AddressParse.parse(self, address_string)
    pytest.fail()
