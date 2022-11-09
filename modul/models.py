from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Module(models.Model):
    image = models.ImageField(upload_to='modules')
    name = models.CharField(max_length=500)
    order = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Modul"
        verbose_name_plural = "Modullar"
    def __str__(self) -> str:
        return self.name

class Theme(models.Model):
    image = models.ImageField(upload_to='themes')
    title = models.CharField(max_length=500)
    order = models.PositiveSmallIntegerField()
    content = RichTextField(verbose_name="Mazmuni") 

    class Meta:
        verbose_name = "Mavzu"
        verbose_name_plural = "Mavzular"
    def __str__(self) -> str:
        return self.title

class Answer(models.Model):
    content = models.CharField(max_length=500)
    is_true = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Variantlar"
        verbose_name_plural = "Variantlar"
    
    def __str__(self) -> str:
        return self.content

class Question(models.Model):
    theme = models.ForeignKey(Theme, on_delete = models.CASCADE)
    content = models.CharField(max_length=500)
    answers = models.ManyToManyField(Answer)
    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Testlar"
    
    def __str__(self) -> str:
        return self.content

