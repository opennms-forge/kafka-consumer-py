# tests.conftest.py

import pytest

from onms_kafka_events import KafkaConnection, Severity

from typing import List


class MockKafka(KafkaConnection):
    def __init__(self, servers: List[str], topic: str) -> None:
        super().__init__(servers, topic)


@pytest.fixture
def test_kafka():
    return KafkaConnection(servers=["localhost:9092"], topic="opennms-kafka-events")


@pytest.fixture
def test_event(test_kafka: KafkaConnection):
    return test_kafka.create_event(
        uei="uei.python.test/event", severity=Severity.WARNING, node_id=1, parm1="one"
    )
