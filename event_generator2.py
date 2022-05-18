from event_generator import Severity, KafkaConnection

my_producer = KafkaConnection(
    servers=["broker1:9092", "broker2:9092"], topic="opennms-kafka-events"
)

my_event_fid = my_producer.create_event(
    uei="uei.opennms.org/custom/event/name",
    severity=Severity.NORMAL,
    _foreignSource="requisitionName",
    _foreignId="12345",
)
my_producer.send_event(my_event_fid)
