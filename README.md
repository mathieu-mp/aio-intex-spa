# aio-intex-spa

<!-- badges start -->

[![PyPI version][pypibadge]][pypilink]
![Project Maintenance][maintenance-shield]
[![Open in Remote - Containers][devcontainer-badge]][devcontainer]

<!-- badges end -->

_An AsyncIO-compatible Python client for Intex Spa wifi interface_

## Description

This python package aims to provide an interface with the Intex Spa wifi module.

It is compatible with Intex wifi-enabled spas without any specific hardware, as it uses the built-in Intex wifi module.

It uses direct TCP connection to the spa, and does not require access to the Intex cloud. The built-in Intex wifi module only has to be connected to a wifi Access Point.

It is written with asyncio network functions. It only supports asyncio usage.

## User installation

```bash
python3 -m pip install -U aio-intex-spa
```

## Usage examples

Below are some examples, see `examples` directory for more delight.

### Retrieve spa status
```python
from aio_intex_spa import IntexSpa

async def get_spa_status():
    spa = IntexSpa(SPA_ADDRESS)
    await spa.async_update_status()

asyncio.run(get_spa_status())
```

### Set spa heater state
```python
from aio_intex_spa import IntexSpa

async def set_spa_heater_state():
    spa = IntexSpa(SPA_ADDRESS)
    await spa.async_set_heater(True)

asyncio.run(set_spa_heater_state())
```

## Versioning

The versioning of this python package follows Semantic Versioning 2.0.0

***Reminder**: Major version zero (0.y.z) is for initial development. Anything MAY change at any time. The public API SHOULD NOT be considered stable.*

For Changelog, please read [releases].

<!-- links start -->

[pypilink]: https://pypi.org/project/aio-intex-spa/
[pypibadge]: https://badge.fury.io/py/aio-intex-spa.svg
[releases]: https://github.com/mathieu-mp/aio-intex-spa/releases
[maintenance-shield]: https://img.shields.io/maintenance/yes/2023.svg
[devcontainer]: https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/mathieu-mp/aio-intex-spa
[devcontainer-badge]: https://img.shields.io/static/v1?label=Remote%20-%20Containers&message=Open&color=blue&logo=visualstudiocode

<!-- links end -->