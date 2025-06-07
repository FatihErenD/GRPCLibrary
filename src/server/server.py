from concurrent import futures
import grpc
import uuid
from generated import university_pb2 as pb
from generated import university_pb2_grpc as pb_grpc
from grpc_reflection.v1alpha import reflection
from google.protobuf.empty_pb2 import Empty

# In-memory veri depoları
books = {}
students = {}
loans = {}

# ========== Book Service ==========
class BookService(pb_grpc.BookServiceServicer):
    def ListBooks(self, request, context):
        return pb.BookList(books=list(books.values()))

    def GetBook(self, request, context):
        return books.get(request.id, pb.Book())

    def CreateBook(self, request, context):
        book = request.book
        book_id = str(uuid.uuid4())
        new_book = pb.Book(
            id=book_id,
            title=book.title,
            author=book.author,
            isbn=book.isbn,
            publisher=book.publisher,
            pageCount=book.pageCount,
            stock=book.stock
        )
        books[book_id] = new_book
        return new_book

    def UpdateBook(self, request, context):
        if request.book.id in books:
            books[request.book.id] = request.book
            return request.book
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details('Book not found')
        return pb.Book()

    def DeleteBook(self, request, context):
        if request.id in books:
            del books[request.id]
        return Empty()

# ========== Student Service ==========
class StudentService(pb_grpc.StudentServiceServicer):
    def ListStudents(self, request, context):
        return pb.StudentList(students=list(students.values()))

    def GetStudent(self, request, context):
        return students.get(request.id, pb.Student())

    def CreateStudent(self, request, context):
        student = request.student
        student_id = str(uuid.uuid4())
        new_student = pb.Student(
            id=student_id,
            name=student.name,
            studentNumber=student.studentNumber,
            email=student.email,
            isActive=student.isActive
        )
        students[student_id] = new_student
        return new_student

    def UpdateStudent(self, request, context):
        if request.student.id in students:
            students[request.student.id] = request.student
            return request.student
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details('Student not found')
        return pb.Student()

    def DeleteStudent(self, request, context):
        if request.id in students:
            del students[request.id]
        return Empty()

# ========== Loan Service ==========
class LoanService(pb_grpc.LoanServiceServicer):
    def ListLoans(self, request, context):
        return pb.LoanList(loans=list(loans.values()))

    def GetLoan(self, request, context):
        return loans.get(request.id, pb.Loan())

    def LoanBook(self, request, context):
        loan_id = str(uuid.uuid4())
        loan = pb.Loan(
            id=loan_id,
            studentId=request.studentId,
            bookId=request.bookId,
            loanDate=request.loanDate,
            returnDate="",
            status=pb.LoanStatus.ONGOING
        )
        loans[loan_id] = loan
        return loan

    def ReturnBook(self, request, context):
        if request.loanId in loans:
            loan = loans[request.loanId]
            updated_loan = pb.Loan(
                id=loan.id,
                studentId=loan.studentId,
                bookId=loan.bookId,
                loanDate=loan.loanDate,
                returnDate=request.returnDate,
                status=pb.LoanStatus.RETURNED
            )
            loans[request.loanId] = updated_loan
            return updated_loan
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details('Loan not found')
        return pb.Loan()

# ========== gRPC Server Başlat ==========
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb_grpc.add_BookServiceServicer_to_server(BookService(), server)
    pb_grpc.add_StudentServiceServicer_to_server(StudentService(), server)
    pb_grpc.add_LoanServiceServicer_to_server(LoanService(), server)

    SERVICE_NAMES = (
        pb.DESCRIPTOR.services_by_name['BookService'].full_name,
        pb.DESCRIPTOR.services_by_name['StudentService'].full_name,
        pb.DESCRIPTOR.services_by_name['LoanService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("✅ gRPC Server running on port 50051 with reflection...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
