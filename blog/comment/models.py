from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

class Blog(models.Model):
    nameBlog = models.CharField(verbose_name='Название блога', max_length=400, db_index=True, unique=True)
    textBlog = models.TextField(unique=True,verbose_name='Текст блога',max_length=1000000000)
    showBlog = models.BooleanField(verbose_name='Показать нужный нужный блог', default=False)

    class Meta:
        verbose_name = 'Блоги'
        ordering = ['id']


class Comments(MPTTModel):
    body = models.TextField(unique=False,verbose_name='Текст комментарий')
    created_on = models.DateTimeField(default=timezone.now,unique=False,verbose_name='Дата и время')
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null = True, blank=True,
                               related_name='+',unique=False,verbose_name='Родительская и дочерняя связь')

    class Meta:
        verbose_name = 'Комментарии пользователей'
        ordering = ['id']

    @property
    def children(self):
        return Comments.objects.filter(parent=self).order_by('-created_on').all()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False