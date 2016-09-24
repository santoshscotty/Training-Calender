from django.contrib import admin
from tc.models import student, faculty, course

class studentadmin(admin.ModelAdmin):
	search_fields		= ['name']
	prepopulated_fields	= {'slug':('studentid',)}

class facultyadmin(admin.ModelAdmin):
	search_fields		= ['name']

class courseadmin(admin.ModelAdmin):
	search_fields		= ['name']
	prepopulated_fields	= {'slug':('courseid',)}
	filter_horizontal	= ('student_name',)

#class attendence(admin.ModelAdmin):
	

admin.site.register(student,studentadmin)
admin.site.register(faculty,facultyadmin)
admin.site.register(course,courseadmin)
#admin.site.register(attendence)
