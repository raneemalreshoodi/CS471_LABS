from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)
    
    def __str__(self):
        return self.title

# task1


class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city
class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, default=1)  # <-- Add default here

    def __str__(self):
        return self.name

#task 2
# models.py

class Address2(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=20)  # 👈 add default
    addresses = models.ManyToManyField(Address2)

    def __str__(self):
        return self.name

### task3 
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery_images/')
    description = models.TextField(null=True, blank=True)  # <-- add this


    def __str__(self):
        return self.title