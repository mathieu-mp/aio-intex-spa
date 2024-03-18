"""Load IntexSpaInfo class."""

import logging

_LOGGER = logging.getLogger(__name__)


class IntexSpaInfo:
    """Hold and expose the info response objects.

    Attributes
    ----------
    dtype : str
        The spa dtype, provided by the spa
    ip : str
        The spa ip, provided by the spa
    uid : str
        The spa uid, provided by the spa

    """

    def __init__(self, raw_info: str = None):
        """Initialize IntexSpaInfo class.

        Parameters
        ----------
        raw_info : int, optional
            The raw response data received from the spa

        """
        if raw_info is not None:
            self.update(raw_info)

    def update(self, raw_info: dict):
        """Update the attributes value.

        Parameters
        ----------
        raw_info : dict
            The response data received from the spa

        """
        self.ip: str = raw_info["ip"]  # pylint: disable=invalid-name
        self.uid: str = raw_info["uid"]
        self.dtype: str = raw_info["dtype"]
        _LOGGER.debug("Spa info: '%s'", self)

    def as_dict(self) -> dict:
        """Return main attributes only, as dict.

        Returns
        -------
        info_attributes : dict
            IntexSpaInfo main attributes as dict

        """
        try:
            return {
                "ip": self.ip,
                "uid": self.uid,
                "dtype": self.dtype,
            }
        # If attributes are not defined
        except AttributeError:
            return {
                "ip": None,
                "uid": None,
                "dtype": None,
            }

    def __repr__(self) -> str:
        """Represent IntexSpaInfo main attributes."""
        return repr(self.as_dict())
