from django.db import models


class Classes(models.Model):
    name = models.CharField('名称', max_length=100)

    class Meta:
        db_table = 'classes'
        verbose_name_plural = verbose_name = '班级'

    def __str__(self):
        return self.name
