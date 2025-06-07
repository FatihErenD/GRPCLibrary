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
![image](https://github.com/user-attachments/assets/6f6d9cff-b505-4197-8405-45f291e0863d)

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
![image](https://github.com/user-attachments/assets/c247aeab-18cb-4b5f-a69b-2e04d89f00bb)

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
![image](https://github.com/user-attachments/assets/d19e38f8-15d8-42b0-8312-fa219cdeb120)


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
![image](https://github.com/user-attachments/assets/71c11400-aa74-400f-8688-4060b26b0184)


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

![image](https://github.com/user-attachments/assets/7c7f3897-d5ee-4726-b9f7-65f044fd4e14)


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
![image](https://github.com/user-attachments/assets/89eab1ce-6bf8-4f30-bdae-0d525fa09d94)

---

## ⚠️ Uyarı: Windows CMD Ortamında JSON Geçme Sorunları

Windows CMD terminalinde, `grpcurl` komutlarında `-d` ile JSON veri göndermek çoğu zaman kaçış karakterleri (`\"`) nedeniyle hataya yol açabilmektedir.

Aşağıdaki nedenlerle bazı komutlar doğrudan CMD ortamında çalışmamaktadır:

- `"` karakterlerinin düzgün kaçırılmaması (`\"`)
- Çok satırlı JSON'un desteklenmemesi
- `Too many arguments.` veya `Unexpected token` gibi hatalar alınması

### ✅ Çözüm Önerileri:

- JSON verisini dış bir dosyaya (`book.json`, `student.json`) kaydedip şu şekilde çalıştırmak:
  ```bash
  grpcurl -plaintext -d @book.json localhost:50051 university.BookService/CreateBook
  ```
- Alternatif olarak Git Bash veya PowerShell kullanmak
Bu sebeple, bu testlerde verilen komutlar teorik olarak doğrudur ancak CMD üzerinde çalıştırılması yerine dosya veya PowerShell kullanımı önerilir.

