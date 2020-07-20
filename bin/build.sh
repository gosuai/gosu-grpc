#!/usr/bin/env bash

rm -rf ./google/*

python3 -m grpc_tools.protoc \
       --proto_path=googleapis \
       --python_out=. \
       --grpclib_python_out=. \
       $(find googleapis/google/cloud/{dialogflow/v2,texttospeech/v1,translate/v3} -iname "*.proto")
