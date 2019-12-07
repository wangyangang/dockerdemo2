from django.db import models


class Classes(models.Model):
    name = models.CharField('名称', max_length=100)

    class Meta:
        db_table = 'classes'
        verbose_name_plural = verbose_name = '班级'

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField('教师', max_length=20)

    class Meta:
        db_table = 'teacher'
        verbose_name = verbose_name_plural = '教师'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.name


