from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    student = Students.stuObj.get(pk =1)
    return render(request, 'myApp/head.html',{"stu":student})


def detial1(request, num):
    return HttpResponse("detial -%s"%num)
def detial2(request, num1, num2):
    return HttpResponse("detial -%s-%s"%(num1,num2))

from . models import Grades,Students
def grades(request):
    #去模型里取数据
    gradesList = Grades.objects.all()
    #将数据传递给模板，模板再渲染页面，将渲染好的页面返回给浏览器
    # return render(request, 'myApp/grades.html', {"grades":gradesList})



def students(request):
    #去模型里取数据
    studentsList = Students.stuObj.all()
    #将数据传递给模板，模板再渲染页面，将渲染好的页面返回给浏览器
    return render(request, 'myApp/students.html', {"num":10,"students":studentsList,"str":"hello","list":["hello","goodbye","byebye"]
                                                   ,"code":"<h1>good man</h1>"})

def students2(request):
    #会报异常MultipleObjectsReturned at /students2/，找到了多个对象
    studnetsList = Students.stuObj2.get(sgender = True)
    #将数据传递给模板，模板再渲染页面，将渲染好的页面返回给浏览器
    return HttpResponse(">>>>>>>>>>>>......")


def grade_students(request, grade_id):
    #先拿到对应的班级信息
    grade = Grades.objects.get(pk = grade_id)
    #再通过班级拿到班级中的学生信息
    studentsList = grade.student_set.all()
    # 将数据传递给模板，模板再渲染页面，将渲染好的页面返回给浏览器
    return render(request, 'myApp/students.html', {"students": studentsList})

def addstudent(request):
    grade = Grades.objects.get(pk=1)
    Students.stuObj2.createObj("李明",23,True, "我是李明",grade,"2020-1-11","2020-4-22")
    return HttpResponse("创建成功！")


#分页显示学生
def studentPage(request, page_num):
    page_num = int(page_num)
    studentsList = Students.stuObj.all()[(page_num-1)*4 : page_num*4]
    return render(request, 'myApp/students.html', {"students": studentsList})


from django.db.models import Max
def studentSearch(request):
    # studentsList = Students.stuObj.filter(sname__startswith="严")
    # studentsList = Students.stuObj.filter(sname__contains="韩")
    # studentsList = Students.stuObj.filter(pk__in=[5,1,2,3,4])
    # studentsList = Students.stuObj.filter(sage__gt=30)
    maxAge = Students.stuObj.aggregate(Max('sage'))#返回的是字典类型
    studentsList = Students.stuObj.filter(sage = maxAge.get('sage__max'))
    return render(request, 'myApp/students.html', {"students": studentsList})

from django.db.models import F,Q
def gradeSearch(request):
    # gradesList = Grades.objects.filter(ggirlnum__gt=F('gboynum')+20)
    # gradesList = Grades.objects.filter(Q(ggirlnum__gte = 40) | Q(gboynum__gte = 40))

    #跨关联查询
    #描述中带有"严茂萍"这三个字的数据是属于哪个班级的
    gradesList = Grades.objects.filter(students__scontend__contains = "严茂萍")
    return render(request, 'myApp/grades.html', {"grades": gradesList})

#打印HttpRequest属性
def attributes(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("HttpRequest属性页面")


#获取get传递的数据
#获取单个值
def get1(request):
    a = request.GET.get("a")
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse("a = %s  b = %s  c = %s"%(a,b,c))
def get2(request):
    a = request.GET.getlist("a")
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')
    return HttpResponse("a1 = %s  a2 = %s  c = %s" % (a1, a2, c))

#获取post传递的数据
def showreg(request):
    return render(request, 'myApp/register.html')

def reg(request):
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    hobby = request.POST.getlist("hobby")
    return HttpResponse("注册成功！name =%s   gender =%s  age =%s   hobby =%s "%(name, gender, age, hobby))

#response属性
def showresponse(request):
    res = HttpResponse()
    res.content = b'Hello'
    print(res.content)
    print(res.charset)
    print(res.status_code)
    print(res.content_type)
    return res

#cookie
def cookietest(request):
    res = HttpResponse()
    res.write(request.COOKIES["1"])
    #设置cookie值
    # res.set_cookie("1","you are a good man")
    return res


#重定向
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
def redirect1(request):
    # return HttpResponseRedirect("/hanyb/redirect2")
    return redirect("/hanyb/redirect2")

def redirect2(request):
    return HttpResponse("我是重定向2")

#session示例
def main(request):
    #取session
    username = request.session.get('name', default = '游客')
    return render(request, "myApp/main.html", {'username':username})
def login(request):

    return render(request, "myApp/login.html")
def showmain(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    #存储session
    request.session["name"] = username
    request.session.set_expiry(5)
    # request.session["password"] = password
    # request.session[username] = password
    return redirect('/hanyb/main/')
from django.contrib.auth import logout
def quit(request):
    #清除session
    logout(request)    #推荐使用
    # request.session.flush()
    # request.session.clear()
    return redirect('/hanyb/main/')

def good(request, num1, num2):
    numList = []
    numList.append(num1)
    numList.append(num2)
    return render(request, "myApp/good.html", {"num":numList})

def extend(request):
    return render(request, "myApp/extend.html")

def postfile(request):
    return render(request, "myApp/postfile.html")
def showinfo(request):
    name = request.POST.get("username")
    pwd = request.POST.get("password")
    return render(request, "myApp/showinfo.html", {"username":name,"password":pwd})


#验证码
def verifycode(request):
    #引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象
    font = ImageFont.truetype('C:\Windows\Fonts\STFANGSO.TTF', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    # import io
    # buf = io.StringIO()
    from io import BytesIO
    buf = BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'img/png')

def verifycodefile(request):
    flag = request.session.get('flag', default = True)
    str = ""
    if flag == False:
        str += "验证码输入错误，请重新输入"
        request.session.clear()
    return render(request, 'myApp/verifycodefile.html', {"flag":str})
def verifycodecheck(request):
    if request.POST.get('verifycode').upper() == request.session.get("verifycode").upper():
        return HttpResponse("登陆成功！")
    else:
        request.session['flag'] = False
        return redirect('/hanyb/verifycodefile/')

#上传文件
import os
from django.conf import settings
def upfile(request):
    return render(request, 'myApp/upfile.html')
#保存文件
def savefile(request):
    if request.method == 'POST':
        f = request.FILES["file"]
        #合成文件在服务端的路径
        filePath = os.path.join(settings.MDEIA_ROOT, f.name)
        #分段读取上传的文件，并写入文件夹
        with open(filePath, "wb") as fp:
            for info in f.chunks():
                fp.write(info)
        return HttpResponse("上传成功！")
    else:
        return HttpResponse("上传失败！")

#学生分页
from django.core.paginator import Paginator
def studentpage(request, page_num):
    #所有学生列表
    studentsList = Students.stuObj2.all()
    paginator = Paginator(studentsList, 4)
    page = paginator.page(page_num)
    number = len(page)
    return render(request, 'myApp/studentpage.html', {"students":page})

def ajaxstudens(request):
    return render(request, 'myApp/ajaxstudents.html')

from django.http import JsonResponse
def getstudentsinfo(request):
    stus = Students.stuObj.all()
    list = []
    for stu in stus:
        list.append([stu.sname, stu.sage])
    return JsonResponse({"students": list})

def edit(request):
    return render(request, 'myApp/edit.html')

from myApp import task
def celery(request):
    task.func.delay()
    return render(request, 'myApp/celery.html')

