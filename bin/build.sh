#!/usr/bin/env bash

python -m grpc_tools.protoc \
       -I protobufs \
       --python_out=gosu_grpc \
       $(find protobufs -iname "*.proto")

python -m grpc_tools.protoc \
       -I protobufs \
       --grpc_python_out=gosu_grpc \
       $(find protobufs/google/cloud -iname "*.proto")

sed -i -E '/from google\.protobuf/b; s/from google/from gosu_grpc.google/g' $(find gosu_grpc/google -iname '*.py')
