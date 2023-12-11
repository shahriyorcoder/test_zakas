from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

TOGRI = (
    ('a', 'a'),
    ('b', 'b'),
    ('c', 'c'),
    ('d', 'd')
)


class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title
    

class Appect_user(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    

class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    a = models.CharField(max_length=150)
    b = models.CharField(max_length=150)
    c = models.CharField(max_length=150)
    d = models.CharField(max_length=150)


    togri_javob = models.CharField(max_length=30, choices=TOGRI, default='a')
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('admindetail', kwargs={'id': self.category.id})


class Taskusers(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    natija = models.CharField(max_length=200)
    checking = models.BooleanField(default=False, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username.username
