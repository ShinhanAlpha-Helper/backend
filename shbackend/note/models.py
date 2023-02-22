from django.db import models

# Create your models here.

class Note (models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, verbose_name='사용자')
    title = models.CharField(max_length=128, verbose_name="용어")
    content = models.TextField(verbose_name="설명")
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'shinhan_member_note'
        verbose_name = '사용자 단어장'
        verbose_name_plural = '사용자 단어장'


class Bookmark(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, verbose_name='사용자')
    note = models.ForeignKey('note.Note', on_delete=models.CASCADE, verbose_name='단어')

    class Meta:
        db_table = 'shinhan_bookmark'
        verbose_name = '단어 즐겨찾기'
        verbose_name_plural = '단어 즐겨찾기'