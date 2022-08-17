# Define test fixtures here.
import pytest

@pytest.fixtures
def client():
    address = '123 main st chicago il'
    return address