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

## Changelog

This python package follows Semantic Versioning 2.0.0

***Reminder**: Major version zero (0.y.z) is for initial development. Anything MAY change at any time. The public API SHOULD NOT be considered stable.*

### 0.5.0 - 2022-06-21

Parse eventual `error_code` from status

**Breaking change**: `current_temp` can now return `False` if an error code is read

### 0.4.1 - 2022-06-20

Handle concurrent requests sequentially

### 0.4.0 - 2022-06-18

Add "direct" async_set method to IntexSpa class \
Remove platforms parameter to IntexSpa class

### 0.3.0 - 2022-06-18

Add platforms parameter to IntexSpa class

### 0.2.1 - 2022-06-11

Make compatible with Python 3.9

### 0.2.0 - 2022-06-11

Allow client to import package classes

### 0.1.2 - 2022-06-04

✨ First release to PyPI

### 0.1.0 - 2022-06-04

✨ First release

<!-- links start -->

[maintained]: https://img.shields.io/maintenance/yes/2022.svg
[pypilink]: https://pypi.org/project/intex-spa/
[pypibadge]: https://badge.fury.io/py/intex-spa.svg

<!-- links end -->