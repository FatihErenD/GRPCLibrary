# 📡 gRPCurl Test Results

Bu dosyada `grpcurl` komut satırı aracı kullanılarak yapılan testlerin çıktıları ve açıklamaları yer almaktadır.

---

## ✅ 1. Tüm Servisleri Listeleme

```bash
grpcurl -plaintext localhost:50051 list
```

### 📤 Çıktı:
```bash
grpc.reflection.v1alpha.ServerReflection
university.BookService
university.LoanService
university.StudentService
```
## ✅ 2. BookService Metotlarını Görüntüleme

```bash
grpcurl -plaintext localhost:50051 describe university.BookService
```

### 📤 Çıktı:
```bash
university.BookService is a service:
service BookService {
  rpc CreateBook ( .university.CreateBookRequest ) returns ( .university.Book );
  rpc DeleteBook ( .university.DeleteBookRequest ) returns ( .google.protobuf.Empty );
  rpc GetBook ( .university.BookId ) returns ( .university.Book );
  rpc ListBooks ( .google.protobuf.Empty ) returns ( .university.BookList );
  rpc UpdateBook ( .university.UpdateBookRequest ) returns ( .university.Book );
}
```
## ✅ 3. Kitap Ekleme

```bash
grpcurl -plaintext -d '{
  "book": {
    "title": "gRPC Basics",
    "author": "Jane Doe",
    "isbn": "9780000000001",
    "publisher": "OpenBooks",
    "pageCount": 150,
    "stock": 10
  }
}' localhost:50051 university.BookService/CreateBook
```

### 📤 Çıktı:
```bash
{
  "id": "89b6eed8-cd22-411b-93ea-08768ac0384c",
  "title": "gRPC Basics",
  "author": "Jane Doe",
  "isbn": "9780000000001",
  "publisher": "OpenBooks",
  "pageCount": 150,
  "stock": 10
}
```

## ✅ 4. Kitap Listeleme

```bash
grpcurl -plaintext -d '{}' localhost:50051 university.BookService/ListBooks
```

### 📤 Çıktı:
```bash
{
  "books": [
    {
      "id": "89b6eed8-cd22-411b-93ea-08768ac0384c",
      "title": "gRPC Basics",
      "author": "Jane Doe",
      "isbn": "9780000000001",
      "publisher": "OpenBooks",
      "pageCount": 150,
      "stock": 10
    }
  ]
}
```

## ✅ 5. Öğrenci Ekleme

```bash
grpcurl -plaintext -d '{
  "student": {
    "name": "Ali Yılmaz",
    "studentNumber": "20230001",
    "email": "ali@example.com",
    "isActive": true
  }
}' localhost:50051 university.StudentService/CreateStudent
```

### 📤 Çıktı:
```bash
{
  "id": "2d51801c-52ed-47c2-8559-a968af9bd1a4",
  "name": "Ali Yılmaz",
  "studentNumber": "20230001",
  "email": "ali@example.com",
  "isActive": true
}
```

## ✅ 6. Öğrenci Listeleme

```bash
grpcurl -plaintext -d '{}' localhost:50051 university.StudentService/ListStudents
```

### 📤 Çıktı:
```bash
{
  "students": [
    {
      "id": "2d51801c-52ed-47c2-8559-a968af9bd1a4",
      "name": "Ali Yılmaz",
      "studentNumber": "20230001",
      "email": "ali@example.com",
      "isActive": true
    }
  ]
}
```
