from intex_spa.intex_spa_query import IntexSpaQuery

valid_status_responses = [
    b'{"sid":"12345678901234","data":"FFFF110F010700220000000080808022000012","result":"ok","type":2}\n',
    b'{"sid":"12345678901234","data":"FFFF110F010700B50000000080808022000012","result":"ok","type":2}\n',
    b'{"sid":"12345678901234","data":"FFFF110F0107006400000085808085670000FF","result":"ok","type":2}\n',  # From https://github.com/mathieu-mp/intex-spa/issues/27
    b'{"sid":"12345678901234","data":"FFFF110F01070064000000008080806700008A","result":"ok","type":2}\n',  # From https://github.com/mathieu-mp/intex-spa/issues/27
]
invalid_status_responses = [
    b'{"sid":"12345678901234","data":"FFFF110F010700220000000080808022000044","result":"ok","type":2}\n',  # Arbitrary false checksum
    b'{"sid":"12345678901234","data":"00000000000000000000000000000000000000","result":"ok","type":2}\n',  # Checksum 0x00 means no checksum calculation
]


def test_valid_intex_spa_checksums():
    query = IntexSpaQuery(intent="status")
    query.intex_timestamp = "12345678901234"
    for status_response in valid_status_responses:
        try:
            query.render_response_data(received_bytes=status_response)
        except Exception as exc:
            assert False, f"str(status_response) raised an exception {exc}"


def test_invalid_intex_spa_checksums():
    query = IntexSpaQuery(intent="status")
    query.intex_timestamp = "12345678901234"
    for status_response in invalid_status_responses:
        try:
            query.render_response_data(received_bytes=status_response)
        except AssertionError as exc:
            assert True, f"str(status_response) raised an exception {exc}"
