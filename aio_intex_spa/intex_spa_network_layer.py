"""IntexSpa"""
import logging
import asyncio
import socket

from .intex_spa_exceptions import IntexSpaDnsException

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
            "Opening TCP connection with the spa at %s:%s with asyncio...",
            self.address,
            self.port,
        )
        try:
            self.reader, self.writer = await asyncio.open_connection(
                self.address, self.port
            )

        except socket.gaierror as err:
            if err.args[0] == socket.EAI_NONAME:
                raise IntexSpaDnsException(
                    f"Cannot resolve DNS address for {self.address}"
                ) from err
            else:
                raise socket.gaierror(err) from err

        _LOGGER.info(
            "TCP connection established with the spa",
        )

    async def _async_disconnect(self) -> None:
        """Close the connection to the spa"""
        # If there is a writer to send a disconnect message
        try:
            _LOGGER.debug("Closing previous TCP connection to the spa with asyncio...")
            self.writer.close()
            await self.writer.wait_closed()
            _LOGGER.info("Previous TCP connection closed with the spa")
        except AttributeError:
            _LOGGER.debug("No previous spa connection known")
        except Exception:  # pylint: disable=broad-except
            _LOGGER.debug(
                "Failure while closing previous TCP connection to the spa, dumping it"
            )
        finally:
            self.reader = None
            self.writer = None

    async def async_force_disconnect(self) -> None:
        """Force reconnecting to the spa"""
        await self._async_disconnect()

    async def async_send(self, bytes_to_write: bytes = None) -> None:
        """Send command to the spa"""
        if self.writer is None or self.reader is None:
            _LOGGER.info("Not connected to the spa, trying to connect...")
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
