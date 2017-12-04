from django.contrib import admin
	# Register your models here.
from .models import JobTitle, Department  # Department 추가 등록

class JobTitleAdmin(admin.ModelAdmin):
	list_display = ('id', 'title')  # 이렇게 안하면 title만 보인다.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'upper_department')

admin.site.register(JobTitle, JobTitleAdmin)
admin.site.register(Department) # Department 추가 등록
