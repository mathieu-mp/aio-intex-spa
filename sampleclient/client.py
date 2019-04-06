"""Client."""
import datetime


class Client:
    """Client class"""

    def __init__(self, username, password):
        """Init."""
        self.username = username
        self.password = password
        self.something = False

    def get_data(self):
        """Return sample data."""
        data = {
            "username": self.username,
            "password": self.password,
            "data": {
                "time": datetime.time(),
                "static": "Some sample static text.",
                "bool_on": True,
                "bool_off": False,
                "none": None,
            },
        }
        return data

    async def async_get_data(self):
        """Return sample data."""
        data = {
            "username": self.username,
            "password": self.password,
            "data": {
                "time": datetime.time(),
                "static": "Some sample static text.",
                "bool_on": True,
                "bool_off": False,
                "none": None,
            },
        }
        return data

    def change_something(self, something: bool = None):
        """Change something."""
        self.something = something

    async def async_change_something(self, something: bool = None):
        """Change something."""
        self.something = something
