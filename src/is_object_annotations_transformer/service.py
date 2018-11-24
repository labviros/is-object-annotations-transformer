from is_msgs.image_pb2 import ObjectAnnotations
from is_wire.core import Channel, Message, Subscription, Logger
from .utils import load_options
from .transformation import TransformationFetcher, transform_object_annotations


def main():
    log = Logger(name='ObjectAnnotationsTransformer')
    ops = load_options()

    channel = Channel(ops.broker_uri)
    subscription = Subscription(channel)
    for topic in ops.input_topics:
        subscription.subscribe(topic)

    tf_fetcher = TransformationFetcher(ops.broker_uri)

    while True:
        msg = channel.consume()
        annotations = msg.unpack(ObjectAnnotations)
        
        _from, _to = annotations.frame_id, ops.frame_id
        tf = tf_fetcher.get_transformation(_from, _to)
        if tf is None:
            log.warn("Can't get transformation from '{}' to '{}'", _from, _to)
            continue

        annotations = transform_object_annotations(annotations, tf, _to)
        msg = Message(content=annotations)
        channel.publish(msg, topic=ops.output_topic)


if __name__ == '__main__':
    main()
