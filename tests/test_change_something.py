"""Test change_something"""
USERNAME = "test_username"
PASSWORD = "test_password"


def test_change_something_true():
    """Test hange_something_true."""
    from sampleclient.client import Client

    client = Client(USERNAME, PASSWORD)
    print(client.something)
    client.change_something(False)
    print(client.something)


def test_change_something_false():
    """Test change_something_false."""
    from sampleclient.client import Client

    client = Client(USERNAME, PASSWORD)
    print(client.something)
    client.change_something(False)
    print(client.something)


test_change_something_true()
test_change_something_false()
