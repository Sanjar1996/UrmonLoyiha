from ckeditor.fields import RichTextField
from django.db import models


class Xodim(models.Model):
    full_name = models.CharField(max_length=250)
    # deportment = models.CharField(max_length=150, blank=True)
    occupation = models.CharField(max_length=150)
    images = models.ImageField(upload_to='images/')
    brith_day = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return self.full_name


class HomeCarusel(models.Model):
    images = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=150)
    sub_title = models.TextField()

    def __str__(self):
        return self.title


class HomeNews(models.Model):
    images = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=350)
    sub_title = models.CharField(max_length=450)
    body = models.TextField()

    def __str__(self):
        return self.title


class HomeVideo(models.Model):
    title = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class ByudjetModel(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class ByudjetPlan(models.Model):
    title = models.ManyToManyField(ByudjetModel)
    plan = models.CharField(max_length=75)
    file = models.FileField(upload_to='files/', blank=True)

    def __str__(self):
        return self.plan


class QuestionModel(models.CharField):
    question = models.CharField(max_length=250)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Service(models.Model):
    icon = models.CharField(max_length=20)
    link = models.CharField(max_length=50)
    title = models.CharField(max_length=75)
    sub_title = models.TextField()

    def __str__(self):
        return self.title


class DockModel(models.Model):
    title = models.CharField(max_length=70)
    sub_title = models.CharField(max_length=250)
    link = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Qaror(models.Model):
    icon = models.CharField(max_length=45)
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=450)
    link = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class Farmon(models.Model):
    icon = models.CharField(max_length=45)
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=450)
    link = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.name


class YangilikModel(models.Model):
    date = models.DateField(auto_now_add=False)
    title = models.CharField(max_length=150)
    descriptions = models.CharField(max_length=150)
    body = RichTextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Rasm(models.Model):
    title = models.CharField(max_length=150, blank=True)
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=45, blank=True)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        self.title