"""Test get_data"""
USERNAME = "test_username"
PASSWORD = "test_password"


def test_get_data():
    """Test get_data."""
    from sampleclient.client import Client

    client = Client(USERNAME, PASSWORD)
    print(client.get_data())


test_get_data()
