from django.db import models
# Create your models here.

class Experience(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=255)
    order = models.IntegerField()
   
    def __str__(self) :
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=255)
 
    def __str__(self) :
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(default='default.png', upload_to='projects')
    short_descr = models.TextField()
    tags = models.CharField(max_length=255)
    long_descr = models.TextField(default=short_descr)
    link = models.CharField(max_length=255)

    def __str__(self) :
        return self.title
