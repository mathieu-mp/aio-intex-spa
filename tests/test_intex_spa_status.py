from aio_intex_spa.intex_spa_object_status import IntexSpaStatus


def test_intex_spa_status():
    """Test function for IntexSpaStatus with standard input status."""
    status_str = "FFFF110F010700220000000080808022000012"
    status_int = int("0x" + status_str, 16)
    intex_spa_status = IntexSpaStatus(status_int)
    assert intex_spa_status.power
    assert intex_spa_status.filter
    assert intex_spa_status.heater
    assert intex_spa_status.jets is False
    assert intex_spa_status.bubbles is False
    assert intex_spa_status.sanitizer is False
    assert intex_spa_status.unit == "°C"
    assert intex_spa_status.current_temp == 34
    assert intex_spa_status.error_code is False
    assert intex_spa_status.preset_temp == 34


def test_intex_spa_error_code():
    """Test function for IntexSpaStatus with E81 error input status."""
    status_str = "FFFF110F010700B50000000080808022000012"
    status_int = int("0x" + status_str, 16)
    intex_spa_status = IntexSpaStatus(status_int)
    assert intex_spa_status.power
    assert intex_spa_status.filter
    assert intex_spa_status.heater
    assert intex_spa_status.jets is False
    assert intex_spa_status.bubbles is False
    assert intex_spa_status.sanitizer is False
    assert intex_spa_status.unit == "°C"
    assert intex_spa_status.current_temp is False
    assert intex_spa_status.error_code == "E81"
    assert intex_spa_status.preset_temp == 34
