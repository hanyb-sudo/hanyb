from . import views
from django.urls import path,re_path
#导入正则地址re_path
app_name = "app"
urlpatterns = [
    path(r'', views.index, name = "index"),
    re_path(r'^(\d+)/$', views.detial1),
    re_path(r'^(\d+)/(\d+)/$', views.detial2),
    re_path(r'^grades/$', views.grades),
    re_path(r'^students/$', views.students),
    re_path(r'^students2/$', views.students2),
    re_path(r'^grades/(\d+)/$', views.grade_students),
    re_path(r'^addstudent/$', views.addstudent),
    re_path(r'^student/(\d+)/$', views.studentPage),
    re_path(r'^studentsearch/$', views.studentSearch),
    re_path(r'^gradesearch/$', views.gradeSearch),
    #HttpRequest属性
    re_path(r'^attributes/$', views.attributes),
    #get属性
    re_path(r'^get1/$', views.get1),
    re_path(r'^get2/$', views.get2),
    #post属性
    re_path(r'^showregister/$', views.showreg),
    re_path(r'^showregister/register/$', views.reg),
    #response属性
    re_path(r'^showresponse/$', views.showresponse),
    #cookie测试
    re_path(r"^cookietest/$", views.cookietest),
    #重定向
    re_path(r"^redirect1/$", views.redirect1),
    re_path(r"^redirect2/$", views.redirect2),
    #session示例
    re_path(r"^main/$", views.main),
    re_path(r"^login/$", views.login),
    re_path(r"^showmain/$", views.showmain),
    re_path(r"^quit/$", views.quit),
    re_path(r"^good/(\d+)/(\d+)$", views.good, name = "good"),
    re_path(r"^extend/$", views.extend),
    re_path(r"^postfile/$", views.postfile, name = "postfile"),
    re_path(r"^showinfo/$", views.showinfo, name = "showinfo"),
    re_path(r'^verifycode/$', views.verifycode, name = 'verifycode'),
    re_path(r'^verifycodefile/$', views.verifycodefile),
    re_path(r'^verifycodecheck/$', views.verifycodecheck),
    re_path(r"^upfile/$", views.upfile),
    re_path(r"^savefile/$", views.savefile),
    #学生分页
    re_path(r"^studentpage/(\d+)/$", views.studentpage),
    re_path(r"^ajaxstudents/$", views.ajaxstudens),
    re_path(r"^getstudentsinfo/$", views.getstudentsinfo),
    re_path(r"^edit/$", views.edit),
    re_path(r"^celery/$", views.celery)
]