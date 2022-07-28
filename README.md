# intex-spa

<!-- badges start -->

[![PyPI version][pypibadge]][pypilink]
[![Maintained][Maintained]](#)

<!-- badges end -->

_An AsyncIO-compatible Intex Spa wifi client_

## Description

This python package aims to provide an interface with the Intex Spa wifi module.

It is compatible with Intex wifi-enabled spas without any specific hardware, as it uses the built-in Intex wifi module.

It uses direct TCP connection to the spa, and does not require access to the Intex cloud. The built-in Intex wifi module only has to be connected to a wifi Access Point.

It is written with asyncio network functions. It only supports asyncio usage.

## User installation

```bash
python3 -m pip install -U intex-spa
```

## Usage examples

Below are some examples, see `examples` directory for more delight.

### Retrieve spa status
```python
from intex_spa import IntexSpa

async def use_intex_spa():
    intex_spa = IntexSpa(SPA_ADDRESS)
    await intex_spa.async_update_status()

asyncio.run(use_intex_spa())
```

### Set spa function state
```python
from intex_spa import IntexSpa

async def use_intex_spa():
    intex_spa = IntexSpa(SPA_ADDRESS)
    await intex_spa.async_set_heater(True)

asyncio.run(use_intex_spa())
```

## Versioning

The versioning of this python package follows Semantic Versioning 2.0.0

***Reminder**: Major version zero (0.y.z) is for initial development. Anything MAY change at any time. The public API SHOULD NOT be considered stable.*

For Changelog, please read [releases].

<!-- links start -->

[maintained]: https://img.shields.io/maintenance/yes/2022.svg
[pypilink]: https://pypi.org/project/intex-spa/
[pypibadge]: https://badge.fury.io/py/intex-spa.svg
[releases]: https://github.com/mathieu-mp/intex-spa/releases

<!-- links end -->