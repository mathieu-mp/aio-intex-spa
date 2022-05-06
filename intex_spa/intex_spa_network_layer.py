"""IntexSpa"""
import logging
import asyncio

_LOGGER = logging.getLogger(__name__)


class IntexSpaNetworkLayer:
    """
    AsyncIO-enabled class to manage network-layer communications with Intex Spa wifi module

    Attributes
    -------
    address : str
        The fqdn or IP of the intex spa wifi module
    port : str
        The TCP service port the intex spa wifi module
    reader : asyncio.StreamReader
        The StreamReader connected to the spa
    writer : asyncio.StreamWriter
        The StreamWriter connected to the spa
    """

    def __init__(self, address: str, port: str):
        """
        Initialize IntexSpaNetworkLayer class

        Parameters
        ----------
        address : str
            The fqdn or IP of the intex spa wifi module
        port : str
            The TCP service port of the intex spa wifi module
        """
        self.address = address
        self.port = port

        self.reader: asyncio.StreamReader = None
        self.writer: asyncio.StreamWriter = None

    async def _async_connect(self) -> None:
        """Initialize a connection to the spa"""
        _LOGGER.debug(
            "Opening TCP connection with the spa at %s:%s with asyncio",
            self.address,
            self.port,
        )
        self.reader, self.writer = await asyncio.open_connection(
            self.address, self.port
        )
        _LOGGER.info(
            "TCP connection established with the spa",
        )

    async def _async_disconnect(self) -> None:
        """Close the connection to the spa"""
        _LOGGER.debug(
            "Closing TCP connection to the spa with asyncio",
        )
        self.writer.close()
        await self.writer.wait_closed()
        _LOGGER.info(
            "TCP connection closed with the spa",
        )

    async def async_send(self, bytes_to_write: bytes = None) -> None:
        """Send command to the spa"""
        if self.writer is None or self.reader is None:
            _LOGGER.info("Not connected to the spa")
            await self._async_connect()
        elif self.writer.is_closing() or self.reader.at_eof():
            _LOGGER.info("Connection with the spa seems to be broken")
            await self._async_disconnect()
            await self._async_connect()

        _LOGGER.debug("Sending bytes to the spa: %s", bytes_to_write)
        self.writer.write(bytes_to_write)
        await self.writer.drain()

    async def async_receive(self) -> None:
        """Receive response from the spa"""
        response_as_bytes = await self.reader.readline()
        _LOGGER.debug("Receiving bytes from the spa: %s", response_as_bytes)
        return response_as_bytes
