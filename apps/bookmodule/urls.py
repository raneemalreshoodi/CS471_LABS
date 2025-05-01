from django.urls import path
from . import views  




urlpatterns = [
    path('', views.index, name="books.index"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    # path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('html5/links/', views.links, name="books.links"),
    path('html5/text/formatting/', views.formatting, name="books.formatting"),
    path('html5/listing/', views.listing, name="books.listing"),
    path('html5/tables/', views.tables, name="books.tables"),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>/', views.viewbook),
    path('search', views.search_books, name="books.search"),
    path('simple/query/', views.simple_query, name='simple_query'),
    path('complex/query/', views.complex_query, name='complex_query'),
    path('lookup/query/', views.lookup_query, name='lookup_query'),
    path('lab8/task1/', views.task1, name='task1'),
    path('lab8/task2/', views.task2, name='task2'),
    path('lab8/task3/', views.task3, name='task3'),
    path('lab8/task4/', views.task4, name='task4'),
    path('lab8/task5/', views.task5, name='task5'),
    path('lab8/task7/', views.task7, name='task7'),
    path('lab9_part1/listbooks/', views.list_books, name='list_books'),
    path('lab9_part1/addbook/', views.add_book, name='add_book1'),
    path('lab9_part1/editbook/<int:id>/', views.edit_book, name='edit_book1'),
    path('lab9_part1/deletebook/<int:id>/', views.delete_book, name='delete_book'),
    path('lab9_part2/addbookforms/', views.add_bookforms, name='add_book2'),
    path('lab9_part2/editbookforms/<int:id>/', views.edit_bookforms, name='edit_book2'),
      path('list/', views.list_students, name='list_students'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('add_address/', views.add_address, name='add_address'),
    path('list2/', views.list_students2, name='list_students2'),
    path('add2/', views.add_student2, name='add_student2'),
    path('edit2/<int:id>/', views.edit_student2, name='edit_student2'),
    path('delete2/<int:student_id>/', views.delete_student2, name='delete_student2'),
    path('add_address2/', views.add_address2, name='add_address2'),
    path('gallery/', views.gallery_list, name='gallery_list'),  # <-- this line
    path('gallery/add/', views.add_gallery, name='add_gallery'),



]
