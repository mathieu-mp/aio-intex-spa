"""IntexSpaExceptions"""


class IntexSpaUnreachableException(Exception):
    """Exception raised when spa is unreachable"""


class IntexSpaDnsException(Exception):
    """Exception raised when DNS address cannot be resolved"""
