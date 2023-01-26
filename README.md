# onms_kafka_events

This example shows one way to generate protobuf payloads with Python, and send them to a Kafka topic for OpenNMS Horizon/Meridian to consume.

Documentation for configuring the Kafka Consumer feature can be found at https://docs.opennms.com/horizon/latest/operation/deep-dive/events/sources/kafka.html.

## Associating events to nodes

When received, the eventd daemon will attempt to associate the event to a node in the following order:

 * If the `nodeId` field is included, the event will be matched to the node with that database ID.
 * If the event does not have `nodeID`, the parameters `_foreignSource` and `_foreignId` can be included to associate the event based on the requisition name and ID.
 * Any event that cannot match a node on either of these criteria will not be associated with a node.

## Example

```py
from onms_kafka_events import KafkaConnection, Severity

my_producer = KafkaConnection(
    servers=["broker01:9092", "broker02:9092"], topic="opennms-kafka-events"
)

my_event = my_producer.create_event(
    uei="uei.opennms.org/custom/event",
    severity=Severity.WARNING,
)

result = my_producer.send_event(my_event)
```
