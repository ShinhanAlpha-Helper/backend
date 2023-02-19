from django.db import models

# Create your models here.

class Dictionary (models.Model):
    title = models.CharField(max_length=128, unique=True, verbose_name="용어")
    content = models.TextField(verbose_name="설명")
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'shinhan_dictionary'
        verbose_name = '사전'
        verbose_name_plural = '사전'