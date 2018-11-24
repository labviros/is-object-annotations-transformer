ObjectAnnotations Transformation Service
==================

Changes the coordinate referential frame of [ObjectAnnotations] messages becoming from a list of topics and then publishes to a specific topic.


Streams
---------
| Name | Input (Topic/Message) | Output (Topic/Message) | Description | 
| ---- | --------------------- | ---------------------- | ----------- |
| <GENERIC_NAME> | **LIST_OF_TOPICS** [ObjectAnnotations] | **OUTPUT_TOPIC** [ObjectAnnotations] | Consumes messages from topics which publish [ObjectAnnotations] messages, transform to a given referential frame, then publishes to a chosen topic. Input topics, output topic and destination frame ID can be [configure](https://github.com/labviros/is-object-annotations-transformer/blob/src/conf/options.proto) as you prefer.


[ObjectAnnotations]: https://github.com/labviros/is-msgs/blob/modern-cmake/docs/README.md#is.vision.ObjectAnnotations