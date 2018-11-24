from is_wire.core import Channel, Message, Logger
from is_msgs.image_pb2 import ObjectAnnotations

channel = Channel('amqp://localhost:5672')

for topic_id in range(3):
    annotations = ObjectAnnotations()
    annotations.frame_id = 1000 + topic_id + 1
    for i in range(2):
        ob = annotations.objects.add()
        for j in range(3):
            kp = ob.keypoints.add()
            kp.id = topic_id + i + j
            kp.position.x = topic_id + j
            kp.position.y = topic_id + j
            kp.position.z = topic_id + j

    msg = Message(content=annotations)
    topic = 'SkeletonsGrouper.{}.Localization'.format(topic_id)
    channel.publish(msg, topic=topic)
