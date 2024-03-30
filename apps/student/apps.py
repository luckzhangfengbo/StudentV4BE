from django.apps import AppConfig


class StudentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
#     这个地方出现了异常报错是RuntimeError: Model class student.models.Student doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
# /Users/zhangfengbo/project/Jetbrain/PycharmProjects/StudentV4BE/StudentV4BE/settings.py changed, reloading.
#     解决方式是把下面的    name = 'apps.student'改成name = 'student'

    name = 'student'
