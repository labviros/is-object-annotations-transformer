#/bin/bash
set -e

docker run --rm -v `pwd`:/protos mendonca/is-msgs-protoc:1.1.8 options.proto
mv -vuf options_pb2.py ../is_object_annotations_transformer