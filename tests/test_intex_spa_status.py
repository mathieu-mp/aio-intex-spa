from intex_spa.intex_spa_status import IntexSpaStatus

status_str = "FFFF110F010700220000000080808022000012"
status_int = int("0x" + status_str, 16)


def test_intex_spa_status():
    intex_spa_status = IntexSpaStatus(status_int)
    assert intex_spa_status.power
    assert intex_spa_status.filter
    assert intex_spa_status.heater
    assert not intex_spa_status.jets
    assert not intex_spa_status.bubbles
    assert not intex_spa_status.sanitizer
    assert intex_spa_status.unit == "°C"
    assert intex_spa_status.current_temp == 34
    assert intex_spa_status.preset_temp == 34
