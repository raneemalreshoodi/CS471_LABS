from django import forms
from .models import Book
from .models import Student, Address, Gallery

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']


## task1

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'address']
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']


##task 2
from .models import Student, Address, Student2, Address2

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']
        widgets = {
            'addresses': forms.CheckboxSelectMultiple(),
        }

class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = ['city']

#### task 3
from django import forms
from .models import Gallery

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'

