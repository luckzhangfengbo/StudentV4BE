from django.db import models

# Create your models here.

# Student :学生
# 生成数据库命令: python manage.py makemigrations, python manage.py migrate
class Student(models.Model):
    gender_choices = (('男', '男'),('女','女'))
    sno = models.IntegerField(db_column="Sno",primary_key=True, null=False) #学号
    name = models.CharField(db_column="SName",max_length=100, null=False) #姓名
    gender = models.CharField(db_column="Gender",max_length=100,choices=gender_choices)
    birthday = models.DateField(db_column="Birthday", null=False) #生日
    mobile = models.CharField(db_column="Mobile",max_length=100) #电话
    email = models.CharField(db_column="Email",max_length=100) #邮箱
    address = models.CharField(db_column="Address",max_length=200) #地址
    image = models.CharField(db_column="Image",max_length=200, null=True) #照片

    class Meta:
        managed = True
        db_table = 'Student'

        def __str__(self):
            return "学号:%s\t姓名:%s\t性别:%s\t" %(self.sno,self.name,self.gender)

