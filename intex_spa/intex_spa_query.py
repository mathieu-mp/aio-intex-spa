"""IntexSpaQuery"""
import time
import json

TYPE: dict = {
    "command": 1,
    "status": 2,
    "info": 3,
}

COMMAND: dict = {
    "status": {
        "request": "8888060FEE0F01",
        "type": TYPE["command"],
    },
    "power": {
        "request": "8888060F014000",
        "type": TYPE["command"],
    },
    "filter": {
        "request": "8888060F010004",
        "type": TYPE["command"],
    },
    "heater": {
        "request": "8888060F010010",
        "type": TYPE["command"],
    },
    "jets": {
        "request": "8888060F011000",
        "type": TYPE["command"],
    },
    "bubbles": {
        "request": "8888060F010400",
        "type": TYPE["command"],
    },
    "sanitizer": {
        "request": "8888060F010001",
        "type": TYPE["command"],
    },
    "preset_temp": {
        "request": "8888050F0C",
        "type": TYPE["command"],
    },
    "info": {
        "request": "",
        "type": TYPE["info"],
    },
}


def checksum_as_int(data: str) -> int:
    """Return integer checksum for the given data, as expected by Intex Spa protocol"""
    calculated_checksum = 0xFF
    for index in range(0, len(data), 2):
        calculated_checksum = calculated_checksum - (
            int("0x" + data[index : index + 2], 16)
        )
    return calculated_checksum % 0xFF


def checksum_as_str(data: str) -> str:
    """Return string checksum for the given data, as expected by Intex Spa protocol"""
    # Return checksum as a hex string without 0x prefix
    return hex(checksum_as_int(data) % 0xFF)[2:].upper()


class IntexSpaQuery:
    """
    Class to manage one application-layer query with Intex Spa wifi module

    Manages encoding and decoding of one request and its response messages

    Attributes
    -------
    intex_timestamp : str
        The 10th of milliseconds timestamp, as expected by Intex Spa protocol
    request : str
        The request data to send, as expected by Intex Spa protocol
    request_bytes : bytes
        The full message request to send, as expected by Intex Spa protocol, encoded as bytes
    response_data
        The rendered response data
    """

    def __init__(self, intent: str, preset_temp: int = None):
        """Init."""
        self.intex_timestamp = str(int(time.time() * 10000))

        self.request: str = COMMAND[intent]["request"]
        if intent == "preset_temp":
            self.request = self.request + hex(preset_temp)[2:].upper()

        self.type: int = COMMAND[intent]["type"]

        self.response_data: int

    @property
    def request_bytes(self) -> bytes:
        """The full message request to send, as expected by Intex Spa protocol, encoded as bytes"""
        request_dict = {
            "data": self.request + checksum_as_str(self.request),
            "sid": self.intex_timestamp,
            "type": self.type,
        }
        return json.dumps(request_dict).encode()

    def render_response_data(self, received_bytes: bytes):
        """
        Render response data from `received_bytes` from Intex Spa wifi module

        Parameters
        ----------
        received_bytes : bytes
            The response received from Intex Spa wifi module, as bytes

        Returns
        ----------
        response_data : int
            The new data, rendered from the spa response
        """
        response = json.loads(received_bytes.decode())

        # Timestamp correspondance check
        assert response["sid"] == self.intex_timestamp
        assert response["result"] == "ok"

        if self.type == TYPE["command"]:
            assert response["type"] == TYPE["status"]

            # Checksum comparison
            checksum_calculated = checksum_as_int(response["data"][:-2])
            checksum_in_response = int("0x" + response["data"][-2:], 16)
            assert checksum_calculated == checksum_in_response

            self.response_data = int("0x" + response["data"], 16)

        elif self.type == TYPE["info"]:
            assert response["type"] == TYPE["info"]
            data = json.loads(response["data"])
            assert data["dtype"] == "spa"

            self.response_data = {
                "ip": data["ip"],
                "uid": data["uid"],
                "dtype": data["dtype"],
            }

        return self.response_data
