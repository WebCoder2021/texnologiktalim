from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Books(models.Model):
    image = models.ImageField(upload_to='themes')
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    file = models.FileField(upload_to='books')

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"
    def __str__(self) -> str:
        return self.title

class InternetResources(models.Model):
    image = models.ImageField(upload_to='themes')
    title = models.CharField(max_length=500)
    url = models.URLField()

    class Meta:
        verbose_name = "Internet resurs"
        verbose_name_plural = "Internet resurslar"
    def __str__(self) -> str:
        return self.title


class VideoLessons(models.Model):
    image = models.ImageField(upload_to='themes')
    title = models.CharField(max_length=500)
    url = models.URLField(null=True,blank=True)
    iframe = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = "Video dars"
        verbose_name_plural = "Video darslar"
    def __str__(self) -> str:
        return self.title




class Questionnaire(models.Model):
    publish = models.BooleanField(default=False)
    title = models.CharField(max_length=500)
    ans1 = models.CharField(max_length=200)
    ans2 = models.CharField(max_length=200)
    ans3 = models.CharField(max_length=200,null=True,blank=True)
    ans4 = models.CharField(max_length=200,null=True,blank=True)
    ans5 = models.CharField(max_length=200,null=True,blank=True)
    ans6 = models.CharField(max_length=200,null=True,blank=True)
    res1 = models.PositiveSmallIntegerField(null=True,blank=True)
    res2 = models.PositiveSmallIntegerField(null=True,blank=True)
    res3 = models.PositiveSmallIntegerField(null=True,blank=True)
    res4 = models.PositiveSmallIntegerField(null=True,blank=True)
    res5 = models.PositiveSmallIntegerField(null=True,blank=True)
    res6 = models.PositiveSmallIntegerField(null=True,blank=True)

    class Meta:
        verbose_name = "So'rovnoma"
        verbose_name_plural = "So'rovnomalar"
    def __str__(self) -> str:
        return self.title