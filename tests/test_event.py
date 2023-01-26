# tests.test_event.py

import pytest

from onms_kafka_events import KafkaConnection, Severity


def test_event(test_event):
    assert test_event.uei == "uei.python.test/event"
    assert test_event.node_id == 1
    assert test_event.parameter[0].name == "parm1"
    assert test_event.parameter[0].value == "one"
    assert (
        bytes(test_event.SerializeToString())
        == b"\n\x15uei.python.test/event\x12\x0ekafka-consumer\x18\x03(\x01j\x0c\n\x05parm1\x12\x03one"
    )
