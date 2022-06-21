"""IntexSpaStatus"""
import logging
import typing

_LOGGER = logging.getLogger(__name__)


class IntexSpaStatus:
    """
    Class to represent Intex Spa status

    Attributes
    -------
    _raw_status : int
        The raw integer-encoded status data, as received from the spa
    power : bool
    filter : bool
    heater : bool
    jets : bool
    bubbles : bool
    sanitizer : bool
    unit : str
    current_temp : int
    preset_temp : int
    """

    @property
    def power(self) -> bool:
        """Power state of the spa"""
        return bool((self._raw_status >> 104) & 0b1)

    @property
    def filter(self) -> bool:
        """State of the filter function"""
        return bool((self._raw_status >> 105) & 0b1)

    @property
    def heater(self) -> bool:
        """State of the heater function"""
        return bool((self._raw_status >> 106) & 0b1)

    @property
    def jets(self) -> bool:
        """State of the jets function"""
        return bool((self._raw_status >> 107) & 0b1)

    @property
    def bubbles(self) -> bool:
        """State of the bubbles function"""
        return bool((self._raw_status >> 108) & 0b1)

    @property
    def sanitizer(self) -> bool:
        """State of sanitizer function"""
        return bool((self._raw_status >> 109) & 0b1)

    @property
    def unit(self) -> str:
        """Temperature measurement unit
        *"°C" for Celsius*
        *"°F" for Farenheit*
        """
        if self.preset_temp <= 40:
            return "°C"
        else:
            return "°F"

    @property
    def current_temp(self) -> typing.Union[int, bool]:
        """Current temperature of the water, expressed in `unit`"""
        raw_current_temp = (self._raw_status >> 88) & 0xFF

        # If current_temp encodes a temperature, return the temperature
        if raw_current_temp < 181:
            return raw_current_temp
        # Else if current_temp encodes an error (E81, ...), return False
        else:
            return False

    @property
    def error_code(self) -> typing.Union[int, bool]:
        """Current error code of the spa"""
        raw_current_temp = (self._raw_status >> 88) & 0xFF

        # If current_temp encodes an error (E81, ...), return the error code
        if raw_current_temp >= 181:
            error_no = raw_current_temp - 100
            return f"E{error_no}"
        # Else if current_temp encodes a temperature, return False
        else:
            return False

    @property
    def preset_temp(self) -> int:
        """Preset temperature of the water, expressed in `unit`"""
        return (self._raw_status >> 24) & 0xFF

    def __init__(self, raw_status: int = None):
        """
        Initialize IntexSpaStatus class

        Parameters
        ----------
        raw_status : int, optional
            The raw response data received from the spa
        """
        if raw_status is not None:
            self.update(raw_status)

    def update(self, raw_status: int):
        """
        Update the raw_status

        Parameters
        ----------
        raw_status : int
            The raw response data received from the spa
        """
        self._raw_status = raw_status
        _LOGGER.debug("Spa status: '%s'", self)

    def as_dict(self) -> dict:
        """
        Return main status attributes only, as dict

        Returns
        -------
        status_attributes : dict
            IntexSpaStatus main status attributes as dict
        """
        return {
            "power": self.power,
            "filter": self.filter,
            "heater": self.heater,
            "jets": self.jets,
            "bubbles": self.bubbles,
            "sanitizer": self.sanitizer,
            "unit": self.unit,
            "current_temp": self.current_temp,
            "preset_temp": self.preset_temp,
            "error_code": self.error_code,
        }

    def __repr__(self) -> str:
        """
        Represent IntexSpaStatus main status attributes
        """
        return repr(self.as_dict())
