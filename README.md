# OpenNMS Kafka Consumer Example
## Python

This example shows one way to generate protobuf payloads with Python, and send them to a Kafka topic for OpenNMS Horizon/Meridian to consume.

Documentation for configuring the Kafka Consumer feature can be found at https://docs.opennms.com/horizon/29/operation/events/sources/kafka.html


A copy of the `kafka-consumer-events.proto` file is included here, and can be found in the repository at https://github.com/OpenNMS/opennms/blob/develop/features/kafka/consumer/src/main/proto/kafka-consumer-events.proto.

The `kafka_consumer_events_pb2.py` file is the output of using the protobuf compiler against the proto definition file.
This file can then be leveraged to create Event objects.

When sending payloads to Kafka, we will serialize the event object as a string, then send it as a bytes object.

## Associating events to nodes

When received, the eventd daemon will attempt to associate the event to a node in the following order:

 * If the `nodeId` field is included, the event will be matched to the node with that database ID.
 * If the event does not have `nodeID`, the parameters `_foreignSource` and `_foreignId` can be included to associate the event based on the requisition name and ID.
 * Any event that cannot match a node on either of these criteria will not be associated with a node.

## Requirements

This example uses two libraries:

* [Google Protobuf](https://developers.google.com/protocol-buffers/docs/pythontutorial)
* [kafka-python](https://kafka-python.readthedocs.io/en/master/)
