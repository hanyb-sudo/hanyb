from django.contrib import admin

# Register your models here.
from .models import Grades,Students,Text
admin.site.register(Text)

class StudentsInfo(admin.TabularInline):#admin.StackedInline
    model = Students
    extra = 2

#注册
@admin.register(Grades)
class GradeAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
    #列表页属性
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5

    #添加、修改页属性
    # fields = ['ggirlnum', 'gboynum','gname', 'gdate', 'isDelete']
    fieldsets = [
        ("num",{"fields":['ggirlnum','gboynum']}),
        ("base",{"fields":['gname','gdate','isDelete']})
    ]

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    # 设置页面列的名称
    gender.short_description = "性别"
    #列表页属性
    list_display = ['pk', 'sname', gender, 'sage', 'scontend', 'isDelete']
    list_per_page = 5
    #执行动作的位置
    actions_on_bottom = True
    actions_on_top = False

# admin.site.register(Grades, GradeAdmin)
# admin.site.register(Student, StudentAdmin)

