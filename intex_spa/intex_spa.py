"""IntexSpa"""
import logging
import asyncio
import typing

from .intex_spa_network_layer import IntexSpaNetworkLayer
from .intex_spa_query import IntexSpaQuery
from .intex_spa_object_status import IntexSpaStatus
from .intex_spa_object_info import IntexSpaInfo
from .intex_spa_exceptions import IntexSpaUnreachableException

_LOGGER = logging.getLogger(__name__)


class IntexSpa:
    """
    AsyncIO-enabled class to interface with Intex Spa wifi module

    Attributes
    -------
    network : IntexSpaNetworkLayer
      The network layer object for communications with intex spa wifi module
    status : IntexSpaStatus
      The status object of the spa
    info : IntexSpaInfo
      The info object of the spa
    """

    def __init__(self, address: str = "SPA_DEVICE", port: str = "8990"):
        """
        Initialize IntexSpa instance

        Parameters
        ----------
        address : str, default = "SPA_DEVICE"
          The fqdn or IP of the intex spa wifi module
        port : str, default = "8990"
          The TCP service port the intex spa wifi module
        """
        _LOGGER.info("Initializing IntexSpa instance...")
        self.network = IntexSpaNetworkLayer(address, port)
        self._semaphore = asyncio.Semaphore(1)
        self.status = IntexSpaStatus()
        self.info = IntexSpaInfo()
        _LOGGER.info("IntexSpa instance initialized")

    async def _async_handle_intent(
        self, intent: str = "status", expected_state: typing.Union[bool, int] = None
    ) -> IntexSpaStatus:
        """
        Handle any intent by conversing with the spa wifi module

        An intent can be:
        * update: to refresh the status object of the spa
        * *command*: to change the function state or temperature preset on the spa

        A conversation with the spa is made of one or more queries:
        * A command intent always triggers a preliminary status update
        * Command is sent and response is received
        * Retries can happen as needed

        Parameters
        ----------
        intent : str
          The intent to handle (i.e.: "status", "heater", "preset_temp", ...)
        expected_state : bool | int, optional
          The expected state of the function or the temperature preset

        Returns
        -------
        status : IntexSpaStatus
          The status of the spa
        """

        _LOGGER.debug("'%s' intent: Handling new intent...", intent)

        # Trigger a preliminary update status intent if the provided intent is a command
        if intent != "status" and intent != "info":
            _LOGGER.debug(
                "'%s' intent: triggering a preliminary 'update' intent...", intent
            )
            await self.async_update_status()

        # Run concurrent requests senquentially
        async with self._semaphore:
            if (
                # the provided intent is an update status
                intent == "status"
                # the provided intent is an update info
                or intent == "info"
                # the provided intent is a command
                # and its expected_state differs from the current state
                or getattr(self.status, intent) != expected_state
            ):
                _LOGGER.debug("'%s' intent: a spa query is needed", intent)

                # Attempt maximum 3 times
                for _ in range(3):
                    try:
                        _LOGGER.debug("'%s' intent: new spa query...", intent)
                        # Initialize a query to the spa
                        query = IntexSpaQuery(intent, expected_state)

                        # Send the raw request bytes via the network object
                        await self.network.async_send(query.request_bytes)

                        # Receive the raw response bytes via the network object
                        received_bytes = await self.network.async_receive()
                        # Give the raw received_bytes back to the query object
                        # to render the new status
                        query.render_response_data(received_bytes)
                        if intent == "info":
                            # Update the info object with the data received
                            self.info = IntexSpaInfo(query.response_data)
                            _LOGGER.debug("'%s' intent: new info is rendered", intent)
                            return self.info
                        else:
                            # Update the status object with the data received
                            self.status = IntexSpaStatus(query.response_data)
                            _LOGGER.debug("'%s' intent: new status is rendered", intent)
                            return self.status

                    except (AssertionError,):
                        _LOGGER.info("Malformed spa response during spa querying")
                        await asyncio.sleep(2)
                        continue

                    except (
                        asyncio.IncompleteReadError,
                        asyncio.TimeoutError,
                        ConnectionRefusedError,
                        ConnectionResetError,
                        ConnectionError,
                        OSError,
                    ):
                        _LOGGER.info("Network raised an exception during spa querying")
                        await self.network.async_force_disconnect()
                        await asyncio.sleep(2)
                        continue

                    else:
                        break
                else:  # No retry has succeeded
                    _LOGGER.info("Spa is unreachable")
                    self.status = IntexSpaStatus()
                    raise IntexSpaUnreachableException("Spa is unreachable")

        # Return a status even when getattr(self.status, intent) == expected_state
        # Fixes mathieu-mp/intex-spa#17
        return self.status

    async def async_update_status(self) -> IntexSpaStatus:
        """Update known status of the spa

        Returns
        -------
        status : IntexSpaStatus
          The updated spa status
        """
        return await self._async_handle_intent("status")

    async def async_set(
        self, parameter: str, expected_state: bool = True
    ) -> IntexSpaStatus:
        """
        Set specified parameter to `expected_state`

        Returns
        -------
        status : IntexSpaStatus
          The updated spa status
        """
        return await self._async_handle_intent(parameter, expected_state)

    async def async_set_power(self, expected_state: bool = True) -> IntexSpaStatus:
        """
        Set power function to `expected_state`

        Returns
        -------
        status : IntexSpaStatus
          The updated spa status
        """
        return await self.async_set("power", expected_state)

    async def async_set_filter(self, expected_state: bool = True) -> IntexSpaStatus:
        """
        Set filter function to `expected_state`

        Returns
        -------
        status : IntexSpaStatus
          The updated spa status
        """
        return await self.async_set("filter", expected_state)

    async def async_set_heater(self, expected_state: bool = True) -> IntexSpaStatus:
        """
        Set heater function to `expected_state`

        Returns
        -------
        status : IntexSpaStatus
          The updated spa status
        """
        return await self.async_set("heater", expected_state)

    async def async_set_jets(self, expected_state: bool = True) -> IntexSpaStatus:
        """
        Set jets function to `expected_state`

        Returns
        -------
        status : IntexSpaStatus
          The updated spa status
        """
        return await self.async_set("jets", expected_state)

    async def async_set_bubbles(self, expected_state: bool = True) -> IntexSpaStatus:
        """
        Set bubbles function to `expected_state`

        Returns
        -------
        status : IntexSpaStatus
          The updated spa status
        """
        return await self.async_set("bubbles", expected_state)

    async def async_set_sanitizer(self, expected_state: bool = True) -> IntexSpaStatus:
        """
        Set sanitizer function to `expected_state`

        Returns
        -------
        status : IntexSpaStatus
          The updated spa status
        """
        return await self.async_set("sanitizer", expected_state)

    async def async_set_preset_temp(self, expected_state: int) -> IntexSpaStatus:
        """
        Set preset_temp function to `expected_state`

        Returns
        -------
        status : IntexSpaStatus
          The updated spa status
        """
        return await self._async_handle_intent("preset_temp", expected_state)

    async def async_update_info(self) -> IntexSpaInfo:
        """
        Update known info of the spa

        Returns
        -------
        info : IntexSpaInfo
          The updated spa info
        """
        return await self._async_handle_intent("info")
