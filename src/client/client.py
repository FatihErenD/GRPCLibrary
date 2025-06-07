import grpc
from server.generated import university_pb2 as pb
from server.generated import university_pb2_grpc as pb_grpc
from google.protobuf.empty_pb2 import Empty
import datetime

def main():
    # Sunucuya bağlan
    channel = grpc.insecure_channel('localhost:50051')
    book_stub = pb_grpc.BookServiceStub(channel)
    student_stub = pb_grpc.StudentServiceStub(channel)
    loan_stub = pb_grpc.LoanServiceStub(channel)

    # ✅ Yeni kitap ekle
    new_book = pb.Book(
        title="Clean Code",
        author="Robert C. Martin",
        isbn="9780132350884",
        publisher="Prentice Hall",
        pageCount=464,
        stock=5
    )
    created_book = book_stub.CreateBook(pb.CreateBookRequest(book=new_book))
    print("📚 Kitap eklendi:", created_book)

    # ✅ Yeni öğrenci ekle
    new_student = pb.Student(
        name="Fatih Eren Durmuş",
        studentNumber="20231234",
        email="fatih@example.com",
        isActive=True
    )
    created_student = student_stub.CreateStudent(pb.CreateStudentRequest(student=new_student))
    print("👤 Öğrenci eklendi:", created_student)

    # ✅ Kitapları listele
    books = book_stub.ListBooks(Empty())
    print("\n📘 Kitaplar:")
    for book in books.books:
        print("-", book.title, f"({book.id})")

    # ✅ Öğrencileri listele
    students = student_stub.ListStudents(Empty())
    print("\n🧑‍🎓 Öğrenciler:")
    for student in students.students:
        print("-", student.name, f"({student.id})")

    # ✅ Kitap ödünç al
    loan_date = datetime.date.today().isoformat()
    loan_request = pb.LoanBookRequest(
        studentId=created_student.id,
        bookId=created_book.id,
        loanDate=loan_date
    )
    loan = loan_stub.LoanBook(loan_request)
    print("\n📕 Kitap ödünç alındı:", loan)

    # ✅ Ödünçleri listele
    all_loans = loan_stub.ListLoans(Empty())
    print("\n📒 Ödünç Alınan Kitaplar:")
    for l in all_loans.loans:
        print(f"- Loan ID: {l.id}, Book: {l.bookId}, Student: {l.studentId}, Status: {pb.LoanStatus.Name(l.status)}")

    # ✅ Kitap iade et
    return_date = datetime.date.today().isoformat()
    return_request = pb.ReturnBookRequest(
        loanId=loan.id,
        returnDate=return_date
    )
    returned_loan = loan_stub.ReturnBook(return_request)
    print("\n✅ Kitap iade edildi:", returned_loan)

if __name__ == '__main__':
    main()
