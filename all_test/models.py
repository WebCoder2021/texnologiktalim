import random
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class TestAnswer(models.Model):
    content = models.CharField(max_length=500,verbose_name="Variant")
    is_true = models.BooleanField(default=False,verbose_name='To\'g\'ri yoki xatoligi')

    class Meta:
        verbose_name = "Variant"
        verbose_name_plural = "Variantlar"
    
    def __str__(self) -> str:
        return self.content

class TestQuestion(models.Model):
    content = RichTextField(verbose_name="Savol matni")
    answers = models.ManyToManyField(TestAnswer,verbose_name='Variantlar')
    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Testlar"
    
    def __str__(self) -> str:
        return self.content