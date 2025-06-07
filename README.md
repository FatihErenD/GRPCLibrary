# 📘 gRPC Library System

This project implements a university library system using gRPC and Protocol Buffers.

## 📁 Project Structure

- `university.proto`: Protocol Buffers definition
- `server/`: gRPC server implementation in Python
- `client/`: gRPC client to test the API
- `grpcurl-tests.md`: gRPCurl-based service testing

## 🧪 How to Run

### 1. Install dependencies
```bash
pip install grpcio grpcio-tools grpcio-reflection
```
### 2. Generate Python stubs

```bash
python -m grpc_tools.protoc -I. -I[path-to-_proto] --python_out=./generated --grpc_python_out=./generated university.proto
```

### 3. Start the server
```bash
cd src
python server/server.py
```

### 4. Run the client
```bash
cd src
python -m client/client.py
```

### 5. Run grpcurl tests
```bash
grpcurl -plaintext localhost:50051 list
```
