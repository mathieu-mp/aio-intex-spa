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

Below are some examples, see `tests` directory for more examples

### Retrieve spa status
```python
import asyncio

async def use_intex_spa():
    intex_spa = IntexSpa(SPA_ADDRESS)
    await intex_spa.async_update_status()

asyncio.run(use_intex_spa())
```

### Set spa function state
```python
import asyncio

async def use_intex_spa():
    intex_spa = IntexSpa(SPA_ADDRESS)
    await intex_spa.async_set_heater(True)

asyncio.run(use_intex_spa())
```

## Changelog

This python package follows semantic versioning specification (SemVer).

### 0.1.0 - 2022-06-04

✨ First release

<!-- links start -->

[maintained]: https://img.shields.io/maintenance/yes/2022.svg
[pypilink]: https://pypi.org/project/intex-spa/
[pypibadge]: https://badge.fury.io/py/intex-spa.svg

<!-- links end -->