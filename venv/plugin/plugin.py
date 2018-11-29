""""Module with fixtures for Investment API"""

import pytest
from packeges.http_client.http_client1 import HttpClient


@pytest.fixture(scope="function")
def http_client():
    """Client to work whith HTTP requests"""
    return  HttpClient()