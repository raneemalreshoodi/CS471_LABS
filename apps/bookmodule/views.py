from django.shortcuts import render,redirect,get_object_or_404  # Add this import
from django.http import HttpResponse
from .models import Book
from .models import Student,Address
from django.db.models import Q
from django.db.models import Count
#lab 10

def list_books(request):
    books = Book.objects.all() 
    print(books)
    return render(request, 'bookmodule/list_books.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        edition = request.POST['edition']
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return redirect('list_books')
    return render(request, 'bookmodule/add_book.html')


def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.edition = request.POST['edition']
        book.save()
        return redirect('list_books')
    return render(request, 'bookmodule/edit_book.html', {'book': book})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('list_books')

# forms part
from .forms import BookForm

def list_books2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/list_books2.html', {'books': books})


def add_bookforms(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books2')
    else:
        form = BookForm()
    return render(request, 'bookmodule/add_bookforms.html', {'form': form})

def edit_bookforms(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books2')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/edit_bookforms.html', {'form': form})

##
def task7(request):
    city_counts = Student.objects.values('address__city').annotate(num_students=Count('id'))
    return render(request, 'bookmodule/task7.html', {'city_counts': city_counts})


def task1(request):
    books = Book.objects.filter(Q(price__lte=50))
    return render(request, 'bookmodule/task1.html', {'books': books})

def task2(request):
    books = Book.objects.filter(
        Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task2.html', {'books': books})

def task3(request):
    books = Book.objects.filter(
        Q(edition__lte=2) & ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task3.html', {'books': books})

def task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': books})

from django.db.models import Count, Sum, Avg, Max, Min

def task5(request):
    aggregation = Book.objects.aggregate(
        num_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'aggregation': aggregation})


def simple_query(request):

    books = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': books})


def complex_query(request):
    
    expensive_books = Book.objects.filter(price__gt=20.0)
    return render(request, 'bookmodule/bookList2.html', {'books': expensive_books})

def lookup_query(request):
    mybooks = Book.objects.filter(author__isnull=False) \
                          .filter(title__icontains='The') \
                          .filter(edition__gte=2) \
                          .exclude(price__lte=20)[:10]

    if len(mybooks) > 1:
        return render(request, 'bookmodule/lookup.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')


def index2(request, val1=0):
    return HttpResponse(f"value1 = {val1}")


def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2
    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)

def index(request):
    return render(request, "bookmodule/index.html")

def aboutus(request):
    return render(request, "bookmodule/aboutus.html")



def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html")

def links(request):
    return render(request, "bookmodule/links.html")

def formatting(request):
    return render(request, "bookmodule/formatting.html")

def listing(request):
    return render(request, "bookmodule/listing.html")

def tables(request):
    return render(request, "bookmodule/tables.html")


def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

def search_books(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        search_in_title = request.POST.get('option1')
        search_in_author = request.POST.get('option2')
        books = []

        for book in __getBooksList():
            match = False
            if search_in_title and keyword in book['title'].lower():
                match = True
            if search_in_author and keyword in book['author'].lower():
                match = True
            if match:
                books.append(book)

        return render(request, "bookmodule/bookList.html", {'books': books})

    return render(request, "bookmodule/search.html")
