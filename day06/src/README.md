# How to start server

## Compile *.proto file

```shell
python3 -m grpc_tools.protoc -I./protobuf --python_out=./protobuf --grpc_python_out=./protobuf --pyi_out=./protobuf protobuf/spaceship.proto
```

## Run server

```shell
python3 reporting_server.py
```

## Ex00

```shell
python3 reporting_client.py 1745 40.0409 −29 00 28.118
```

## Ex01

```shell
python3 reporting_client_v2.py 1745 40.0409 −29 00 28.118
```

## Ex01

```shell
python3 reporting_client_v3.py scan 1745 40.0409 −29 00 28.118
python3 reporting_client_v3.py list
```