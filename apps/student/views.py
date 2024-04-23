from django.shortcuts import render

# Create your views here.

from student.models import Student
from django.http import JsonResponse
import json
from django.db.models import Q
def get_students(request):
    try:
        obj_students = Student.objects.all().values()
        students = list(obj_students)
        return JsonResponse({'code':1,'data':students})
    except Exception as e:
        return JsonResponse({'code':0,'msg':"获取学生信息出现异常" + str(e)})

def query_student(request):
    #接收传递过来的查询条件 axios默认是json格式, ---字典类型（"inputstr"） -- data = ['inputstr']
    data = json.loads(request.body.decode('utf-8'))

    try:
        #使用Q查询获取满足条件的数据
        obj_students = Student.objects.filter(Q(sno__contains=data['inputstr'])|Q(name__contains=data['inputstr'])
                                              |Q(gender__icontains=data['inputstr'])|Q(birthday__contains=data['inputstr'])
                                                |Q(mobile__contains=data['inputstr'])|Q(email__contains=data['inputstr'])
                                                |Q(address__contains=data['inputstr'])).values()
        students = list(obj_students)
        return JsonResponse({'code': 1, 'data': students})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "查询学生信息出现异常" + str(e)})


def is_exsits_sno(request):
    # 判断学号是否存在
    try:
        data = json.loads(request.body.decode('utf-8'))
        obj_students = Student.objects.filter(sno=data['sno'])
        if obj_students.count() == 0:
            return JsonResponse({'code': 1,'exists': False})
        else:
            return JsonResponse({'code': 1,'exists': True})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "校验学号失败，具体原因" + str(e)})

def add_student(request):
    #新增学生信息
    data = json.loads(request.body.decode('utf-8'))
    try:
        obj_student = Student(sno=data['sno'],name=data['name'],gender=data['gender'],birthday=data['birthday'],
                              mobile=data['mobile'],email=data['email'],address=data['address'])
        obj_student.save()
        obj_students = Student.objects.all().values()
        students = list(obj_students)
        return JsonResponse({'code': 1, 'data': students})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "新增学生信息出现异常" + str(e)})

def update_student(request):
    #新增学生信息
    data = json.loads(request.body.decode('utf-8'))
    try:
        obj_student = Student.objects.get(sno=data['sno'])
        obj_student.name = data['name']
        obj_student.gender = data['gender']
        obj_student.birthday = data['birthday']
        obj_student.mobile = data['mobile']
        obj_student.email = data['email']
        obj_student.address = data['address']

        obj_student.save()
        obj_students = Student.objects.all().values()
        students = list(obj_students)
        return JsonResponse({'code': 1, 'data': students})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "修改学生信息出现异常" + str(e)})