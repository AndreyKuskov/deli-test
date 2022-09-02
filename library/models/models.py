from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    patronymic = models.CharField(verbose_name='Отчество', 
                               max_length=128, 
                               blank=True, 
                               null=True)
    phone_number = models.CharField(verbose_name='Номер телефона', 
                                max_length=128,
                                blank=True,
                                null=True)
    
    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
 
class Book(models.Model):
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        verbose_name='Автор')
    name = models.CharField('Название книги', max_length=255)
    photo = models.ImageField('Фото', upload_to='book/')
    annotation = models.TextField('Аннотация')
    publication_year = models.PositiveBigIntegerField('Год публикации')
    created_at = models.DateTimeField(
        'created_at', 
        auto_now_add=True, 
        blank=True)
    
    class Meta:
        db_table = 'books'
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-created_at']
    
    def __str__(self) -> str:
        return self.name