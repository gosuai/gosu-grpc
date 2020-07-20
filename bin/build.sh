#!/usr/bin/env bash

shopt -s globstar

rm -rf ./google/*

python3 -m grpc_tools.protoc \
       --proto_path=googleapis \
       --python_out=. \
       --grpclib_python_out=. \
       googleapis/google/cloud/{dialogflow/v2,texttospeech/v1,translate/v3}/**/*.proto
