"""IntexSpaStatus"""
import logging

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
    def current_temp(self) -> int:
        """Current temperature of the water, expressed in `unit`"""
        return (self._raw_status >> 88) & 0xFF

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
        }

    def __repr__(self) -> str:
        """
        Represent IntexSpaStatus main status attributes
        """
        return repr(self.as_dict())
