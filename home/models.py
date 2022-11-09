from django.db import models
from ckeditor.fields import RichTextField
from .validators import validate_file_extension
# Create your models here.
class Books(models.Model):
    image = models.ImageField(upload_to='themes',verbose_name="Rasm")
    title = models.CharField(max_length=500,verbose_name="Kitob nomi")
    author = models.CharField(max_length=200,verbose_name='Kitob muallifi')
    file = models.FileField(upload_to='books',verbose_name='Kitob fayli',validators=[validate_file_extension])

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"
    def __str__(self) -> str:
        return self.title

class InternetResources(models.Model):
    image = models.ImageField(upload_to='themes',verbose_name="Resurs rasmi")
    title = models.CharField(max_length=500,verbose_name='Sarlavha')
    url = models.URLField(verbose_name='Resurs url manzili')

    class Meta:
        verbose_name = "Internet resurs"
        verbose_name_plural = "Internet resurslar"
    def __str__(self) -> str:
        return self.title


class VideoLessons(models.Model):
    image = models.ImageField(upload_to='video_lessons',verbose_name='Video dars rasmi')
    title = models.CharField(max_length=500,verbose_name='Sarlavha')
    url = models.URLField(null=True,blank=True)
    iframe = models.TextField(null=True,blank=True,verbose_name="YouTube ifareme")

    class Meta:
        verbose_name = "Video dars"
        verbose_name_plural = "Video darslar"
    def __str__(self) -> str:
        return self.title




class Questionnaire(models.Model):
    publish = models.BooleanField(default=False,verbose_name="So'rovnoma holati")
    title = models.CharField(max_length=500,verbose_name="So'rovnoma savoli")
    ans1 = models.CharField(max_length=200,verbose_name="Variant")
    ans2 = models.CharField(max_length=200,verbose_name="Variant")
    ans3 = models.CharField(max_length=200,null=True,blank=True,verbose_name="Variant")
    ans4 = models.CharField(max_length=200,null=True,blank=True,verbose_name="Variant")
    ans5 = models.CharField(max_length=200,null=True,blank=True,verbose_name="Variant")
    ans6 = models.CharField(max_length=200,null=True,blank=True,verbose_name="Variant")
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