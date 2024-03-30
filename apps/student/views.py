from django.shortcuts import render

# Create your views here.

from student.models import Student
from django.http import JsonResponse
def get_students(request):
    try:
        obj_students = Student.objects.all().values()
        students = list(obj_students)
        return JsonResponse({'code':1,'data':students})
    except Exception as e:
        return JsonResponse({'code':0,'msg':"获取学生信息出现异常" + str(e)})