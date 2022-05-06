"""IntexSpaQuery"""
import time
import json

from .intex_spa_status import IntexSpaStatus

REQUEST: dict = {
    "status": "8888060FEE0F01",
    "power": "8888060F014000",
    "filter": "8888060F010004",
    "heater": "8888060F010010",
    "jets": "8888060F011000",
    "bubbles": "8888060F010400",
    "sanitizer": "8888060F010001",
    "preset_temp": "8888050F0C",
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
    response_status : IntexSpaStatus
        The rendered response data, as int
    """

    def __init__(self, intent: str, preset_temp: int = None):
        """Init."""
        self.intex_timestamp = str(int(time.time() * 10000))

        self.request: str = REQUEST[intent]
        if intent == "preset_temp":
            self.request = self.request + hex(preset_temp)[2:].upper()

        self.response_status: IntexSpaStatus

    @property
    def request_bytes(self) -> bytes:
        """The full message request to send, as expected by Intex Spa protocol, encoded as bytes"""
        request_dict = {
            "data": self.request + checksum_as_str(self.request),
            "sid": self.intex_timestamp,
            "type": 1,
        }
        return json.dumps(request_dict).encode()

    def render_response_status(self, received_bytes: bytes) -> IntexSpaStatus:
        """
        Render response data from `received_bytes` from Intex Spa wifi module

        Parameters
        ----------
        received_bytes : bytes
            The response received from Intex Spa wifi module, as bytes

        Returns
        ----------
        response_status : IntexSpaStatus
            The new status, rendered from the spa response
        """
        response = json.loads(received_bytes.decode())

        # Timestamp correspondance check
        assert response["sid"] == self.intex_timestamp
        assert response["result"] == "ok"
        assert response["type"] == 2

        # Checksum comparison
        checksum_calculated = checksum_as_int(response["data"][:-2])
        checksum_in_response = int("0x" + response["data"][-2:], 16)
        assert checksum_calculated == checksum_in_response

        response_as_int = int("0x" + response["data"], 16)
        self.response_status = IntexSpaStatus(response_as_int)

        return self.response_status
