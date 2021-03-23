
### 编译生成 pb.py2
```bash
python -m grpc_tools.protoc -I . --python_out=.  proto/crawler/crawleddata.proto
```

### 编译生成 pb.py2 和 pb2_grpc.py
```bash
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. proto/crawler/crawleddata.proto
```

### 编译多个
```bash
sh proto/compile.sh
```