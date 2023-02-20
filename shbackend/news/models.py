from django.db import models

# Create your models here.

# 국내 뉴스
class DomesticNews (models.Model):
    title = models.TextField(unique=True, verbose_name="뉴스 기사 제목")
    url = models.URLField(max_length=500, verbose_name="뉴스 링크")
    press = models.CharField(max_length=128, verbose_name="언론사")
    date = models.CharField(max_length=128, verbose_name="보도 날짜")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'shinhan_DomesticNews'
        verbose_name = '국내 뉴스'
        verbose_name_plural = '국내 뉴스'


# 해외 뉴스
class OverseasNews (models.Model):
    title = models.TextField(unique=True, verbose_name="뉴스 기사 제목")
    url = models.URLField(max_length=500, verbose_name="뉴스 링크")
    press = models.CharField(max_length=128, verbose_name="언론사")
    date = models.CharField(max_length=128, verbose_name="보도 날짜")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'shinhan_OverseasNews'
        verbose_name = '해외 뉴스'
        verbose_name_plural = '해외 뉴스'